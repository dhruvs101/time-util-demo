from datetime import datetime


def get_current_time() -> datetime:
    """Return the current local time."""
    return datetime.now()


def format_timestamp(dt: datetime) -> str:
    return dt.strftime("%Y-%m-%d %H:%M:%S UTC")
