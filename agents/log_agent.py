from agents.parser import parse_log


def analyze_log(log):

    data = parse_log(log)

    return f"""
EVENT DETAILS

Timestamp          : {data['timestamp']}
Hostname           : {data['hostname']}
Username           : {data['user']}
Source IP          : {data['source_ip']}
Destination IP     : {data['destination_ip']}
Process            : {data['process']}
Event ID           : {data['event_id']}
Port               : {data['port']}
Behavior           : {data['behavior']}
Files Modified     : {data['files_modified']}
File Extension     : {data['extension']}
CPU Usage          : {data['cpu']}
"""