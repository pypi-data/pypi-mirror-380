class Duration:
    def __init__(self, nanoseconds: int):
        if not isinstance(nanoseconds, int):
            raise TypeError("nanoseconds must be an integer")
        self.nanoseconds = nanoseconds

    def __repr__(self):
        return f"Duration(nanoseconds={self.nanoseconds})"

    def __eq__(self, other):
        if not isinstance(other, Duration):
            return NotImplemented
        return self.nanoseconds == other.nanoseconds

    def __lt__(self, other):
        if not isinstance(other, Duration):
            return NotImplemented
        return self.nanoseconds < other.nanoseconds

    def __le__(self, other):
        if not isinstance(other, Duration):
            return NotImplemented
        return self.nanoseconds <= other.nanoseconds

    def __gt__(self, other):
        if not isinstance(other, Duration):
            return NotImplemented
        return self.nanoseconds > other.nanoseconds

    def __ge__(self, other):
        if not isinstance(other, Duration):
            return NotImplemented
        return self.nanoseconds >= other.nanoseconds

    def __add__(self, other):
        if not isinstance(other, Duration):
            return NotImplemented
        return Duration(self.nanoseconds + other.nanoseconds)

    def __sub__(self, other):
        if not isinstance(other, Duration):
            return NotImplemented
        return Duration(self.nanoseconds - other.nanoseconds)

    @classmethod
    def from_seconds(cls, seconds: int | float):
        return cls(int(seconds * 1_000_000_000))

    @classmethod
    def from_minutes(cls, minutes: int | float):
        return cls(int(minutes * 60 * 1_000_000_000))

    @classmethod
    def from_hours(cls, hours: int | float):
        return cls(int(hours * 3600 * 1_000_000_000))

    @classmethod
    def from_days(cls, days: int | float):
        return cls(int(days * 86400 * 1_000_000_000))

    def to_seconds(self) -> float:
        return self.nanoseconds / 1_000_000_000

    def to_minutes(self) -> float:
        return self.nanoseconds / (60 * 1_000_000_000)

    def to_hours(self) -> float:
        return self.nanoseconds / (3600 * 1_000_000_000)

    def to_days(self) -> float:
        return self.nanoseconds / (86400 * 1_000_000_000)

