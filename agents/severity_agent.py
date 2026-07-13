def analyze_severity(log):

    log = log.lower()

    if "ransomware" in log:
        return "🔴 Critical"

    elif "malware" in log:
        return "🔴 Critical"

    elif "brute force" in log:
        return "🟠 High"

    elif "failed login" in log:
        return "🟠 High"

    elif "phishing" in log:
        return "🟡 Medium"

    elif "virus" in log:
        return "🟠 High"

    else:
        return "🟢 Low"