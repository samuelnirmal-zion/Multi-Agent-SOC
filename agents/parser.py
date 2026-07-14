import re


def parse_log(log: str):

    data = {
        "timestamp": "Unknown",
        "hostname": "Unknown",
        "user": "Unknown",
        "source_ip": "Unknown",
        "destination_ip": "Unknown",
        "process": "Unknown",
        "event_id": "Unknown",
        "port": "Unknown",
        "behavior": "Unknown",
        "files_modified": "Unknown",
        "extension": "Unknown",
        "cpu": "Unknown"
    }

    patterns = {
        "timestamp": r"timestamp\s*[:=]\s*(.+)",
        "hostname": r"hostname\s*[:=]\s*(.+)",
        "user": r"user\s*[:=]\s*(.+)",
        "source_ip": r"(?:source[_ ]?ip|src[_ ]?ip)\s*[:=]\s*([\d\.]+)",
        "destination_ip": r"(?:destination[_ ]?ip|dest[_ ]?ip|dst[_ ]?ip)\s*[:=]\s*([\d\.]+)",
        "process": r"process\s*[:=]\s*(.+)",
        "event_id": r"event[_ ]?id\s*[:=]\s*(.+)",
        "port": r"port\s*[:=]\s*(.+)",
        "behavior": r"behavior\s*[:=]\s*(.+)",
        "files_modified": r"files[_ ]?modified\s*[:=]\s*(.+)",
        "extension": r"extension\s*[:=]\s*(.+)",
        "cpu": r"cpu\s*[:=]\s*(.+)"
    }

    for key, pattern in patterns.items():

        match = re.search(
            pattern,
            log,
            re.IGNORECASE
        )

        if match:
            data[key] = match.group(1).strip()

    return data