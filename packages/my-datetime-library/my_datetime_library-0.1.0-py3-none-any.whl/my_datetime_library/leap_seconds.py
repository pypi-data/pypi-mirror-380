from typing import List, Tuple, TYPE_CHECKING
from bisect import bisect_right

from .constants import NANOSECONDS_PER_SECOND, SECONDS_PER_DAY, SECONDS_PER_HOUR, SECONDS_PER_MINUTE, HOURS_PER_DAY
from .calendar_utils import days_since_epoch

if TYPE_CHECKING:
    from .timepoint import TimePoint, TimeScale

# Constants for converting between our internal epoch (0001-01-01 00:00:00) and other epochs.
# These are based on a continuous Gregorian calendar.

# Days from 0001-01-01 to 1900-01-01 (exclusive of 1900-01-01)
DAYS_0001_TO_1900 = days_since_epoch(1900, 1, 1) - days_since_epoch(1, 1, 1)
SECONDS_0001_TO_1900 = DAYS_0001_TO_1900 * SECONDS_PER_DAY

# Days from 0001-01-01 to 1970-01-01 (exclusive of 1970-01-01)
DAYS_0001_TO_1970 = days_since_epoch(1970, 1, 1) - days_since_epoch(1, 1, 1)
SECONDS_0001_TO_1970 = DAYS_0001_TO_1970 * SECONDS_PER_DAY

class LeapSecondTable:
    def __init__(self):
        # Stores (ntp_timestamp_seconds, cumulative_tai_utc_offset_seconds)
        # ntp_timestamp_seconds: seconds since 1900-01-01 00:00:00 UTC
        # cumulative_tai_utc_offset_seconds: TAI - UTC offset in seconds *after* this timestamp
        self.leap_seconds_data: List[Tuple[int, int]] = []

    def load_from_file(self, filepath: str):
        """Loads leap second data from a file like 'leap-seconds.list'."""
        self.leap_seconds_data = []
        with open(filepath, 'r') as f:
            for line in f:
                line = line.strip()
                # Skip comments, header lines, and hash lines
                if not line or line.startswith(('$', '@', 'h')):
                    continue
                
                # The actual data lines start with a number (NTP timestamp)
                if line.startswith('#'): # Skip comments within data section
                    continue

                parts = line.split()
                if len(parts) >= 2:
                    try:
                        ntp_timestamp = int(parts[0])
                        tai_utc_offset = int(parts[1])
                        self.leap_seconds_data.append((ntp_timestamp, tai_utc_offset))
                    except (ValueError, IndexError) as e:
                        print(f"Warning: Could not parse line in leap-seconds.list: {line} - {e}")
        # Ensure data is sorted by timestamp, though it usually is.
        self.leap_seconds_data.sort(key=lambda x: x[0])

    def get_tai_utc_offset(self, timepoint_utc: "TimePoint") -> int:
        """Returns the TAI-UTC offset (in seconds) for a given UTC TimePoint.
        The input TimePoint MUST be in UTC scale.
        """
        if timepoint_utc.time_scale.value != "UTC":
            raise ValueError("Input TimePoint must be in UTC scale to get TAI-UTC offset.")

        seconds_since_0001_utc = timepoint_utc.nanoseconds_since_epoch // NANOSECONDS_PER_SECOND
        ntp_seconds = seconds_since_0001_utc - SECONDS_0001_TO_1900

        # Use binary search to find the correct leap second entry
        # bisect_right returns an insertion point which comes after (to the right of) any existing entries of the value.
        # This means it points to the first element *greater* than the value.
        # We want the element *less than or equal to* the value, so we need to go back one step.
        
        # Extract just the NTP timestamps for binary search
        timestamps = [entry[0] for entry in self.leap_seconds_data]
        
        idx = bisect_right(timestamps, ntp_seconds)

        if idx == 0:
            # If the timepoint is before the first leap second event, the offset is 0.
            return 0
        else:
            # The correct entry is at idx - 1
            return self.leap_seconds_data[idx - 1][1]

    def get_leap_second_events(self) -> List[Tuple[int, int]]:
        """Returns the raw list of leap second events (NTP timestamp, TAI-UTC offset)."""
        return self.leap_seconds_data

