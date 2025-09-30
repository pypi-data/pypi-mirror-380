import re
from unittest import mock
from simdb.config import Config
from io import StringIO


def test_create_config():
    Config()


@mock.patch("appdirs.site_config_dir")
@mock.patch("appdirs.user_config_dir")
def test_load_config(user_config_dir, site_config_dir):
    user_config_dir.return_value = ""
    site_config_dir.return_value = ""
    config = Config()
    config.load()
    user_config_dir.assert_called_once_with("simdb")
    site_config_dir.assert_called_once_with("simdb")
    assert config.list_options() == []
    version_regex = re.compile(r"\d\.\d")
    assert version_regex.match(config.api_version)


@mock.patch("appdirs.site_config_dir")
@mock.patch("appdirs.user_config_dir")
def test_load_config_from_specified_file(user_config_dir, site_config_dir):
    user_config_dir.return_value = ""
    site_config_dir.return_value = ""
    config = Config()
    stream = StringIO()
    stream.write(
        """
    [db]
    type = sqlite
    file = /tmp/simdb.db
    """
    )
    stream.seek(0)
    config.load(file=stream)
    user_config_dir.assert_called_once_with("simdb")
    site_config_dir.assert_called_once_with("simdb")
    assert config.list_options() == [
        "db.type: sqlite",
        "db.file: /tmp/simdb.db",
    ]
    version_regex = re.compile(r"\d\.\d")
    assert version_regex.match(config.api_version)
