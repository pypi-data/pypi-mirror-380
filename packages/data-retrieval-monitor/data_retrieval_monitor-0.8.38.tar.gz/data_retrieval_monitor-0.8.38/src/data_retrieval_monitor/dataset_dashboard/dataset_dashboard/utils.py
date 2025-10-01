from datetime import datetime, timezone
import pytz

def utc_now_iso():
    return datetime.now(timezone.utc).isoformat()

def to_local_str(ts_iso, tzname="UTC"):
    if not ts_iso:
        return "-"
    try:
        dt = datetime.fromisoformat(str(ts_iso).replace("Z","+00:00"))
        tz = pytz.timezone(tzname or "UTC")
        return dt.astimezone(tz).strftime("%Y-%m-%d %H:%M:%S %Z")
    except Exception:
        return str(ts_iso)

def px(n:int) -> str:
    return f"{int(n)}px"
