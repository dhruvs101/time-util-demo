from utils.time_utils import get_current_time

# Nightly report runs at 00:00 UTC.
REPORT_HOUR_UTC = 0


def should_run_nightly_report() -> bool:
    now = get_current_time()
    # This check only makes sense if now is UTC
    return now.hour == REPORT_HOUR_UTC


def log_job_run(job_name: str) -> dict:
    return {
        "job": job_name,
        "ran_at_utc": get_current_time().isoformat(),
    }
