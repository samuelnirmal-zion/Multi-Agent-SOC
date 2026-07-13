import os
from datetime import datetime


def save_report(report):
    """
    Save the SOC report into the generated_reports folder.
    """

    # Create the folder if it doesn't exist
    os.makedirs("reports/generated_reports", exist_ok=True)

    # Create a unique filename using date and time
    filename = datetime.now().strftime(
        "SOC_Report_%Y%m%d_%H%M%S.txt"
    )

    # Full file path
    filepath = os.path.join(
        "reports",
        "generated_reports",
        filename,
    )

    # Save the report
    with open(filepath, "w", encoding="utf-8") as file:
        file.write(report)

    return filepath