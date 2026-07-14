from agents.parser import parse_log


def analyze_severity(log):

    data = parse_log(log)

    score = 0
    reasons = []

    text = log.lower()

    # -----------------------------
    # Threat Indicators
    # -----------------------------

    if "ransomware" in text or "encrypt" in text or ".locked" in text:
        score += 45
        reasons.append("Ransomware behaviour detected")

    if "failed login" in text or "authentication" in text:
        score += 30
        reasons.append("Repeated failed authentication")

    if "phishing" in text:
        score += 25
        reasons.append("Phishing indicators found")

    if "trojan" in text:
        score += 35
        reasons.append("Trojan activity detected")

    if "virus" in text:
        score += 30
        reasons.append("Virus detected")

    if "worm" in text:
        score += 35
        reasons.append("Network worm behaviour")

    if "malware" in text:
        score += 30
        reasons.append("Malware indicators")

    # -----------------------------
    # CPU Usage
    # -----------------------------

    try:
        cpu = int(data["cpu"].replace("%", ""))

        if cpu >= 90:
            score += 15
            reasons.append("High CPU utilisation")

    except:
        pass

    # -----------------------------
    # Files Modified
    # -----------------------------

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

Risk Score : {score}/100

Risk Factors

• {'\n• '.join(reasons)}
"""