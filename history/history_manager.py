import json
import os
from datetime import datetime


HISTORY_FILE = "history/incidents.json"


def save_incident(incident):

    incident["timestamp"] = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    if not os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "w") as file:
            json.dump([], file)


    with open(HISTORY_FILE, "r") as file:
        incidents = json.load(file)


    incidents.append(incident)


    with open(HISTORY_FILE, "w") as file:
        json.dump(
            incidents,
            file,
            indent=4
        )


def get_incidents():

    if not os.path.exists(HISTORY_FILE):
        return []


    with open(HISTORY_FILE, "r") as file:
        return json.load(file)