from __future__ import annotations
from enum import Enum
from .duration import Duration
from .calendar_utils import is_leap_year, days_in_month, days_since_epoch, get_date_from_days_since_epoch
from .constants import NANOSECONDS_PER_SECOND, SECONDS_PER_MINUTE, MINUTES_PER_HOUR, HOURS_PER_DAY, SECONDS_PER_HOUR, SECONDS_PER_DAY

# Constants for converting between our internal epoch (0001-01-01 00:00:00) and other epochs.
# These are based on a continuous Gregorian calendar.

# Days from 0001-01-01 to 1900-01-01 (exclusive of 1900-01-01)
DAYS_0001_TO_1900 = days_since_epoch(1900, 1, 1) - days_since_epoch(1, 1, 1)
SECONDS_0001_TO_1900 = DAYS_0001_TO_1900 * SECONDS_PER_DAY

# Days from 0001-01-01 to 1970-01-01 (exclusive of 1970-01-01)
DAYS_0001_TO_1970 = days_since_epoch(1970, 1, 1) - days_since_epoch(1, 1, 1)
SECONDS_0001_TO_1970 = DAYS_0001_TO_1970 * SECONDS_PER_DAY

class TimeScale(Enum):
    TAI = "TAI"
    UTC = "UTC"

class TimePoint:
    # Our internal epoch is 0001-01-01 00:00:00 (conceptually TAI for internal calculations)
    EPOCH_YEAR = 1

    def __init__(self, nanoseconds_since_epoch: int, time_scale: TimeScale):
        if not isinstance(nanoseconds_since_epoch, int):
            raise TypeError("nanoseconds_since_epoch must be an integer")
        if not isinstance(time_scale, TimeScale):
            raise TypeError("time_scale must be an instance of TimeScale enum")

        self.nanoseconds_since_epoch = nanoseconds_since_epoch
        self.time_scale = time_scale

    def __repr__(self):
        return f"TimePoint(nanoseconds_since_epoch={self.nanoseconds_since_epoch}, time_scale={self.time_scale.value})"

    def __eq__(self, other):
        if not isinstance(other, TimePoint):
            return NotImplemented
        # For equality, we assume both TimePoints are in the same time scale for now.
        # Conversion between scales will be handled by specific methods.
        return self.nanoseconds_since_epoch == other.nanoseconds_since_epoch and \
               self.time_scale == other.time_scale

    def __lt__(self, other):
        if not isinstance(other, TimePoint):
            return NotImplemented
        if self.time_scale != other.time_scale:
            raise ValueError("Cannot compare TimePoints of different time scales directly. Convert them first.")
        return self.nanoseconds_since_epoch < other.nanoseconds_since_epoch

    def __le__(self, other):
        if not isinstance(other, TimePoint):
            return NotImplemented
        if self.time_scale != other.time_scale:
            raise ValueError("Cannot compare TimePoints of different time scales directly. Convert them first.")
        return self.nanoseconds_since_epoch <= other.nanoseconds_since_epoch

    def __gt__(self, other):
        if not isinstance(other, TimePoint):
            return NotImplemented
        if self.time_scale != other.time_scale:
            raise ValueError("Cannot compare TimePoints of different time scales directly. Convert them first.")
        return self.nanoseconds_since_epoch > other.nanoseconds_since_epoch

    def __ge__(self, other):
        if not isinstance(other, TimePoint):
            return NotImplemented
        if self.time_scale != other.time_scale:
            raise ValueError("Cannot compare TimePoints of different time scales directly. Convert them first.")
        return self.nanoseconds_since_epoch >= other.nanoseconds_since_epoch

    def __add__(self, other):
        if isinstance(other, Duration):
            return TimePoint(self.nanoseconds_since_epoch + other.nanoseconds, self.time_scale)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Duration):
            return TimePoint(self.nanoseconds_since_epoch - other.nanoseconds, self.time_scale)
        elif isinstance(other, TimePoint):
            if self.time_scale != other.time_scale:
                raise ValueError("Cannot subtract TimePoints of different time scales directly. Convert them first.")
            return Duration(self.nanoseconds_since_epoch - other.nanoseconds_since_epoch)
        return NotImplemented

    @classmethod
    def from_components(cls, year: int, month: int, day: int, hour: int = 0, minute: int = 0, second: int = 0, nanosecond: int = 0, time_scale: TimeScale = TimeScale.TAI):
        if not (0 <= hour < HOURS_PER_DAY and 0 <= minute < SECONDS_PER_MINUTE and 0 <= second < SECONDS_PER_MINUTE and 0 <= nanosecond < NANOSECONDS_PER_SECOND):
            raise ValueError("Invalid time components")

        # Calculate total days since epoch (0001-01-01)
        total_days = days_since_epoch(year, month, day) - days_since_epoch(cls.EPOCH_YEAR, 1, 1)

        # Calculate total nanoseconds from days
        nanoseconds = total_days * SECONDS_PER_DAY * NANOSECONDS_PER_SECOND

        # Add nanoseconds from time components
        nanoseconds += hour * SECONDS_PER_HOUR * NANOSECONDS_PER_SECOND
        nanoseconds += minute * SECONDS_PER_MINUTE * NANOSECONDS_PER_SECOND
        nanoseconds += second * NANOSECONDS_PER_SECOND
        nanoseconds += nanosecond

        return cls(nanoseconds, time_scale)

    def to_components(self) -> tuple[int, int, int, int, int, int, int]:
        # Convert nanoseconds_since_epoch back to components
        remaining_nanoseconds = self.nanoseconds_since_epoch

        # Calculate days since epoch
        total_days_since_epoch = remaining_nanoseconds // (SECONDS_PER_DAY * NANOSECONDS_PER_SECOND)
        remaining_nanoseconds %= (SECONDS_PER_DAY * NANOSECONDS_PER_SECOND)

        # Convert days back to year, month, day
        year, month, day = get_date_from_days_since_epoch(total_days_since_epoch + days_since_epoch(self.EPOCH_YEAR, 1, 1))

        # Calculate time components
        hour = remaining_nanoseconds // (SECONDS_PER_HOUR * NANOSECONDS_PER_SECOND)
        remaining_nanoseconds %= (SECONDS_PER_HOUR * NANOSECONDS_PER_SECOND)

        minute = remaining_nanoseconds // (SECONDS_PER_MINUTE * NANOSECONDS_PER_SECOND)
        remaining_nanoseconds %= (SECONDS_PER_MINUTE * NANOSECONDS_PER_SECOND)

        second = remaining_nanoseconds // NANOSECONDS_PER_SECOND
        nanosecond = remaining_nanoseconds % NANOSECONDS_PER_SECOND

        return year, month, day, hour, minute, second, nanosecond

    def to_utc(self, leap_second_table: "LeapSecondTable") -> TimePoint:
        if self.time_scale == TimeScale.UTC:
            return self
        elif self.time_scale == TimeScale.TAI:
            # TAI = UTC + offset
            # UTC = TAI - offset

            # Initial approximation for UTC time to find the offset.
            # We use the current TAI nanoseconds as an approximation for UTC nanoseconds
            # to look up the TAI-UTC offset. This is valid because leap seconds are discrete
            # and the offset doesn't change continuously.
            approx_utc_timepoint = TimePoint(self.nanoseconds_since_epoch, TimeScale.UTC)
            
            # Get the TAI-UTC offset for this approximate UTC time.
            tai_utc_offset_seconds = leap_second_table.get_tai_utc_offset(approx_utc_timepoint)

            # Calculate UTC nanoseconds: TAI_nanoseconds - (offset_seconds * NANOSECONDS_PER_SECOND)
            utc_nanoseconds_since_epoch = self.nanoseconds_since_epoch - (tai_utc_offset_seconds * NANOSECONDS_PER_SECOND)
            
            return TimePoint(utc_nanoseconds_since_epoch, TimeScale.UTC)
        else:
            raise ValueError(f"Unsupported time scale conversion from {self.time_scale.value} to UTC")

    def to_tai(self, leap_second_table: "LeapSecondTable") -> TimePoint:
        if self.time_scale == TimeScale.TAI:
            return self
        elif self.time_scale == TimeScale.UTC:
            # TAI = UTC + offset

            # Get the TAI-UTC offset for this UTC time.
            tai_utc_offset_seconds = leap_second_table.get_tai_utc_offset(self)

            # Calculate TAI nanoseconds: UTC_nanoseconds + (offset_seconds * NANOSECONDS_PER_SECOND)
            tai_nanoseconds_since_epoch = self.nanoseconds_since_epoch + (tai_utc_offset_seconds * NANOSECONDS_PER_SECOND)
            return TimePoint(tai_nanoseconds_since_epoch, TimeScale.TAI)
        else:
            raise ValueError(f"Unsupported time scale conversion from {self.time_scale.value} to TAI")

    def format(self, format_string: str, timezone=None): # Will require formatting logic
        raise NotImplementedError("Formatting not yet implemented")

