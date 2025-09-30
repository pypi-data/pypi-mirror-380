import datetime
import itertools
import os
from pathlib import Path
from typing import Dict, List, Optional, Tuple

from flask import jsonify, request
from flask_restx import Namespace, Resource

from ....database import DatabaseError
from ....database.models import metadata as models_meta
from ....database.models import simulation as models_sim
from ....uri import URI
from ... import APIConstants
from ...core.typing import current_app
from ...core.alias import create_alias_dir
from ...core.auth import User, requires_auth
from ...core.cache import cache, cache_key, clear_cache
from ...core.errors import error
from ...core.path import secure_path

api = Namespace("simulations", path="/")


def _update_simulation_status(
    simulation: models_sim.Simulation, status: models_sim.Simulation.Status, user
) -> None:
    from ....email.server import EmailServer

    old_status = simulation.status
    simulation.status = status
    simulation.set_meta(
        status.value.lower().replace(" ", "_") + "_on",
        datetime.datetime.now().isoformat(),
    )
    if status != old_status and simulation.watchers.count():
        server = EmailServer(current_app.simdb_config)
        msg = f"""\
Simulation status changed from {old_status} to {status}.

Updated by {user}.

Note: please don't reply to this email, replies to this address are not monitored. 
"""
        to_addresses = [w.email for w in simulation.watchers]
        if to_addresses:
            server.send_message(f"Simulation {simulation.alias}", msg, to_addresses)


def _validate(simulation, user) -> Dict:
    from ....validation import ValidationError, Validator

    schema = Validator.validation_schema()
    try:
        Validator(schema).validate(simulation)
        _update_simulation_status(simulation, models_sim.Simulation.Status.PASSED, user)
        return {
            "passed": True,
        }
    except ValidationError as err:
        _update_simulation_status(simulation, models_sim.Simulation.Status.FAILED, user)
        return {
            "passed": False,
            "error": str(err),
        }


def _set_alias(alias: str):
    character = None
    if alias.endswith("-"):
        character = "-"
    elif alias.endswith("#"):
        character = "#"

    if not character:
        return None, -1

    next_id = 1
    aliases = current_app.db.get_aliases(alias)
    for existing_alias in aliases:
        existing_id = int(existing_alias.split(character)[1])
        if next_id <= existing_id:
            next_id = existing_id + 1
    alias = "%s%d" % (alias, next_id)

    return alias, next_id


def _build_trace(sim_id: str) -> dict:
    try:
        simulation = current_app.db.get_simulation(sim_id)
    except DatabaseError as err:
        return {"error": str(err)}
    data = simulation.data(recurse=False)

    status = simulation.find_meta("status")
    if status:
        status = status[0].value
        if isinstance(status, str):
            data["status"] = status
        else:
            data["status"] = status.value
        status_on_name = data["status"] + "_on"
        status_on = simulation.find_meta(status_on_name)
        if status_on:
            data[status_on_name] = status_on[0].value

    replaces = simulation.find_meta("replaces")
    if replaces:
        data["replaces"] = _build_trace(replaces[0].value)

    replaced_on = simulation.find_meta("replaced_on")
    if replaced_on:
        data["deprecated_on"] = replaced_on[0].value

    replaces_reason = simulation.find_meta("replaces_reason")
    if replaces_reason:
        data["replaces_reason"] = replaces_reason[0].value

    return data


@api.route("/simulations")
class SimulationList(Resource):
    parser = api.parser()
    parser.add_argument(
        APIConstants.LIMIT_HEADER,
        location="headers",
        type=int,
        help="Limit returned results",
    )
    parser.add_argument(
        APIConstants.PAGE_HEADER,
        location="headers",
        type=int,
        help="Specify the page of results to return",
    )

    @api.expect(parser)
    @api.response(200, "Success")
    @api.response(401, "Unauthorized")
    @requires_auth()
    @cache.cached(key_prefix=cache_key)
    def get(self, user: User):
        from ....query import QueryType, parse_query_arg

        limit = int(request.headers.get(SimulationList.LIMIT_HEADER, 100))
        page = 1
        names = []
        constraints = []
        if request.args:
            constraints: List[Tuple[str, str, QueryType]] = []
            for name in request.args:
                names.append(name)
                values = request.args.getlist(name)
                for value in values:
                    constraint = parse_query_arg(value)
                    if constraint[0]:
                        constraints.append((name,) + constraint)

        if constraints:
            count, data = current_app.db.query_meta_data(
                constraints, names, limit=limit, page=page
            )
        else:
            count, data = current_app.db.list_simulation_data(
                meta_keys=names, limit=limit, page=page
            )

        return jsonify(data)

    @requires_auth()
    def post(self, user: User):
        try:
            data = request.get_json()

            if "simulation" not in data:
                return error("Simulation data not provided")

            simulation = models_sim.Simulation.from_data(data["simulation"])
            simulation.user = user.name

            if "alias" in data["simulation"]:
                alias = data["simulation"]["alias"]
                (updated_alias, next_id) = _set_alias(alias)
                if updated_alias:
                    simulation.meta.append(models_meta.MetaData("seqid", next_id))
                    simulation.alias = updated_alias
                else:
                    simulation.alias = alias
            else:
                simulation.alias = simulation.uuid.hex[0:8]

            staging_dir = (
                Path(current_app.simdb_config.get_option("server.upload_folder"))
                / simulation.uuid.hex
            )

            files = list(itertools.chain(simulation.inputs, simulation.outputs))
            common_root = None
            if files:
                paths = [f.uri.path for f in files]
                if len(paths) > 1:
                    common_root = Path(os.path.commonpath(paths))

            for sim_file in files:
                path = secure_path(sim_file.uri.path, common_root, staging_dir)
                if not path.exists():
                    raise ValueError("simulation file %s not uploaded" % sim_file.uuid)
                if sim_file.uri.scheme.name == "file":
                    sim_file.uri = URI(scheme="file", path=path)

            result = {
                "ingested": simulation.uuid.hex,
            }

            if current_app.simdb_config.get_option(
                "validation.auto_validate", default=False
            ):
                result["validation"] = _validate(simulation, user)

            if current_app.simdb_config.get_option(
                "validation.error_on_fail", default=False
            ):
                if simulation.status == models_sim.Simulation.Status.NOT_VALIDATED:
                    raise Exception(
                        "Validation config option error_on_fail=True without auto_validate=True."
                    )
                elif simulation.status == models_sim.Simulation.Status.FAILED:
                    result[
                        "error"
                    ] = "Simulation validation failed and server has error_on_fail=True."
                    response = jsonify(result)
                    response.status_code = 400
                    return response

            replaces = simulation.find_meta("replaces")
            if not current_app.simdb_config.get_option(
                "development.disable_replaces", default=False
            ):
                if replaces and replaces[0].value:
                    sim_id = replaces[0].value
                    try:
                        replaces_sim = current_app.db.get_simulation(sim_id)
                    except DatabaseError:
                        replaces_sim = None
                    if replaces_sim is None:
                        pass
                        # raise ValueError(f'Simulation replaces:{sim_id} is not a valid simulation identifier.')
                    else:
                        _update_simulation_status(
                            replaces_sim, models_sim.Simulation.Status.DEPRECATED, user
                        )
                        replaces_sim.set_meta("replaced_by", simulation.uuid)
                        current_app.db.insert_simulation(replaces_sim)

            current_app.db.insert_simulation(simulation)
            clear_cache()

            try:
                create_alias_dir(simulation)
            except OSError:
                pass

            return jsonify(result)
        except (DatabaseError, ValueError) as err:
            return error(str(err))


@api.route("/simulation/<path:sim_id>")
class Simulation(Resource):
    @requires_auth()
    @cache.cached(key_prefix=cache_key)
    def get(self, sim_id: str, user: User):
        try:
            simulation = current_app.db.get_simulation(sim_id)
            if simulation:
                return jsonify(simulation.data(recurse=True))
            return error("Simulation not found")
        except DatabaseError as err:
            return error(str(err))

    parser = api.parser()
    parser.add_argument(
        'status', type=str, location="json", help = "status", required=True
    )
    @api.expect(parser)
    @requires_auth("admin")
    def patch(self, sim_id: str, user: User = Optional[None]):
        try:
            data = request.get_json()
            if "status" not in data:
                return error("Status not provided")
            simulation = current_app.db.get_simulation(sim_id)
            if simulation is None:
                raise ValueError(f"Simulation {sim_id} not found.")
            status = models_sim.Simulation.Status(data["status"])
            _update_simulation_status(simulation, status, user)
            current_app.db.insert_simulation(simulation)
            clear_cache()
            return {}
        except DatabaseError as err:
            return error(str(err))

    @requires_auth("admin")
    def delete(self, sim_id: str, user: User):
        try:
            simulation = current_app.db.delete_simulation(sim_id)
            clear_cache()
            files = []
            for file in itertools.chain(simulation.inputs, simulation.outputs):
                files.append("%s (%s)" % (file.uuid, file.file_name))
                os.remove(os.path.join(file.directory, file.file_name))
            if simulation.inputs or simulation.outputs:
                directory = (
                    simulation.inputs[0].directory
                    if simulation.inputs
                    else simulation.outputs[0].directory
                )
                os.rmdir(directory)
            return jsonify({"deleted": {"simulation": simulation.uuid, "files": files}})
        except DatabaseError as err:
            return error(str(err))


@api.route("/validate/<string:sim_id>")
class ValidateSimulation(Resource):
    @requires_auth()
    def post(self, sim_id, user: User):
        try:
            simulation = current_app.db.get_simulation(sim_id)
            result = _validate(simulation, user)
            current_app.db.insert_simulation(simulation)
            clear_cache()
            return jsonify(result)
        except DatabaseError as err:
            return error(str(err))


@api.route("/trace/<path:sim_id>")
class SimulationTrace(Resource):
    @requires_auth()
    @cache.cached(key_prefix=cache_key)
    def get(self, sim_id: str, user: User):
        try:
            data = _build_trace(sim_id)
            return jsonify(data)
        except DatabaseError as err:
            return error(str(err))
