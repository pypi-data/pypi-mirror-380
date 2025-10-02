from copy import copy
from io import StringIO
from urllib.parse import urljoin
from zoneinfo import ZoneInfo

import iso8601
import requests

from htimeseries import HTimeseries


class MalformedResponseError(Exception):
    pass


class EnhydrisApiClient:
    def __init__(self, base_url, token=None):
        self.base_url = base_url
        self.token = token
        self.session = requests.Session()
        if token is not None:
            self.session.headers.update({"Authorization": f"token {self.token}"})

        # My understanding from requests' documentation is that when I make a post
        # request, it shouldn't be necessary to specify Content-Type:
        # application/x-www-form-urlencoded, and that requests adds the header
        # automatically. However, when running in Python 3, apparently requests does not
        # add the header (although it does convert the post data to
        # x-www-form-urlencoded format). This is why I'm specifying it explicitly.
        self.session.headers.update(
            {"Content-Type": "application/x-www-form-urlencoded"}
        )

    def __enter__(self):
        self.session.__enter__()
        return self

    def __exit__(self, *args):
        self.session.__exit__(*args)

    def check_response(self, expected_status_code=None):
        try:
            self._raise_HTTPError_on_error(expected_status_code=expected_status_code)
        except requests.HTTPError as e:
            if self.response.text:
                raise requests.HTTPError(
                    f"{str(e)}. Server response: {self.response.text}"
                )

    def _raise_HTTPError_on_error(self, expected_status_code):
        self._check_status_code_is_nonerror()
        self._check_status_code_is_the_one_expected(expected_status_code)

    def _check_status_code_is_nonerror(self):
        self.response.raise_for_status()

    def _check_status_code_is_the_one_expected(self, expected_status_code):
        if expected_status_code and self.response.status_code != expected_status_code:
            raise requests.HTTPError(
                f"Expected status code {expected_status_code}; "
                f"got {self.response.status_code} instead"
            )

    def get_token(self, username, password):
        if not username:
            return

        # Get a csrftoken
        login_url = urljoin(self.base_url, "api/auth/login/")
        data = f"username={username}&password={password}"
        self.response = self.session.post(login_url, data=data, allow_redirects=False)
        self.check_response()
        key = self.response.json()["key"]
        self.session.headers.update({"Authorization": f"token {key}"})
        return key

    def list_stations(self):
        url = urljoin(self.base_url, "api/stations/")
        while url:
            try:
                self.response = self.session.get(url)
                self.check_response()
                data = self.response.json()
                for station in data["results"]:
                    yield station
                url = data["next"]
            except (KeyError, TypeError) as e:
                raise MalformedResponseError(
                    f"Malformed response from server: {str(e)}"
                )

    def get_station(self, station_id):
        url = urljoin(self.base_url, f"api/stations/{station_id}/")
        self.response = self.session.get(url)
        self.check_response()
        return self.response.json()

    def post_station(self, data):
        self.response = self.session.post(
            urljoin(self.base_url, "api/stations/"), data=data
        )
        self.check_response()
        return self.response.json()["id"]

    def put_station(self, station_id, data):
        self.response = self.session.put(
            urljoin(self.base_url, f"api/stations/{station_id}/"), data=data
        )
        self.check_response()

    def patch_station(self, station_id, data):
        self.response = self.session.patch(
            urljoin(self.base_url, f"api/stations/{station_id}/"), data=data
        )
        self.check_response()

    def delete_station(self, station_id):
        url = urljoin(self.base_url, f"api/stations/{station_id}/")
        self.response = self.session.delete(url)
        self.check_response(expected_status_code=204)

    def list_timeseries_groups(self, station_id):
        url = urljoin(self.base_url, f"api/stations/{station_id}/timeseriesgroups/")
        while url:
            try:
                self.response = self.session.get(url)
                self.check_response()
                data = self.response.json()
                for tg in data["results"]:
                    yield tg
                url = data["next"]
            except (KeyError, TypeError) as e:
                raise MalformedResponseError(
                    f"Malformed response from server: {str(e)}"
                )

    def get_timeseries_group(self, station_id, timeseries_group_id):
        url = urljoin(
            self.base_url,
            f"api/stations/{station_id}/timeseriesgroups/{timeseries_group_id}/",
        )
        self.response = self.session.get(url)
        self.check_response()
        return self.response.json()

    def post_timeseries_group(self, station_id, data):
        url = urljoin(self.base_url, f"api/stations/{station_id}/timeseriesgroups/")
        self.response = self.session.post(url, data=data)
        self.check_response()
        return self.response.json()["id"]

    def put_timeseries_group(self, station_id, timeseries_group_id, data):
        url = urljoin(
            self.base_url,
            f"api/stations/{station_id}/timeseriesgroups/{timeseries_group_id}/",
        )
        self.response = self.session.put(url, data=data)
        self.check_response()
        return self.response.json()["id"]

    def patch_timeseries_group(self, station_id, timeseries_group_id, data):
        url = urljoin(
            self.base_url,
            f"api/stations/{station_id}/timeseriesgroups/{timeseries_group_id}/",
        )
        self.response = self.session.patch(url, data=data)
        self.check_response()

    def delete_timeseries_group(self, station_id, timeseries_group_id):
        url = urljoin(
            self.base_url,
            f"api/stations/{station_id}/timeseriesgroups/{timeseries_group_id}/",
        )
        self.response = self.session.delete(url)
        self.check_response(expected_status_code=204)

    def list_timeseries(self, station_id, timeseries_group_id):
        url = urljoin(
            self.base_url,
            f"api/stations/{station_id}/timeseriesgroups/{timeseries_group_id}/"
            "timeseries/",
        )
        self.response = self.session.get(url)
        self.check_response()
        return self.response.json()["results"]

    def get_timeseries(self, station_id, timeseries_group_id, timeseries_id):
        url = urljoin(
            self.base_url,
            f"api/stations/{station_id}/timeseriesgroups/{timeseries_group_id}/"
            f"timeseries/{timeseries_id}/",
        )
        self.response = self.session.get(url)
        self.check_response()
        return self.response.json()

    def post_timeseries(self, station_id, timeseries_group_id, data):
        self.response = self.session.post(
            urljoin(
                self.base_url,
                f"api/stations/{station_id}/timeseriesgroups/{timeseries_group_id}/"
                "timeseries/",
            ),
            data=data,
        )
        self.check_response()
        return self.response.json()["id"]

    def delete_timeseries(self, station_id, timeseries_group_id, timeseries_id):
        url = urljoin(
            self.base_url,
            f"api/stations/{station_id}/timeseriesgroups/{timeseries_group_id}/"
            f"timeseries/{timeseries_id}/",
        )
        self.response = self.session.delete(url)
        self.check_response(expected_status_code=204)

    def read_tsdata(
        self,
        station_id,
        timeseries_group_id,
        timeseries_id,
        start_date=None,
        end_date=None,
        timezone=None,
    ):
        url = urljoin(
            self.base_url,
            f"api/stations/{station_id}/timeseriesgroups/{timeseries_group_id}/"
            f"timeseries/{timeseries_id}/data/",
        )
        params = {"fmt": "hts"}
        tzinfo = ZoneInfo(timezone) if timezone else None
        dates_are_aware = (start_date is None or start_date.tzinfo is not None) and (
            end_date is None or end_date.tzinfo is not None
        )
        if not dates_are_aware:
            raise ValueError("start_date and end_date must be aware")
        params["start_date"] = start_date and start_date.isoformat()
        params["end_date"] = end_date and end_date.isoformat()
        params["timezone"] = timezone
        self.response = self.session.get(url, params=params)
        self.check_response()
        if self.response.text:
            return HTimeseries(StringIO(self.response.text), default_tzinfo=tzinfo)
        else:
            return HTimeseries()

    def post_tsdata(self, station_id, timeseries_group_id, timeseries_id, ts):
        f = StringIO()
        data = copy(ts.data)
        try:
            data.index = data.index.tz_convert("UTC")
        except AttributeError:
            assert data.empty
        data.to_csv(f, header=False)
        url = urljoin(
            self.base_url,
            f"api/stations/{station_id}/timeseriesgroups/{timeseries_group_id}/"
            f"timeseries/{timeseries_id}/data/",
        )
        self.response = self.session.post(
            url, data={"timeseries_records": f.getvalue(), "timezone": "UTC"}
        )
        self.check_response()
        return self.response.text

    def get_ts_end_date(
        self, station_id, timeseries_group_id, timeseries_id, timezone=None
    ):
        url = urljoin(
            self.base_url,
            f"api/stations/{station_id}/timeseriesgroups/{timeseries_group_id}/"
            f"timeseries/{timeseries_id}/bottom/",
        )
        self.response = self.session.get(url, params={"timezone": timezone})
        self.check_response()
        try:
            datestring = self.response.text.strip().split(",")[0]
            return iso8601.parse_date(datestring, default_timezone=None)
        except (IndexError, iso8601.ParseError):
            return None
