import os
from datetime import datetime
from uuid import uuid4

from dotenv import load_dotenv

from agents.log_agent import analyze_log
from agents.threat_agent import analyze_threat
from agents.malware_agent import analyze_malware
from agents.parser import parse_log
from agents.response_agent import response_action
from agents.severity_agent import analyze_severity

from reports.report_generator import save_report

load_dotenv()

try:
    from langchain_groq import ChatGroq
except ImportError:
    ChatGroq = None


def _build_fallback_response(message):

    return (
        "SOC Coordinator is running in Offline Mode.\n\n"
        f"Original Security Log:\n{message}"
    )


def _build_model():

    api_key = os.getenv("GROQ_API_KEY")

    if not api_key or ChatGroq is None:
        return None

    return ChatGroq(
        model="llama-3.3-70b-versatile",
        api_key=api_key,
    )


model = _build_model()


def coordinator(message):

    if not message or not message.strip():
        return "Please provide a security log."

    # ============================================
    # STEP 1 : LOG AGENT
    # ============================================

    log_analysis = analyze_log(message)

    # ============================================
    # STEP 2 : THREAT AGENT
    # ============================================

    threat_analysis = analyze_threat(message)

    # ============================================
    # STEP 3 : MALWARE AGENT
    # ============================================

    malware_analysis = analyze_malware(message)

    # ============================================
    # STEP 4 : RESPONSE AGENT
    # ============================================

    response_analysis = response_action(
        threat_analysis,
        message
    )

    # ============================================
    # STEP 5 : SEVERITY AGENT
    # ============================================

    severity = analyze_severity(message)

    # ============================================
    # STEP 6 : COORDINATOR AI
    # ============================================

    if model is None:

        ai_response = _build_fallback_response(message)

    else:

        try:

            response = model.invoke(
                [
                    (
                        "system",
                        """
You are a Senior SOC Analyst working in a Security Operations Center.

Your responsibility is to analyse the outputs received from multiple cybersecurity agents and prepare a professional incident report.

The report must contain the following sections:

1. Executive Summary
2. Threat Classification
3. Affected Assets
4. Indicators of Compromise (IoCs)
5. MITRE ATT&CK Technique (if applicable)
6. Business Impact
7. Recommended Response
8. Final Analyst Verdict

Keep the report professional.

Do not repeat information.

Do not invent information that is not present.

Write like a real SOC analyst.
                        """,
                    ),
                    (
                        "human",
                        f"""
Security Event

{message}

------------------------------------

Log Analysis

{log_analysis}

------------------------------------

Threat Analysis

{threat_analysis}

------------------------------------

Malware Analysis

{malware_analysis}

------------------------------------

Severity Assessment

{severity}

------------------------------------

Recommended Response

{response_analysis}

Generate a professional SOC Incident Report.
                        """,
                    ),
                ]
            )

            ai_response = (
                response.content
                if hasattr(response, "content")
                else str(response)
            )

        except Exception:

            ai_response = _build_fallback_response(message)

    incident = parse_log(message)

    incident_id = "SOC-" + uuid4().hex[:8].upper()

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # ============================================
    # STEP 7 : BUILD FINAL REPORT
    # ============================================

    final_report = f"""
============================================================
               AI POWERED SOC INCIDENT REPORT
============================================================

Incident ID : {incident_id}

Status : ACTIVE

============================================================
EVENT INFORMATION
============================================================

Hostname           : {incident["hostname"]}

Username           : {incident["user"]}

Source IP          : {incident["source_ip"]}

Destination IP     : {incident["destination_ip"]}

Process            : {incident["process"]}

CPU Usage          : {incident["cpu"]}

Files Modified     : {incident["files_modified"]}

============================================================
ORIGINAL SECURITY EVENT
============================================================

{message}

============================================================
LOG ANALYSIS
============================================================

{log_analysis}

============================================================
THREAT ANALYSIS
============================================================

{threat_analysis}

============================================================
MALWARE ANALYSIS
============================================================

{malware_analysis}

============================================================
SEVERITY ASSESSMENT
============================================================

{severity}

============================================================
RECOMMENDED RESPONSE
============================================================

{response_analysis}

============================================================
AI SOC ANALYST SUMMARY
============================================================

{ai_response}

============================================================
INCIDENT STATUS
============================================================

Status

✔ Investigation Completed

✔ Threat Classified

✔ Response Generated

✔ Report Saved

============================================================
"""

    # ============================================
    # STEP 8 : SAVE REPORT
    # ============================================

    report_path = save_report(final_report)
        # ============================================
    # STEP 9 : APPEND REPORT STATUS
    # ============================================

    final_report += f"""
============================================================

Report Saved Successfully

Location

{report_path}

============================================================
END OF REPORT
============================================================
"""

    # ============================================
    # STEP 10 : RETURN REPORT
    # ============================================

    return final_report