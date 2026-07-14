from agents.parser import parse_log


def analyze_log(log):

    data = parse_log(log)

    return f"""
Event Summary

Timestamp          : {data['timestamp']}
Hostname           : {data['hostname']}
User               : {data['user']}
Source IP          : {data['source_ip']}
Destination IP     : {data['destination_ip']}
Process            : {data['process']}
Behaviour          : {data['behavior']}
CPU Usage          : {data['cpu']}
Files Modified     : {data['files_modified']}
"""