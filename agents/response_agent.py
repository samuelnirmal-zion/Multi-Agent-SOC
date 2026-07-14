from agents.parser import parse_log


def response_action(threat_result, log=""):

    data = parse_log(log)

    threat = threat_result.lower()

    actions = []

    # ---------------------------------
    # RANSOMWARE
    # ---------------------------------

    if "ransomware" in threat:

        actions.extend([
            f"Immediately isolate {data['hostname']} from the corporate network.",
            f"Terminate process {data['process']}.",
            f"Disable account {data['user']}.",
            f"Block source IP {data['source_ip']}.",
            "Preserve RAM and disk image for forensic investigation.",
            "Collect Indicators of Compromise (IoCs).",
            "Scan neighbouring endpoints using EDR.",
            "Restore encrypted files from secure backups.",
            "Notify SOC Manager and Incident Response Team."
        ])

    # ---------------------------------
    # BRUTE FORCE
    # ---------------------------------

    elif "brute force" in threat:

        actions.extend([
            f"Block source IP {data['source_ip']}.",
            f"Temporarily disable account {data['user']}.",
            "Force password reset.",
            "Enable Multi-Factor Authentication (MFA).",
            "Review authentication logs.",
            "Monitor login attempts for the next 24 hours."
        ])

    # ---------------------------------
    # PHISHING
    # ---------------------------------

    elif "phishing" in threat:

        actions.extend([
            "Quarantine suspicious emails.",
            "Block sender domain.",
            f"Reset password for {data['user']}.",
            "Scan workstation for malware.",
            "Conduct user awareness verification."
        ])

    # ---------------------------------
    # MALWARE
    # ---------------------------------

    elif "malware" in threat:

        actions.extend([
            "Disconnect affected endpoint.",
            "Perform full antivirus scan.",
            "Remove malicious binaries.",
            "Review persistence mechanisms.",
            "Monitor network communications."
        ])

    # ---------------------------------
    # DEFAULT
    # ---------------------------------

    else:

        actions.extend([
            "Continue monitoring.",
            "Review SIEM alerts.",
            "No immediate containment required."
        ])

    return (
        "RECOMMENDED RESPONSE\n\n"
        + "\n".join([f"✓ {item}" for item in actions])
    )