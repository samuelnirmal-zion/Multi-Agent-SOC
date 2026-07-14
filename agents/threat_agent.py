from agents.parser import parse_log


def analyze_threat(log):

    data = parse_log(log)

    text = log.lower()

    if (
        "ransomware" in text
        or "encrypt" in text
        or ".locked" in text
    ):

        return f"""
Threat Classification

Attack Type : Ransomware

Confidence : 98%

Affected Host : {data['hostname']}

MITRE ATT&CK : T1486 (Data Encrypted for Impact)
"""

    elif (
        "failed login" in text
        or "authentication" in text
    ):

        return f"""
Threat Classification

Attack Type : Brute Force

Confidence : 94%

Target User : {data['user']}

MITRE ATT&CK : T1110 (Brute Force)
"""

    elif "phishing" in text:

        return f"""
Threat Classification

Attack Type : Phishing

Confidence : 92%

Target User : {data['user']}

MITRE ATT&CK : T1566 (Phishing)
"""

    elif (
        "trojan" in text
        or "virus" in text
        or "worm" in text
        or "malware" in text
    ):

        return f"""
Threat Classification

Attack Type : Malware

Confidence : 90%

Affected Host : {data['hostname']}

MITRE ATT&CK : T1204 (User Execution)
"""

    else:

        return """
Threat Classification

No Known Threat Detected

Confidence : 15%
"""