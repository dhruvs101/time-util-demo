from utils.time_utils import get_current_time

# Orders expire 24 hours after creation.
# created_at is stored as UTC in the database.
ORDER_EXPIRY_HOURS = 24


def create_order(product_id: str, user_id: str) -> dict:
    now = get_current_time()
    return {
        "product_id": product_id,
        "user_id": user_id,
        "created_at": now.isoformat(),  # saved as UTC to DB
        "status": "pending",
    }


def is_order_expired(order: dict) -> bool:
    from datetime import timezone
    created_at = order["created_at"]  # ISO UTC string from DB
    from datetime import datetime
    created = datetime.fromisoformat(created_at)
    now = get_current_time()
    # Both sides must be UTC for this comparison to be correct
    elapsed_hours = (now - created).total_seconds() / 3600
    return elapsed_hours > ORDER_EXPIRY_HOURS
