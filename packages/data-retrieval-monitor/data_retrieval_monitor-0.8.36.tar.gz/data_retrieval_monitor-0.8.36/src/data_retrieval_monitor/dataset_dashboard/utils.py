from datetime import datetime, timezone
import pytz

def px(n: int) -> str:
    return f"{int(n)}px"

def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()

def to_local_str(iso_str: str | None, tz_name: str) -> str:
    if not iso_str:
        return "-"
    try:
        dt = datetime.fromisoformat(iso_str.replace("Z", "+00:00"))
        if not dt.tzinfo:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt.astimezone(pytz.timezone(tz_name)).strftime("%Y-%m-%d %H:%M:%S %Z")
    except Exception:
        return str(iso_str)