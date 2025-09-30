from typing import Dict, Any
import base64
import enum

try:
    import simplejson as json
except ImportError:
    import json


def _custom_hook(obj: Dict[str, str]) -> Any:
    import numpy as np
    import uuid

    if "_type" in obj:
        if obj["_type"] == "numpy.ndarray":
            np_bytes = base64.decodebytes(obj["bytes"].encode())
            return np.frombuffer(np_bytes, dtype=obj["dtype"])
        elif obj["_type"] == "uuid.UUID":
            return uuid.UUID(obj["hex"])
        else:
            obj_type = obj["_type"]
            raise ValueError(f"Unknown type to deserialise {obj_type}.")
    return obj


class CustomDecoder(json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        kwargs["object_hook"] = _custom_hook
        super().__init__(*args, **kwargs)


class CustomEncoder(json.JSONEncoder):
    def __init__(self, *args, **kwargs):
        kwargs["allow_nan"] = False
        if json.__name__ == "simplejson":
            kwargs["ignore_nan"] = True
        super().__init__(*args, **kwargs)

    def default(self, obj: Any) -> Any:
        import numpy as np
        import uuid

        if isinstance(obj, np.ndarray):
            bytes = base64.b64encode(obj.data).decode()
            return {"_type": "numpy.ndarray", "dtype": obj.dtype.name, "bytes": bytes}
        elif isinstance(obj, uuid.UUID):
            return {"_type": "uuid.UUID", "hex": obj.hex}
        elif isinstance(obj, enum.Enum):
            return obj.value
        return json.JSONEncoder.default(self, obj)
