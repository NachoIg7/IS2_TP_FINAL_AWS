import datetime

CorporateLog = []

def write_log(action, user="system", status="OK", details=""):
    log_entry = {
        "timestamp": datetime.datetime.now().isoformat(),
        "user":user,
        "ACTION":action,
        "status":status,
        "details":details
    }
    CorporateLog.append(log_entry)
    return log_entry

def get_logs():
    return CorporateLog