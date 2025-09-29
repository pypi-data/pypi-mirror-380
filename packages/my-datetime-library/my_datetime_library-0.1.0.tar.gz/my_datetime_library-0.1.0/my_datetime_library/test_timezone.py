import unittest
import os
from .timepoint import TimePoint, TimeScale
from .timezone import TimeZone, TimeZoneDatabase
from .constants import NANOSECONDS_PER_SECOND, SECONDS_PER_HOUR

class TestTimeZone(unittest.TestCase):
    def setUp(self):
        self.tzdb = TimeZoneDatabase()
        # Assuming tzdata files are in the parent directory
        self.tzdb.load_from_tzdata_files(".") 

    def test_get_timezone(self):
        ny_zone = self.tzdb.get_timezone("America/New_York")
        self.assertIsNotNone(ny_zone)
        self.assertEqual(ny_zone.name, "America/New_York")

        london_zone = self.tzdb.get_timezone("Europe/London")
        self.assertIsNotNone(london_zone)
        self.assertEqual(london_zone.name, "Europe/London")

        non_existent_zone = self.tzdb.get_timezone("NonExistent/Zone")
        self.assertIsNone(non_existent_zone)

    def test_get_total_offset_and_abbr(self):
        ny_zone = self.tzdb.get_timezone("America/New_York")
        london_zone = self.tzdb.get_timezone("Europe/London")

        # Test New York (fixed -5 hours offset in our simplified rules)
        utc_tp_ny = TimePoint.from_components(2023, 1, 1, 12, 0, 0, time_scale=TimeScale.UTC)
        offset_ny, abbr_ny = ny_zone.get_total_offset_and_abbr(utc_tp_ny)
        self.assertEqual(offset_ny, -5 * SECONDS_PER_HOUR)
        self.assertEqual(abbr_ny, "EST")

        # Test London (fixed 0 hours offset in our simplified rules)
        utc_tp_london = TimePoint.from_components(2023, 1, 1, 12, 0, 0, time_scale=TimeScale.UTC)
        offset_london, abbr_london = london_zone.get_total_offset_and_abbr(utc_tp_london)
        self.assertEqual(offset_london, 0)
        self.assertEqual(abbr_london, "GMT")

        # Test a generic zone (fixed 0 hours offset in our simplified rules)
        generic_zone = self.tzdb.get_timezone("Asia/Tokyo")
        utc_tp_generic = TimePoint.from_components(2023, 1, 1, 12, 0, 0, time_scale=TimeScale.UTC)
        offset_generic, abbr_generic = generic_zone.get_total_offset_and_abbr(utc_tp_generic)
        self.assertEqual(offset_generic, 0)
        self.assertEqual(abbr_generic, "UTC")

        # Test with TAI TimePoint (should raise ValueError)
        tai_tp = TimePoint.from_components(2023, 1, 1, time_scale=TimeScale.TAI)
        with self.assertRaises(ValueError):
            ny_zone.get_total_offset_and_abbr(tai_tp)

    def test_localize_unlocalize(self):
        ny_zone = self.tzdb.get_timezone("America/New_York")
        self.assertIsNotNone(ny_zone)

        # UTC TimePoint: 2023-01-01 12:00:00 UTC
        utc_tp = TimePoint.from_components(2023, 1, 1, 12, 0, 0, time_scale=TimeScale.UTC)
        
        # Localize to New York (UTC-5)
        local_tp_ny = ny_zone.localize(utc_tp)
        # Expected local time: 2023-01-01 07:00:00 (12 - 5)
        self.assertEqual(local_tp_ny.to_components(), (2023, 1, 1, 7, 0, 0, 0))
        self.assertEqual(local_tp_ny.time_scale, TimeScale.UTC) # Internal scale remains UTC

        # Unlocalize back to UTC
        unlocalized_tp = ny_zone.unlocalize(local_tp_ny)
        # Expected UTC time: 2023-01-01 12:00:00
        self.assertEqual(unlocalized_tp.to_components(), (2023, 1, 1, 12, 0, 0, 0))
        self.assertEqual(unlocalized_tp.time_scale, TimeScale.UTC)

        # Test with a TAI TimePoint for localize (should raise ValueError)
        tai_tp = TimePoint.from_components(2023, 1, 1, time_scale=TimeScale.TAI)
        with self.assertRaises(ValueError):
            ny_zone.localize(tai_tp)

if __name__ == '__main__':
    unittest.main()

