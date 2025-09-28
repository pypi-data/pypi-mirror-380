from unittest import TestCase, mock

import requests

from enhydris_api_client import EnhydrisApiClient
from htimeseries import HTimeseries

from . import mock_session


class GetTokenTestCase(TestCase):
    @mock_session(
        **{
            "get.return_value.cookies": {"csrftoken": "reallysecret"},
            "post.return_value.cookies": {"acookie": "a cookie value"},
        }
    )
    def setUp(self, mock_requests_session):
        self.mock_requests_session = mock_requests_session
        self.client = EnhydrisApiClient("https://mydomain.com")
        self.client.get_token("admin", "topsecret")

    def test_makes_post_request(self):
        self.mock_requests_session.return_value.post.assert_called_once_with(
            "https://mydomain.com/api/auth/login/",
            data="username=admin&password=topsecret",
            allow_redirects=False,
        )


class GetTokenFailTestCase(TestCase):
    @mock_session(**{"post.return_value.status_code": 404})
    def test_raises_exception_on_post_failure(self, mock_requests_session):
        self.client = EnhydrisApiClient("https://mydomain.com")
        with self.assertRaises(requests.HTTPError):
            self.client.get_token("admin", "topsecret")


class GetTokenEmptyUsernameTestCase(TestCase):
    @mock_session()
    def setUp(self, mock_requests_session):
        self.mock_requests_session = mock_requests_session
        self.client = EnhydrisApiClient("https://mydomain.com")
        self.client.get_token("", "useless_password")

    def test_does_not_make_get_request(self):
        self.mock_requests_session.get.assert_not_called()

    def test_does_not_make_post_request(self):
        self.mock_requests_session.post.assert_not_called()


class UseAsContextManagerTestCase(TestCase):
    @mock_session()
    def setUp(self, mock_requests_session):
        self.mock_requests_session = mock_requests_session
        with EnhydrisApiClient("https://mydomain.com/") as api_client:
            api_client.get_station(42)

    def test_called_enter(self):
        self.mock_requests_session.return_value.__enter__.assert_called_once_with()

    def test_called_exit(self):
        self.assertEqual(
            len(self.mock_requests_session.return_value.__exit__.mock_calls), 1
        )

    def test_makes_request(self):
        self.mock_requests_session.return_value.get.assert_called_once_with(
            "https://mydomain.com/api/stations/42/"
        )


class Error400TestCase(TestCase):
    msg = "hello world"

    @mock_session(
        **{
            "get.return_value.status_code": 400,
            "get.return_value.text": "hello world",
            "post.return_value.status_code": 400,
            "post.return_value.text": "hello world",
            "put.return_value.status_code": 400,
            "put.return_value.text": "hello world",
            "patch.return_value.status_code": 400,
            "patch.return_value.text": "hello world",
            "delete.return_value.status_code": 400,
            "delete.return_value.text": "hello world",
        }
    )
    def setUp(self, m):
        self.client = EnhydrisApiClient("https://mydomain.com")

    def test_get_token(self):
        with self.assertRaisesRegex(requests.HTTPError, self.msg):
            self.client.get_token("john", "topsecret")

    def test_get_station(self):
        with self.assertRaisesRegex(requests.HTTPError, self.msg):
            self.client.get_station(42)

    def test_post_station(self):
        with self.assertRaisesRegex(requests.HTTPError, self.msg):
            self.client.post_station({})

    def test_put_station(self):
        with self.assertRaisesRegex(requests.HTTPError, self.msg):
            self.client.put_station(42, {})

    def test_patch_station(self):
        with self.assertRaisesRegex(requests.HTTPError, self.msg):
            self.client.patch_station(42, {})

    def test_delete_station(self):
        with self.assertRaisesRegex(requests.HTTPError, self.msg):
            self.client.delete_station(42)

    def test_get_timeseries(self):
        with self.assertRaisesRegex(requests.HTTPError, self.msg):
            self.client.get_timeseries(41, 42, 43)

    def test_post_timeseries(self):
        with self.assertRaisesRegex(requests.HTTPError, self.msg):
            self.client.post_timeseries(42, 43, {})

    def test_delete_timeseries(self):
        with self.assertRaisesRegex(requests.HTTPError, self.msg):
            self.client.delete_timeseries(41, 42, 43)

    def test_read_tsdata(self):
        with self.assertRaisesRegex(requests.HTTPError, self.msg):
            self.client.read_tsdata(41, 42, 43)

    def test_post_tsdata(self):
        with self.assertRaisesRegex(requests.HTTPError, self.msg):
            self.client.post_tsdata(41, 42, 43, HTimeseries())

    def test_get_ts_end_date(self):
        with self.assertRaisesRegex(requests.HTTPError, self.msg):
            self.client.get_ts_end_date(41, 42, 43)


class EnhydrisApiClientTestCase(TestCase):
    @mock.patch("requests.Session")
    def test_client_with_token(self, mock_requests_session):
        EnhydrisApiClient("https://mydomain.com/", token="test-token")
        mock_requests_session.return_value.headers.update.assert_any_call(
            {"Authorization": "token test-token"}
        )
