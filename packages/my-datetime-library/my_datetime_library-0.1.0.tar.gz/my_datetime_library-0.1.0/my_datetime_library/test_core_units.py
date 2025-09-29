import unittest
import os
from .timepoint import TimePoint, TimeScale, NANOSECONDS_PER_SECOND, SECONDS_PER_MINUTE, SECONDS_PER_HOUR, SECONDS_PER_DAY
from .duration import Duration
from .calendar_utils import is_leap_year, days_in_month, days_since_epoch, get_date_from_days_since_epoch
from .leap_seconds import LeapSecondTable, SECONDS_0001_TO_1900, SECONDS_0001_TO_1970

class TestCalendarUtils(unittest.TestCase):
    def test_is_leap_year(self):
        self.assertTrue(is_leap_year(2000))
        self.assertFalse(is_leap_year(2001))
        self.assertFalse(is_leap_year(1900))
        self.assertTrue(is_leap_year(2004))

    def test_days_in_month(self):
        self.assertEqual(days_in_month(2000, 2), 29) # Leap year
        self.assertEqual(days_in_month(2001, 2), 28) # Non-leap year
        self.assertEqual(days_in_month(2023, 1), 31)
        self.assertEqual(days_in_month(2023, 4), 30)
        with self.assertRaises(ValueError):
            days_in_month(2023, 0)
        with self.assertRaises(ValueError):
            days_in_month(2023, 13)

    def test_days_since_epoch(self):
        # Epoch is Jan 1, Year 1
        self.assertEqual(days_since_epoch(1, 1, 1), 0)
        self.assertEqual(days_since_epoch(1, 1, 2), 1)
        self.assertEqual(days_since_epoch(1, 2, 1), 31)
        self.assertEqual(days_since_epoch(2, 1, 1), 365)
        self.assertEqual(days_since_epoch(2000, 3, 1), 730179)

    def test_get_date_from_days_since_epoch(self):
        self.assertEqual(get_date_from_days_since_epoch(0), (1, 1, 1))
        self.assertEqual(get_date_from_days_since_epoch(1), (1, 1, 2))
        self.assertEqual(get_date_from_days_since_epoch(31), (1, 2, 1))
        self.assertEqual(get_date_from_days_since_epoch(365), (2, 1, 1))
        self.assertEqual(get_date_from_days_since_epoch(730179), (2000, 3, 1))

class TestDuration(unittest.TestCase):
    def test_init(self):
        d = Duration(1000)
        self.assertEqual(d.nanoseconds, 1000)
        with self.assertRaises(TypeError):
            Duration(1000.5)

    def test_from_methods(self):
        self.assertEqual(Duration.from_seconds(1).nanoseconds, NANOSECONDS_PER_SECOND)
        self.assertEqual(Duration.from_minutes(1).nanoseconds, 60 * NANOSECONDS_PER_SECOND)
        self.assertEqual(Duration.from_hours(1).nanoseconds, 3600 * NANOSECONDS_PER_SECOND)
        self.assertEqual(Duration.from_days(1).nanoseconds, SECONDS_PER_DAY * NANOSECONDS_PER_SECOND)
        self.assertEqual(Duration.from_seconds(0.5).nanoseconds, NANOSECONDS_PER_SECOND // 2)

    def test_to_methods(self):
        d = Duration(NANOSECONDS_PER_SECOND * 3600)
        self.assertEqual(d.to_seconds(), 3600)
        self.assertEqual(d.to_minutes(), 60)
        self.assertEqual(d.to_hours(), 1)

    def test_arithmetic(self):
        d1 = Duration.from_seconds(10)
        d2 = Duration.from_seconds(5)
        self.assertEqual((d1 + d2).to_seconds(), 15)
        self.assertEqual((d1 - d2).to_seconds(), 5)
        self.assertEqual((d2 - d1).to_seconds(), -5)

    def test_comparison(self):
        d1 = Duration.from_seconds(10)
        d2 = Duration.from_seconds(5)
        d3 = Duration.from_seconds(10)
        self.assertTrue(d1 > d2)
        self.assertTrue(d2 < d1)
        self.assertTrue(d1 == d3)
        self.assertTrue(d1 >= d2)
        self.assertTrue(d1 <= d3)

        self.assertFalse(d1 < d2)
        self.assertFalse(d2 > d1)
        self.assertFalse(d1 != d3)
        self.assertFalse(d1 < d3)
        self.assertFalse(d1 > d3)

class TestTimePoint(unittest.TestCase):
    def test_init(self):
        tp = TimePoint(0, TimeScale.TAI)
        self.assertEqual(tp.nanoseconds_since_epoch, 0)
        self.assertEqual(tp.time_scale, TimeScale.TAI)
        with self.assertRaises(TypeError):
            TimePoint(0.5, TimeScale.TAI)
        with self.assertRaises(TypeError):
            TimePoint(0, "TAI")

    def test_from_components_to_components(self):
        # Test epoch
        tp = TimePoint.from_components(1, 1, 1)
        self.assertEqual(tp.nanoseconds_since_epoch, 0)
        self.assertEqual(tp.to_components(), (1, 1, 1, 0, 0, 0, 0))

        # Test a simple date
        tp = TimePoint.from_components(1, 1, 2, 1, 2, 3, 4)
        expected_nanoseconds = (1 * SECONDS_PER_DAY + 1 * SECONDS_PER_HOUR + 2 * SECONDS_PER_MINUTE + 3) * NANOSECONDS_PER_SECOND + 4
        self.assertEqual(tp.nanoseconds_since_epoch, expected_nanoseconds)
        self.assertEqual(tp.to_components(), (1, 1, 2, 1, 2, 3, 4))

        # Test a date in a leap year
        tp_leap = TimePoint.from_components(2000, 3, 1, 12, 30, 45, 123456789)
        year, month, day, hour, minute, second, nanosecond = tp_leap.to_components()
        self.assertEqual((year, month, day, hour, minute, second, nanosecond), (2000, 3, 1, 12, 30, 45, 123456789))

        # Test a date in a non-leap year
        tp_non_leap = TimePoint.from_components(2001, 3, 1, 12, 30, 45, 123456789)
        year, month, day, hour, minute, second, nanosecond = tp_non_leap.to_components()
        self.assertEqual((year, month, day, hour, minute, second, nanosecond), (2001, 3, 1, 12, 30, 45, 123456789))

        # Test invalid components
        with self.assertRaises(ValueError):
            TimePoint.from_components(2023, 2, 30) # Feb 30
        with self.assertRaises(ValueError):
            TimePoint.from_components(2023, 1, 1, hour=24)

    def test_add_subtract_duration(self):
        tp = TimePoint.from_components(2023, 1, 1, 10, 0, 0)
        duration = Duration.from_hours(2)
        new_tp = tp + duration
        self.assertEqual(new_tp.to_components(), (2023, 1, 1, 12, 0, 0, 0))

        new_tp = tp - duration
        self.assertEqual(new_tp.to_components(), (2023, 1, 1, 8, 0, 0, 0))

    def test_difference(self):
        tp1 = TimePoint.from_components(2023, 1, 1, 10, 0, 0)
        tp2 = TimePoint.from_components(2023, 1, 1, 12, 0, 0)
        diff = tp2 - tp1
        self.assertEqual(diff.to_hours(), 2)

        tp3 = TimePoint.from_components(2023, 1, 2, 10, 0, 0)
        diff2 = tp3 - tp1
        self.assertEqual(diff2.to_days(), 1)

    def test_comparison(self):
        tp1 = TimePoint.from_components(2023, 1, 1, 10, 0, 0)
        tp2 = TimePoint.from_components(2023, 1, 1, 12, 0, 0)
        tp3 = TimePoint.from_components(2023, 1, 1, 10, 0, 0)

        self.assertTrue(tp2 > tp1)
        self.assertTrue(tp1 < tp2)
        self.assertTrue(tp1 == tp3)
        self.assertTrue(tp1 >= tp3)
        self.assertTrue(tp2 >= tp1)
        self.assertTrue(tp1 <= tp3)
        self.assertTrue(tp1 <= tp2)

        self.assertFalse(tp1 < tp2 and tp1 == tp2)

        tp_utc = TimePoint(0, TimeScale.UTC)
        with self.assertRaises(ValueError):
            tp1 > tp_utc

class TestLeapSecondTable(unittest.TestCase):
    def setUp(self):
        self.leap_second_table = LeapSecondTable()
        # Assuming leap-seconds.list is in the current directory after extraction
        self.leap_second_file = "leap-seconds.list"
        if not os.path.exists(self.leap_second_file):
            self.fail(f"Leap second data file not found: {self.leap_second_file}")
        self.leap_second_table.load_from_file(self.leap_second_file)

    def test_load_from_file(self):
        self.assertGreater(len(self.leap_second_table.leap_seconds_data), 0)
        # Check a known entry, e.g., the first one: 2272060800      10      # 1 Jan 1972
        self.assertEqual(self.leap_second_table.leap_seconds_data[0], (2272060800, 10))
        # Check the last known entry (as of tzdata2025b): 3692217600      37      # 1 Jan 2017
        self.assertEqual(self.leap_second_table.leap_seconds_data[-1], (3692217600, 37))

    def test_get_tai_utc_offset(self):
        # Test before any leap seconds (before 1972-01-01)
        tp_utc_before_ls = TimePoint.from_components(1971, 12, 31, 23, 59, 59, time_scale=TimeScale.UTC)
        self.assertEqual(self.leap_second_table.get_tai_utc_offset(tp_utc_before_ls), 0) # No leap seconds yet

        # Test at the first leap second (1972-01-01)
        tp_utc_1972_jan_1 = TimePoint.from_components(1972, 1, 1, 0, 0, 0, time_scale=TimeScale.UTC)
        self.assertEqual(self.leap_second_table.get_tai_utc_offset(tp_utc_1972_jan_1), 10) # 10 seconds offset

        # Test between two leap seconds (e.g., between 1972-01-01 and 1972-07-01)
        tp_utc_1972_apr_1 = TimePoint.from_components(1972, 4, 1, 0, 0, 0, time_scale=TimeScale.UTC)
        self.assertEqual(self.leap_second_table.get_tai_utc_offset(tp_utc_1972_apr_1), 10)

        # Test at the second leap second (1972-07-01)
        tp_utc_1972_jul_1 = TimePoint.from_components(1972, 7, 1, 0, 0, 0, time_scale=TimeScale.UTC)
        self.assertEqual(self.leap_second_table.get_tai_utc_offset(tp_utc_1972_jul_1), 11) # 11 seconds offset

        # Test a recent date (after last known leap second 2017-01-01)
        tp_utc_recent = TimePoint.from_components(2023, 1, 1, 0, 0, 0, time_scale=TimeScale.UTC)
        self.assertEqual(self.leap_second_table.get_tai_utc_offset(tp_utc_recent), 37) # 37 seconds offset

        # Test with a TAI TimePoint (should raise ValueError)
        tp_tai = TimePoint.from_components(2023, 1, 1, time_scale=TimeScale.TAI)
        with self.assertRaises(ValueError):
            self.leap_second_table.get_tai_utc_offset(tp_tai)

class TestTimePointConversion(unittest.TestCase):
    def setUp(self):
        self.leap_second_table = LeapSecondTable()
        self.leap_second_file = "leap-seconds.list"
        if not os.path.exists(self.leap_second_file):
            self.fail(f"Leap second data file not found: {self.leap_second_file}")
        self.leap_second_table.load_from_file(self.leap_second_file)

    def test_tai_to_utc_conversion(self):
        # TAI = UTC + offset
        # UTC = TAI - offset

        # Example: 1972-01-01 00:00:00 UTC, offset is 10 seconds
        # So, 1972-01-01 00:00:00 UTC is equivalent to 1972-01-01 00:00:10 TAI
        
        # Create a TAI TimePoint
        tai_tp = TimePoint.from_components(1972, 1, 1, 0, 0, 10, time_scale=TimeScale.TAI)
        utc_tp = tai_tp.to_utc(self.leap_second_table)
        self.assertEqual(utc_tp.time_scale, TimeScale.UTC)
        self.assertEqual(utc_tp.to_components(), (1972, 1, 1, 0, 0, 0, 0))

        # Another example: 2017-01-01 00:00:00 UTC, offset is 37 seconds
        # So, 2017-01-01 00:00:00 UTC is equivalent to 2017-01-01 00:00:37 TAI
        tai_tp_recent = TimePoint.from_components(2017, 1, 1, 0, 0, 37, time_scale=TimeScale.TAI)
        utc_tp_recent = tai_tp_recent.to_utc(self.leap_second_table)
        self.assertEqual(utc_tp_recent.time_scale, TimeScale.UTC)
        self.assertEqual(utc_tp_recent.to_components(), (2017, 1, 1, 0, 0, 0, 0))

        # Test a TimePoint before any leap seconds
        tai_tp_early = TimePoint.from_components(1970, 1, 1, 0, 0, 0, time_scale=TimeScale.TAI)
        utc_tp_early = tai_tp_early.to_utc(self.leap_second_table)
        self.assertEqual(utc_tp_early.time_scale, TimeScale.UTC)
        self.assertEqual(utc_tp_early.to_components(), (1970, 1, 1, 0, 0, 0, 0))

    def test_utc_to_tai_conversion(self):
        # TAI = UTC + offset

        # Example: 1972-01-01 00:00:00 UTC, offset is 10 seconds
        utc_tp = TimePoint.from_components(1972, 1, 1, 0, 0, 0, time_scale=TimeScale.UTC)
        tai_tp = utc_tp.to_tai(self.leap_second_table)
        self.assertEqual(tai_tp.time_scale, TimeScale.TAI)
        self.assertEqual(tai_tp.to_components(), (1972, 1, 1, 0, 0, 10, 0))

        # Another example: 2017-01-01 00:00:00 UTC, offset is 37 seconds
        utc_tp_recent = TimePoint.from_components(2017, 1, 1, 0, 0, 0, time_scale=TimeScale.UTC)
        tai_tp_recent = utc_tp_recent.to_tai(self.leap_second_table)
        self.assertEqual(tai_tp_recent.time_scale, TimeScale.TAI)
        self.assertEqual(tai_tp_recent.to_components(), (2017, 1, 1, 0, 0, 37, 0))

        # Test a TimePoint before any leap seconds
        utc_tp_early = TimePoint.from_components(1970, 1, 1, 0, 0, 0, time_scale=TimeScale.UTC)
        tai_tp_early = utc_tp_early.to_tai(self.leap_second_table)
        self.assertEqual(tai_tp_early.time_scale, TimeScale.TAI)
        self.assertEqual(tai_tp_early.to_components(), (1970, 1, 1, 0, 0, 0, 0))

if __name__ == '__main__':
    unittest.main()

