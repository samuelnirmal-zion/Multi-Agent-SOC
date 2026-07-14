import re


def parse_log(log: str):

    data = {
        "timestamp": "Unknown",
        "hostname": "Unknown",
        "user": "Unknown",
        "source_ip": "Unknown",
        "destination_ip": "Unknown",
        "process": "Unknown",
        "behavior": "Unknown",
        "files_modified": "Unknown",
        "cpu": "Unknown",
        "extension": "Unknown",
        "attempts": "Unknown",
        "sender": "Unknown",
        "email_subject": "Unknown",
    }

    patterns = {
        "timestamp": r"Timestamp\s*=\s*(.*)",
        "hostname": r"Hostname\s*=\s*(.*)",
        "user": r"User\s*=\s*(.*)",
        "source_ip": r"Source_IP\s*=\s*(.*)",
        "destination_ip": r"Destination_IP\s*=\s*(.*)",
        "process": r"Process\s*=\s*(.*)",
        "behavior": r"Behavior\s*=\s*(.*)",
        "files_modified": r"Files_Modified\s*=\s*(.*)",
        "cpu": r"CPU\s*=\s*(.*)",
        "extension": r"Extension\s*=\s*(.*)",
        "attempts": r"Attempts\s*=\s*(.*)",
        "sender": r"Sender\s*=\s*(.*)",
        "email_subject": r"Email_Subject\s*=\s*(.*)",
    }

    for key, pattern in patterns.items():

        match = re.search(pattern, log, re.IGNORECASE)

        if match:
            data[key] = match.group(1).strip()

    return data