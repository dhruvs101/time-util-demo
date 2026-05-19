from utils.time_utils import get_current_time


def record_event(user_id: str, action: str, metadata: dict = None) -> dict:
    """Write an audit log entry. Timestamp is UTC for compliance."""
    return {
        "user_id": user_id,
        "action": action,
        "timestamp": get_current_time().isoformat(),  # must be UTC for GDPR audit trail
        "metadata": metadata or {},
    }
