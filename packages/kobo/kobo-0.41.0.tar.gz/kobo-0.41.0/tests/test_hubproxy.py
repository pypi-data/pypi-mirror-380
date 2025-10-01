import socket
import http.client as httplib
import xmlrpc.client

import six.moves.xmlrpc_client as xmlrpclib

import pytest
import gssapi
import mock
import sys

from kobo.xmlrpc import SafeCookieTransport, retry_request_decorator
from kobo.conf import PyConfigParser
from kobo.client import HubProxy


@pytest.fixture(autouse=True)
def requests_session():
    """Mocker for requests.Session; autouse to ensure no accidental real requests.

    Note the tests in this file can't be implemented using requests_mocker because that
    library doesn't track info about authentication.
    """
    with mock.patch("requests.Session") as s:
        # 'with requests.Session()' returns the session instance.
        s.return_value.__enter__.return_value = s.return_value
        yield s


class FakeTransport(SafeCookieTransport):
    """A fake XML-RPC transport where every request succeeds without doing anything.

    Subclasses the real SafeCookieTransport so we get a real CookieJar.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fake_transport_calls = []

    def request(self, host, path, request, verbose=False):
        self.fake_transport_calls.append((path, request))
        return []


def error_raising_transport(exception, bad_function, exception_args=(),
                            exception_kwargs={}):
    # Fake Transport class that raises specific exceptions.
    class FakeTransport(SafeCookieTransport):
        """A fake XML-RPC transport where every request succeeds without doing anything.

        Subclasses the real SafeCookieTransport so we get a real CookieJar.
        """

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.exception_count = 0

        def request(self, host, path, request, verbose=False):
            # Only raise error for a specific faulty function. Hub proxy makes
            # a lot of requests during init we want to allow. Request is binary
            # xml which should contain our function as a string
            if bad_function in request:
                self.exception_count += 1
                raise exception(*exception_args, **exception_kwargs)

            return []

    return FakeTransport

def test_login_token_oidc(requests_session):
    """Login with OIDC client credentials flow."""

    hub_url = "https://example.com/myapp/endpoint"
    login_url = "https://example.com/myapp/auth/tokenoidclogin/"
    token_url = "https://sso.example.com/protocol/openid-connect/token"

    conf = PyConfigParser()
    conf.load_from_dict(
        {
            "HUB_URL": hub_url,
            "AUTH_METHOD": "token_oidc",
            "OIDC_CLIENT_ID": "test-client",
            "OIDC_CLIENT_SECRET": "secret-token",
            "OIDC_AUTH_SERVER_TOKEN_URL": token_url,
            "CA_CERT": "/path/to/ca-bundle.crt"
        }
    )

    transport = FakeTransport()
    proxy = HubProxy(conf, transport=transport)

    with mock.patch("requests.post") as mock_post:
        mock_post.return_value.json.return_value = {"access_token": "secret-token"}

        # Force a login
        proxy._login(force=True)

        mock_post.assert_called_once_with(
            "https://sso.example.com/protocol/openid-connect/token",
            data={
                "grant_type": "client_credentials",
                "client_id": "test-client",
                "client_secret": "secret-token",
                "scope": "openid"
            },
            timeout=30
        )

    # Cookies should have been shared between session and transport
    assert requests_session.return_value.cookies is transport.cookiejar

    requests_session.return_value.get.assert_called_once_with(
        "https://example.com/myapp/auth/tokenoidclogin/",
        headers={"Authorization": "Bearer secret-token"},
        verify="/path/to/ca-bundle.crt"
    )


def test_login_gssapi(requests_session):
    """Login with gssapi method obtains session cookie via SPNEGO & krb5login."""

    hub_url = "https://example.com/myapp/endpoint"
    login_url = "https://example.com/myapp/auth/krb5login/"

    conf = PyConfigParser()
    conf.load_from_dict(
        {"HUB_URL": hub_url, "AUTH_METHOD": "gssapi",}
    )

    transport = FakeTransport()
    proxy = HubProxy(conf, transport=transport)

    # Proxy might have already done some calls during initialization.
    # We're trying to test login in isolation, so keep track of how many
    # mock calls there have been already.
    mock_get = requests_session.return_value.get
    calls_before = len(mock_get.mock_calls)

    # Force a login
    proxy._login(force=True)

    # Cookies should have been shared between session and transport
    assert requests_session.return_value.cookies is transport.cookiejar

    # Check the requests done
    calls = mock_get.mock_calls[calls_before:]

    assert calls[0][0] == ""
    call_args = calls[0][1]
    call_kwargs = calls[0][2]

    # It should have made a request to log in
    assert call_args == (login_url,)

    # It should have enabled SPNEGO auth.
    # More details about this object are verified in a separate test.
    assert "HTTPSPNEGOAuth" in str(type(call_kwargs["auth"]))

    # It should have verified the result
    assert calls[1][0] == "().raise_for_status"

    # And that's all
    assert len(calls) == 2


def test_login_gssapi_krb_opts(requests_session):
    """Login with gssapi method prepares auth using correct gssapi parameters
    according to config."""

    hub_url = "https://hub.example.com/myapp/endpoint"
    login_url = "https://hub.example.com/myapp/auth/krb5login/"

    conf = PyConfigParser()
    conf.load_from_dict(
        {
            "HUB_URL": hub_url,
            "AUTH_METHOD": "gssapi",
            "CA_CERT": "/some/ca-bundle.pem",
            "KRB_PRINCIPAL": "someclient@EXAMPLE.COM",
            "KRB_SERVICE": "SVC",
            "KRB_REALM": "REALM.EXAMPLE.COM",
            "KRB_KEYTAB": "some-keytab",
            "KRB_CCACHE": "some-cache",
        }
    )

    transport = FakeTransport()
    proxy = HubProxy(conf, transport=transport)

    mock_get = requests_session.return_value.get
    calls_before = len(mock_get.mock_calls)

    with mock.patch("requests_gssapi.HTTPSPNEGOAuth") as mock_auth:
        with mock.patch("gssapi.Credentials") as mock_creds:
            # Force a login
            proxy._login(force=True)

    get_call = mock_get.mock_calls[calls_before]

    # It should have prepared credentials with the details from config
    mock_creds.assert_called_once_with(
        name=gssapi.Name("someclient@EXAMPLE.COM", gssapi.NameType.kerberos_principal),
        store={"client_keytab": "some-keytab", "ccache": "FILE:some-cache"},
        usage="initiate",
    )

    # It should have prepared auth with those credentials and our configured
    # server principal
    mock_auth.assert_called_once_with(
        creds=mock_creds.return_value,
        mutual_authentication=2,
        target_name=gssapi.Name(
            "SVC/hub.example.com@REALM.EXAMPLE.COM", gssapi.NameType.kerberos_principal
        ),
    )

    # It should have used the configured CA bundle when issuing the request
    assert get_call[2]["verify"] == "/some/ca-bundle.pem"


def test_login_gssapi_principal_needs_keytab(requests_session):
    """Login with gssapi method raises if principal is provided without keytab."""
    hub_url = "https://hub.example.com/myapp/endpoint"

    conf = PyConfigParser()
    conf.load_from_dict(
        {
            "HUB_URL": hub_url,
            "AUTH_METHOD": "gssapi",
            "KRB_PRINCIPAL": "someclient@EXAMPLE.COM",
        }
    )

    transport = FakeTransport()
    logger = mock.Mock()
    proxy = HubProxy(conf, transport=transport, logger=logger)

    proxy._login(force=True)

    # This is pretty dumb: login() swallows all exceptions (probably for no good reason).
    # The only hint there was a problem is a DEBUG log message, so we detect the error
    # that way.
    logger.debug.assert_called_with(
        "Failed to create new session: Cannot specify a principal without a keytab"
    )


def test_no_auto_logout(requests_session):
    """auto_logout argument warns of deprecation"""
    conf = PyConfigParser()
    conf.load_from_dict({"HUB_URL": 'https://example.com/hub'})

    transport = FakeTransport()
    with pytest.deprecated_call():
        HubProxy(conf, transport=transport, auto_logout=True)


def test_proxies_to_xmlrpc(requests_session):
    """HubProxy proxies to underlying XML-RPC ServerProxy"""
    conf = PyConfigParser()
    conf.load_from_dict({"HUB_URL": 'https://example.com/hub'})

    transport = FakeTransport()
    proxy = HubProxy(conf, transport=transport)

    proxy.some_obj.some_method()

    # Last call should have invoked the method I requested
    (_, request_xml) = transport.fake_transport_calls[-1]
    assert b'some_obj.some_method' in request_xml


def test_pass_transport_args(requests_session):
    """HubProxy proxies to underlying XML-RPC ServerProxy"""
    conf = PyConfigParser()
    conf.load_from_dict({"HUB_URL": 'https://example.com/hub'})
    transport_args = {"retry_count": 2, "retry_timeout": 45}
    with mock.patch(
            "kobo.xmlrpc.SafeCookieTransport") as mock_transport_class, mock.patch(
            "kobo.xmlrpc.retry_request_decorator",
            return_value=mock_transport_class):
        HubProxy(conf, transport_args=transport_args)
        mock_transport_class.assert_called_with(context=mock.ANY,
                                                retry_count=2,
                                                retry_timeout=45)


@pytest.mark.parametrize("exception, exception_args, exception_kwargs",
                         [(socket.error, (), {}),
                          (httplib.CannotSendRequest, (), {}),
                          (xmlrpclib.Fault, ["1", "PermissionDenied"], {})]
                         )
def test_proxy_retries_on_error(requests_session, capsys, exception, exception_args, exception_kwargs):
    """HubProxy proxy retry class captures exceptions"""
    retry_count = 2
    conf = PyConfigParser()
    conf.load_from_dict({"HUB_URL": 'https://example.com/hub'})
    TransportClass = retry_request_decorator(
        error_raising_transport(exception, b"faulty.function", exception_args, exception_kwargs)
    )
    transport = TransportClass(retry_count=retry_count, retry_timeout=1)
    proxy = HubProxy(conf, transport=transport)

    with pytest.raises(exception):
        proxy.faulty.function()

    assert transport.exception_count == retry_count + 1
    captured = capsys.readouterr()
    assert captured.err.count("XML-RPC connection to example.com failed") == retry_count



@pytest.mark.parametrize("exception_string, retried",
                         [("PermissionDenied: Login required.", True),
                          ("SomeOtherError: hub broke.", False)]
                         )
def test_proxy_xmlrpc_fault(requests_session, capsys, exception_string, retried):
    """HubProxy proxy retries xmlrpc fault on PermissionDenied errors"""
    retry_count = 2
    conf = PyConfigParser()
    conf.load_from_dict({"HUB_URL": 'https://example.com/hub'})
    TransportClass = retry_request_decorator(
        error_raising_transport(xmlrpc.client.Fault,
                                b"faulty.function",
                                [1, exception_string],
                                {})
    )
    transport = TransportClass(retry_count=retry_count, retry_timeout=1)
    proxy = HubProxy(conf, transport=transport)

    with pytest.raises(xmlrpc.client.Fault):
        proxy.faulty.function()

    if retried:
        assert transport.exception_count == retry_count + 1
        captured = capsys.readouterr()
        assert captured.err.count("XML-RPC connection to example.com failed") == retry_count
    else:
        assert transport.exception_count == 1
        captured = capsys.readouterr()
        assert captured.err.count(
            "XML-RPC connection to example.com failed") == 0
