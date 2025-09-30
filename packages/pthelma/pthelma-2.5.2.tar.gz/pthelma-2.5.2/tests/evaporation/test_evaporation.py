import datetime as dt
import math
from unittest import TestCase

import numpy as np

from evaporation import PenmanMonteith, cloud2radiation


class SenegalTzinfo(dt.tzinfo):
    """
    At various places we test using Example 19, p. 75, of Allen et al. (1998).
    The example calculates evaporation in Senegal.  Although Senegal has time
    Afrika/Dakar, which is the same as UTC, Example 19 apparently assumes that
    its time zone is actually UTC-01:00 (which would be more consistent with
    its longitude, which may be the reason for the error).  So we make the same
    assumption as example 19, in order to get the same result.
    """

    def utcoffset(self, adate):
        return -dt.timedelta(hours=1)

    def dst(self, adate):
        return dt.timedelta(0)


senegal_tzinfo = SenegalTzinfo()


class PenmanMonteithTestCase(TestCase):
    def test_daily_plain(self):
        # Apply Allen et al. (1998) Example 18 page 72.
        self._get_daily_vars()
        result = PenmanMonteith(**self.pmclassvars).calculate(**self.pmvars)
        self.assertAlmostEqual(result, 3.9, places=1)

    def test_daily_with_solar_radiation(self):
        # Same as above, but instead of sunshine duration we provide the solar radiation
        # directly. Should get the same result.
        self._get_daily_vars()
        del self.pmvars["sunshine_duration"]
        self.pmvars["solar_radiation"] = 22.07
        result = PenmanMonteith(**self.pmclassvars).calculate(**self.pmvars)
        self.assertAlmostEqual(result, 3.9, places=1)

    def test_daily_with_pressure(self):
        # Same as above, but instead of letting it calculate pressure we provide it
        # directly. Should get the same result.
        self._get_daily_vars()
        self.pmclassvars["unit_converters"]["pressure"] = lambda x: x / 10
        self.pmvars["pressure"] = 1001
        result = PenmanMonteith(**self.pmclassvars).calculate(**self.pmvars)
        self.assertAlmostEqual(result, 3.9, places=1)

    def _get_daily_vars(self):
        unit_converters = {
            # Eq. 47 p. 56
            "wind_speed": lambda x: (x * 4.87 / math.log(67.8 * 10 - 5.42))
        }
        self.pmclassvars = {
            "albedo": 0.23,
            "elevation": 100,
            "latitude": 50.8,
            "time_step": "D",
            "unit_converters": unit_converters,
        }
        self.pmvars = {
            "temperature_max": 21.5,
            "temperature_min": 12.3,
            "humidity_max": 84,
            "humidity_min": 63,
            "wind_speed": 2.78,
            "sunshine_duration": 9.25,
            "adatetime": dt.date(2014, 7, 6),
        }

    def test_daily_grid(self):
        # We use a 1x3 grid, where point (1, 1) is the same as Example 18,
        # point (1, 2) has some different values, and the elevation at point
        # (1, 3) is NaN to signify a nodata point.

        unit_converters = {
            # Eq. 47 p. 56
            "wind_speed": lambda x: x
            * 4.87
            / math.log(67.8 * 10 - 5.42)
        }

        pm = PenmanMonteith(
            albedo=0.23,
            elevation=np.array([100, 100, float("nan")]),
            latitude=50.8,
            time_step="D",
            unit_converters=unit_converters,
        )
        result = pm.calculate(
            temperature_max=np.array([21.5, 28, 28]),
            temperature_min=np.array([12.3, 15, 15]),
            humidity_max=np.array([84, 70, 70]),
            humidity_min=np.array([63, 60, 60]),
            wind_speed=np.array([2.78, 3, 3]),
            sunshine_duration=np.array([9.25, 9, 9]),
            adatetime=dt.date(2014, 7, 6),
        )
        np.testing.assert_allclose(result, np.array([3.9, 4.8, float("nan")]), atol=0.1)

        # Same thing with solar radiation instead of sunshine duration
        result = pm.calculate(
            temperature_max=np.array([21.5, 28, 28]),
            temperature_min=np.array([12.3, 15, 15]),
            humidity_max=np.array([84, 70, 70]),
            humidity_min=np.array([63, 60, 60]),
            wind_speed=np.array([2.78, 3, 3]),
            solar_radiation=np.array([22.07, 21.62, 21.62]),
            adatetime=dt.date(2014, 7, 6),
        )
        np.testing.assert_allclose(result, np.array([3.9, 4.8, float("nan")]), atol=0.1)

    def test_hourly(self):
        # Apply Allen et al. (1998) Example 19 page 75.
        pm = PenmanMonteith(
            albedo=0.23,
            nighttime_solar_radiation_ratio=0.8,
            elevation=8,
            latitude=16.217,
            longitude=-16.25,
            time_step="h",
        )

        result = pm.calculate(
            temperature=38,
            humidity=52,
            wind_speed=3.3,
            pressure=101.3,
            solar_radiation=2.450,
            adatetime=dt.datetime(2014, 10, 1, 15, 0, tzinfo=senegal_tzinfo),
        )
        self.assertAlmostEqual(result, 0.63, places=2)
        result = pm.calculate(
            temperature=28,
            humidity=90,
            wind_speed=1.9,
            pressure=101.3,
            solar_radiation=0,
            adatetime=dt.datetime(2014, 10, 1, 2, 30, tzinfo=senegal_tzinfo),
        )
        self.assertAlmostEqual(result, 0.0, places=2)

        # Same thing, but let it calculate pressure itself
        result = pm.calculate(
            temperature=38,
            humidity=52,
            wind_speed=3.3,
            solar_radiation=2.450,
            adatetime=dt.datetime(2014, 10, 1, 15, 0, tzinfo=senegal_tzinfo),
        )
        self.assertAlmostEqual(result, 0.63, places=2)
        result = pm.calculate(
            temperature=28,
            humidity=90,
            wind_speed=1.9,
            solar_radiation=0,
            adatetime=dt.datetime(2014, 10, 1, 2, 30, tzinfo=senegal_tzinfo),
        )
        self.assertAlmostEqual(result, 0.0, places=2)

    def test_hourly_grid(self):
        # We use a 2x1 grid, where point 1, 1 is the same as Example 19, and
        # point 1, 2 has some different values.
        pm = PenmanMonteith(
            albedo=0.23,
            nighttime_solar_radiation_ratio=0.8,
            elevation=8,
            latitude=16.217,
            longitude=np.array([-16.25, -15.25]),
            time_step="h",
        )
        result = pm.calculate(
            temperature=np.array([38, 28]),
            humidity=np.array([52, 42]),
            wind_speed=np.array([3.3, 2.3]),
            pressure=101.3,
            solar_radiation=np.array([2.450, 1.450]),
            adatetime=dt.datetime(2014, 10, 1, 15, 0, tzinfo=senegal_tzinfo),
        )
        np.testing.assert_almost_equal(result, np.array([0.63, 0.36]), decimal=2)

    def test_hourly_with_albedo_grid(self):
        # Apply Allen et al. (1998) Example 19 page 75.
        pm = PenmanMonteith(
            albedo=np.array([0.23]),
            nighttime_solar_radiation_ratio=0.8,
            elevation=8,
            latitude=16.217,
            longitude=-16.25,
            time_step="h",
        )

        result = pm.calculate(
            temperature=38,
            humidity=52,
            wind_speed=3.3,
            pressure=101.3,
            solar_radiation=2.450,
            adatetime=dt.datetime(2014, 10, 1, 15, 0, tzinfo=senegal_tzinfo),
        )
        # The following two lines could be written more simply like this:
        #     self.assertAlmostEqual(result, 0.63, places=2)
        # However, it does not work properly on Python 3 because of a numpy
        # issue.
        self.assertEqual(result.size, 1)
        self.assertAlmostEqual(result[0], 0.63, places=2)

    def test_hourly_array_with_seasonal_albedo_grid(self):
        # We use a 2x1 grid, where point 1, 1 is the same as Example 19, and
        # point 1, 2 has some different values.
        pm = PenmanMonteith(
            albedo=[np.array([0.23, 0.23]) for item in range(1, 13)],
            nighttime_solar_radiation_ratio=0.8,
            elevation=8,
            latitude=16.217,
            longitude=np.array([-16.25, -15.25]),
            time_step="h",
        )
        result = pm.calculate(
            temperature=np.array([38, 28]),
            humidity=np.array([52, 42]),
            wind_speed=np.array([3.3, 2.3]),
            pressure=101.3,
            solar_radiation=np.array([2.450, 1.450]),
            adatetime=dt.datetime(2014, 10, 1, 15, 0, tzinfo=senegal_tzinfo),
        )
        np.testing.assert_almost_equal(result, np.array([0.63, 0.36]), decimal=2)

    def test_hourly_with_seasonal_albedo(self):
        # Apply Allen et al. (1998) Example 19 page 75.

        pm = PenmanMonteith(
            albedo=[
                0.13,
                0.01,
                0.01,
                0.01,
                0.01,
                0.01,
                0.01,
                0.01,
                0.01,
                0.23,
                0.01,
                0.33,
            ],
            nighttime_solar_radiation_ratio=0.8,
            elevation=8,
            latitude=16.217,
            longitude=-16.25,
            time_step="h",
        )

        result = pm.calculate(
            temperature=38,
            humidity=52,
            wind_speed=3.3,
            pressure=101.3,
            solar_radiation=2.450,
            adatetime=dt.datetime(2014, 1, 1, 15, 0, tzinfo=senegal_tzinfo),
        )
        self.assertAlmostEqual(result, 0.69, places=2)

        result = pm.calculate(
            temperature=38,
            humidity=52,
            wind_speed=3.3,
            pressure=101.3,
            solar_radiation=2.450,
            adatetime=dt.datetime(2014, 12, 1, 15, 0, tzinfo=senegal_tzinfo),
        )
        self.assertAlmostEqual(result, 0.56, places=2)

        result = pm.calculate(
            temperature=38,
            humidity=52,
            wind_speed=3.3,
            pressure=101.3,
            solar_radiation=2.450,
            adatetime=dt.datetime(2014, 10, 1, 15, 0, tzinfo=senegal_tzinfo),
        )
        self.assertAlmostEqual(result, 0.63, places=2)


class Cloud2RadiationTestCase(TestCase):
    def test_daily(self):
        # We test using the example at the bottom of FAO56 p. 50, except that we
        # replace n/N with (1 - cloud_cover).
        cloud_cover = 1 - 7.1 / 10.9
        latitude = -(22 + 54 / 60)
        longitude = 0  # Irrelevant
        date = dt.date(2025, 5, 15)
        result = cloud2radiation(cloud_cover, latitude, longitude, date)
        expected_result = 14.5 * 1e6 / 86400
        self.assertTrue(abs(result - expected_result) < 1)
