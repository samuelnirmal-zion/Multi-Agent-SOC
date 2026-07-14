from agents.parser import parse_log


def analyze_severity(log):

    data = parse_log(log)

    score = 0
    reasons = []

    text = log.lower()

    # -----------------------------
    # Threat Indicators
    # -----------------------------

    if (
        "ransomware" in text
        or "encrypt" in text
        or ".locked" in text
    ):

        score += 45
        reasons.append("Ransomware behaviour detected")

    if (
        "failed login" in text
        or "authentication failed" in text
    ):

        score += 30
        reasons.append("Multiple failed logins")

    if "malware" in text:

        score += 35
        reasons.append("Malware indicators present")

    if "virus" in text:

        score += 30
        reasons.append("Virus detected")

    if "trojan" in text:

        score += 35
        reasons.append("Trojan activity")

    if "worm" in text:

        score += 35
        reasons.append("Network worm behaviour")

    if "phishing" in text:

        score += 25
        reasons.append("Phishing indicators")

    # -----------------------------
    # High CPU
    # -----------------------------

    if data["cpu"] != "Unknown":

        try:

            cpu = int(data["cpu"].replace("%", ""))

            if cpu >= 90:
                score += 15
                reasons.append("High CPU usage")

        except:
            pass

    # -----------------------------
    # Large File Modification
    # -----------------------------

    if data["files_modified"] != "Unknown":

        try:

            files = int(data["files_modified"])

            if files >= 500:
                score += 20
                reasons.append("Mass file modification")

        except:
            pass

    score = min(score, 100)

    if score >= 80:
        severity = "🔴 Critical"

    elif score >= 60:
        severity = "🟠 High"

    elif score >= 35:
        severity = "🟡 Medium"

    else:
        severity = "🟢 Low"

    return f"""
Overall Severity : {severity}

Risk Score       : {score}/100

Reasons

• {'\n• '.join(reasons)}
"""