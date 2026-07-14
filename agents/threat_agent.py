from agents.parser import parse_log


def analyze_threat(log):

    data = parse_log(log)

    score = 0
    evidence = []
    threat_type = "Unknown Activity"

    text = log.lower()

    # -----------------------------
    # Ransomware Detection
    # -----------------------------
    if (
        "encrypt" in text
        or ".locked" in text
        or "ransomware" in text
        or "mass file encryption" in text
    ):
        threat_type = "Ransomware"

        score += 50

        evidence.append("Mass file encryption detected")
        evidence.append("Suspicious encryption process observed")

    # -----------------------------
    # Brute Force
    # -----------------------------
    elif (
        "failed login" in text
        or "multiple failed login" in text
        or "authentication failed" in text
    ):

        threat_type = "Brute Force Attack"

        score += 40

        evidence.append("Multiple authentication failures")

    # -----------------------------
    # Phishing
    # -----------------------------
    elif (
        "phishing" in text
        or "fake login" in text
        or "malicious email" in text
    ):

        threat_type = "Phishing Attempt"

        score += 35

        evidence.append("Suspicious email activity detected")

    # -----------------------------
    # Malware
    # -----------------------------
    elif (
        "malware" in text
        or "trojan" in text
        or "virus" in text
        or "worm" in text
    ):

        threat_type = "Malware Infection"

        score += 45

        evidence.append("Known malware keyword detected")

    else:

        score = 10

        evidence.append("No known attack pattern matched")

    # -----------------------------
    # CPU
    # -----------------------------

    if data["cpu"] != "Unknown":

        try:

            cpu = int(
                data["cpu"].replace("%", "")
            )

            if cpu >= 90:

                score += 20

                evidence.append("High CPU utilization")

        except:

            pass

    # -----------------------------
    # Files Modified
    # -----------------------------

    if data["files_modified"] != "Unknown":

        try:

            files = int(data["files_modified"])

            if files > 500:

                score += 20

                evidence.append("Large number of files modified")

        except:

            pass

    confidence = min(score, 100)

    return f"""
Threat Type        : {threat_type}

Confidence Score   : {confidence}%

MITRE ATT&CK

T1486 (Simulated)

Evidence

• {'\n• '.join(evidence)}
"""