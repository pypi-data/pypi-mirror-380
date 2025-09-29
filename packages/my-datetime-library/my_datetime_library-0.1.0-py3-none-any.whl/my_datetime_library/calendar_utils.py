def is_leap_year(year: int) -> bool:
    """Determines if a given year is a leap year."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def days_in_month(year: int, month: int) -> int:
    """Returns the number of days in a given month of a given year."""
    if month < 1 or month > 12:
        raise ValueError("Month must be between 1 and 12")

    if month == 2: # February
        return 29 if is_leap_year(year) else 28
    elif month in [4, 6, 9, 11]: # April, June, September, November
        return 30
    else: # January, March, May, July, August, October, December
        return 31

def days_since_epoch(year: int, month: int, day: int) -> int:
    """Calculates the number of days since a theoretical epoch (Jan 1, Year 1)."""
    # This is a simplified calculation. A real-world library would need to handle
    # calendar changes (e.g., Gregorian calendar adoption) and potentially
    # different epochs (e.g., Unix epoch).
    # For now, we assume a continuous Gregorian calendar from year 1.

    if not (1 <= month <= 12 and 1 <= day <= days_in_month(year, month)):
        raise ValueError(f"Invalid date: {year}-{month}-{day}")

    total_days = 0
    # Days from full years before the given year
    for y in range(1, year):
        total_days += 366 if is_leap_year(y) else 365

    # Days from full months in the given year
    for m in range(1, month):
        total_days += days_in_month(year, m)

    # Days in the current month
    total_days += day - 1 # -1 because day 1 is the first day, not 0 days past

    return total_days

def get_date_from_days_since_epoch(days: int) -> tuple[int, int, int]:
    """Converts days since epoch (Jan 1, Year 1) back to year, month, day."""
    if days < 0:
        raise ValueError("Days since epoch cannot be negative")

    year = 1
    while True:
        days_in_year = 366 if is_leap_year(year) else 365
        if days < days_in_year:
            break
        days -= days_in_year
        year += 1

    month = 1
    while True:
        days_in_current_month = days_in_month(year, month)
        if days < days_in_current_month:
            break
        days -= days_in_current_month
        month += 1

    day = days + 1 # +1 because days are 0-indexed from start of month

    return year, month, day

