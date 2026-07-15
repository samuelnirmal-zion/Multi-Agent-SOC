from agents.parser import parse_log


def response_action(threat_result, log):

    data = parse_log(log)

    threat = threat_result.lower()

    actions = []

    # --------------------------------
    # RANSOMWARE
    # --------------------------------

    if "ransomware" in threat:

        actions = [

            "Isolate endpoint {data['hostname']}",

            "Terminate process {data['process']}",

            "Disable account {data['user']}",

            "Block source IP {data['source_ip']}",

            "Preserve RAM for forensic investigation",

            "Acquire disk image",

            "Collect Indicators of Compromise (IoCs)",

            "Restore encrypted files from backup",

            "Notify Incident Response Team"

        ]

    # --------------------------------
    # BRUTE FORCE
    # --------------------------------

    elif "brute force" in threat:

        actions = [

            "Block source IP {data['source_ip']}",

            "Temporarily disable account {data['user']}",

            "Force password reset",

            "Enable Multi-Factor Authentication (MFA)",

            "Review authentication logs",

            "Increase monitoring for 24 hours"

        ]

    # --------------------------------
    # PHISHING
    # --------------------------------

    elif "phishing" in threat:

        actions = [

            "Quarantine suspicious email",

            "Block sender domain",

            f"Reset password for {data['user']}",

            "Scan endpoint for malware",

            "Perform mailbox investigation",

            "Notify affected employee"

        ]

    # --------------------------------
    # MALWARE
    # --------------------------------

    elif "malware" in threat:

        actions = [

            "Disconnect affected endpoint",

            "Run endpoint antivirus scan",

            "Remove malicious binaries",

            "Review persistence mechanisms",

            "Monitor outbound traffic"

        ]

    # --------------------------------
    # DEFAULT
    # --------------------------------

    else:

        actions = [

            "Continue monitoring",

            "Review SIEM alerts",

            "No immediate containment required"

        ]

    output = "RECOMMENDED RESPONSE\n\n"

    for action in actions:

        output += f"✓ {action}\n"

    return output