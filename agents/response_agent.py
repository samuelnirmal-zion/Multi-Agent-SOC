def response_action(threat_result):
    """
    Suggests the appropriate response based on the detected threat.
    """

    threat = threat_result.lower()

    # Brute Force Response
    if "brute force" in threat:
        return (
            "• Block the suspicious IP address.\n"
            "• Lock the affected user account.\n"
            "• Enable Multi-Factor Authentication (MFA).\n"
            "• Monitor login attempts for the next 24 hours."
        )

    # Malware Response
    elif "malware" in threat:
        return (
            "• Isolate the infected device from the network.\n"
            "• Run a complete antivirus scan.\n"
            "• Remove malicious files.\n"
            "• Investigate possible lateral movement."
        )

    # Phishing Response
    elif "phishing" in threat:
        return (
            "• Reset the user's password.\n"
            "• Scan the mailbox for malicious emails.\n"
            "• Block the sender's email address.\n"
            "• Conduct user awareness training."
        )

    # Unauthorized Access Response
    elif "unauthorized" in threat:
        return (
            "• Disable the compromised account.\n"
            "• Review audit logs.\n"
            "• Force password reset.\n"
            "• Investigate all recent activities."
        )

    # Default Response
    else:
        return (
            "• Continue monitoring the environment.\n"
            "• Review system logs.\n"
            "• No immediate action required."
        )