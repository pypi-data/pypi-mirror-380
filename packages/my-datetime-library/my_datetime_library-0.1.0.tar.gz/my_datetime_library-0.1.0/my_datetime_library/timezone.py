from typing import Dict, List, Tuple, Optional
import os
from bisect import bisect_right

from .timepoint import TimePoint, TimeScale
from .constants import NANOSECONDS_PER_SECOND, SECONDS_PER_MINUTE, SECONDS_PER_HOUR, SECONDS_PER_DAY

class TimeZone:
    def __init__(self, name: str):
        self.name = name
        # Rules will be loaded from IANA TZDB
        # This will be a list of (effective_from_utc_nanoseconds, total_offset_seconds, abbr)
        self.rules: List[Tuple[int, int, str]] = []

    def __repr__(self):
        return f"TimeZone(\"{self.name}\")"

    def get_total_offset_and_abbr(self, timepoint_utc: TimePoint) -> Tuple[int, str]:
        """Returns the total UTC offset (in seconds) and abbreviation for a given UTC TimePoint.
        The input TimePoint MUST be in UTC scale.
        """
        if timepoint_utc.time_scale != TimeScale.UTC:
            raise ValueError("Input TimePoint must be in UTC scale to get offset.")

        utc_nanoseconds = timepoint_utc.nanoseconds_since_epoch

        # Use binary search to find the correct rule entry
        # Extract just the effective_from_utc_nanoseconds for binary search
        effective_times = [entry[0] for entry in self.rules]
        
        idx = bisect_right(effective_times, utc_nanoseconds)

        if idx == 0:
            # If the timepoint is before the first rule, return a default (e.g., 0 offset, or raise error)
            # For robustness, we might need a default rule or a way to handle times outside loaded rules.
            # For now, return 0 offset and "UTC" as abbreviation.
            return 0, "UTC"
        else:
            # The correct entry is at idx - 1
            _, total_offset, abbr = self.rules[idx - 1]
            return total_offset, abbr

    def localize(self, timepoint_utc: TimePoint) -> TimePoint:
        """Converts a UTC TimePoint to a local TimePoint in this time zone.
        Returns a new TimePoint representing the local time, with its nanoseconds_since_epoch adjusted.
        The returned TimePoint will have TimeScale.UTC, but its components will reflect local time.
        """
        if timepoint_utc.time_scale != TimeScale.UTC:
            raise ValueError("Input TimePoint must be in UTC scale for localization.")
        
        total_offset_seconds, _ = self.get_total_offset_and_abbr(timepoint_utc)
        local_nanoseconds = timepoint_utc.nanoseconds_since_epoch + (total_offset_seconds * NANOSECONDS_PER_SECOND)
        return TimePoint(local_nanoseconds, TimeScale.UTC)

    def unlocalize(self, local_timepoint: TimePoint) -> TimePoint:
        """Converts a local TimePoint in this time zone back to a UTC TimePoint.
        This is complex due to ambiguous and non-existent times during DST transitions.
        For a simplified implementation, we will assume no ambiguity and simply subtract the offset.
        A more robust implementation would require checking for overlaps and gaps.
        """
        approx_utc_nanoseconds = local_timepoint.nanoseconds_since_epoch
        approx_utc_tp = TimePoint(approx_utc_nanoseconds, TimeScale.UTC)
        
        total_offset_seconds, _ = self.get_total_offset_and_abbr(approx_utc_tp)
        
        utc_nanoseconds = local_timepoint.nanoseconds_since_epoch - (total_offset_seconds * NANOSECONDS_PER_SECOND)
        return TimePoint(utc_nanoseconds, TimeScale.UTC)


class TimeZoneDatabase:
    def __init__(self):
        self.zones: Dict[str, TimeZone] = {}

    def load_from_tzdata_files(self, directory: str):
        """Loads time zone rules from parsed IANA tzdata files.
        This is a placeholder for a complex parsing process.
        For now, it will load zone names from zone.tab and create dummy TimeZone objects.
        Actual rules parsing will be a significant undertaking.
        """
        print(f"Loading timezone data from {directory} (simplified)")
        zone_tab_path = os.path.join(directory, "zone.tab")
        zone1970_tab_path = os.path.join(directory, "zone1970.tab")

        zone_names = set()
        if os.path.exists(zone_tab_path):
            with open(zone_tab_path, 'r') as f:
                for line in f:
                    line = line.strip()
                    if not line or line.startswith('#'):
                        continue
                    parts = line.split('\t')
                    if len(parts) >= 3:
                        zone_names.add(parts[2])
        
        if os.path.exists(zone1970_tab_path):
            with open(zone1970_tab_path, 'r') as f:
                for line in f:
                    line = line.strip()
                    if not line or line.startswith('#'):
                        continue
                    parts = line.split('\t')
                    if len(parts) >= 3:
                        zone_names.add(parts[2])

        for name in sorted(list(zone_names)):
            tz = TimeZone(name)
            # For now, create dummy TimeZone objects with a single, fixed rule.
            # This is NOT a real TZDB implementation, but a placeholder.
            # Real implementation would parse 'zone', 'rule', 'link' files.
            # (effective_from_utc_nanoseconds, total_offset_seconds, abbr)
            # Let's assume a fixed offset for now for all zones for testing purposes.
            # For example, let's make 'America/New_York' -5 hours, 'Europe/London' 0 hours.
            if "America/New_York" in name:
                tz.rules.append((-(2**63), -5 * SECONDS_PER_HOUR, "EST"))
            elif "Europe/London" in name:
                tz.rules.append((-(2**63), 0, "GMT"))
            else:
                tz.rules.append((-(2**63), 0, "UTC"))
            self.zones[name] = tz

    def get_timezone(self, name: str) -> Optional[TimeZone]:
        return self.zones.get(name)

