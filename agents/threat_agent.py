def analyze_threat(log):
    """
    Checks the log for known threat keywords.
    """

    log = log.lower()

    if "failed login" in log:
        return "Threat Agent: Possible Brute Force Attack"

    elif "malware" in log:
        return "Threat Agent: Malware Activity Detected"

    elif "ransomware" in log:
        return "Threat Agent: Possible Ransomware Detected"

    elif "phishing" in log:
        return "Threat Agent: Possible Phishing Attempt"

    else:
        return "Threat Agent: No known threat detected"