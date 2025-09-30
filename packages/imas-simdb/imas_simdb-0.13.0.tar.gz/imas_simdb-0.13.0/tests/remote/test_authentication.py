import pytest
from unittest import mock
from simdb.config import Config

try:
    import easyad

    has_easyad = True
except ImportError:
    has_easyad = False
try:
    import flask

    has_flask = True
except ImportError:
    has_flask = False

        
@mock.patch("simdb.config.Config.get_option")
@pytest.mark.skipif(not has_flask, reason="requires flask library")
def test_check_role(get_option):
    from simdb.remote.core.auth import check_role, User
    from flask import Flask

    app = Flask("test")
    config = Config()
    app.simdb_config = config
    with app.app_context():
        get_option.return_value = 'user1,"user2", user3'
        ok = check_role(config, User("user1", ""), "test_role")
        assert ok
        get_option.assert_called_with("role.test_role.users", default="")
        ok = check_role(config, User("user4", ""), None)
        assert ok
        ok = check_role(config, User("user4", ""), "test_role")
        assert not ok


@mock.patch("simdb.config.Config.get_option")
@pytest.mark.skipif(not has_easyad, reason="requires easyad library")
@pytest.mark.skipif(not has_flask, reason="requires flask library")
def test_check_auth(get_option):
    from simdb.remote.core.auth import check_auth

    patcher = mock.patch("easyad.EasyAD")
    easy_ad = patcher.start()

    config = Config()
    get_option.side_effect = lambda name, default=None: {
        "server.admin_password": "abc123",
        "authentication.type": "ActiveDirectory",
        "authentication.ad_server": "test.server",
        "authentication.ad_domain": "test.domain",
        "authentication.ad_cert": "test.cert",
    }.get(name, default)   
    class request:
        class authorization:
            username = ""
            password = ""
        headers = {}
    request.authorization.username = "admin"
    request.authorization.password = "abc123"
    ok = check_auth(config, request)    
    assert ok
    get_option.assert_called_once_with("server.admin_password")

    def auth(user, password, **kwargs):
        if user == "user" and password == "password":
            return {"sAMAccountName": "user", "mail": "user@email.com"}
        return None

    easy_ad().authenticate_user.side_effect = auth
    request.authorization.username = "user"
    request.authorization.password = "password"
    ok = check_auth(config, request)    
    assert ok
    easy_ad.assert_called_with(
        {
            "AD_SERVER": "test.server",
            "AD_DOMAIN": "test.domain",
            "AD_CA_CERT_FILE": "test.cert",
        }
    )
    easy_ad().authenticate_user.assert_called_once_with(
        "user", "password", json_safe=True
    )
    request.authorization.username = "user"
    request.authorization.password = "wrong"
    request.headers = {"Authorization": ""}
    ok = check_auth(config, request)
    assert not ok

