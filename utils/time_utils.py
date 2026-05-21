from datetime import datetime, timezone


def get_current_time() -> datetime:
    """Return the current time in UTC."""
    return datetime.now(timezone.utc)


def format_timestamp(dt: datetime) -> str:
    return dt.strftime("%Y-%m-%d %I:%M:%S %p")
