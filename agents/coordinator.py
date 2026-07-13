import os
from dotenv import load_dotenv

from agents.log_agent import analyze_log
from agents.threat_agent import analyze_threat
from agents.malware_agent import analyze_malware
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

    response_analysis = response_action(threat_analysis)

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
You are the Coordinator Agent of a Multi-Agent Security Operations Center.

You receive outputs from specialized agents.

Create one professional SOC Report.

The report MUST contain:

1. Incident Summary

2. Threat Level

3. Affected Asset

4. Malware Analysis

5. Response Recommendation

6. Final Decision

Be concise.

Do not repeat information.
                        """,
                    ),
                    (
                        "human",
                        f"""
Original Security Log

{message}

Log Agent

{log_analysis}

Threat Agent

{threat_analysis}

Malware Agent

{malware_analysis}

Severity

{severity}

Response Recommendation

{response_analysis}
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
                # ============================================
    # STEP 7 : BUILD FINAL REPORT
    # ============================================

    final_report = f"""
============================================================
              MULTI-AGENT SOC REPORT
============================================================

====================================
📝 LOG AGENT
====================================

{log_analysis}


====================================
🛡️ THREAT AGENT
====================================

{threat_analysis}


====================================
🦠 MALWARE AGENT
====================================

{malware_analysis}


====================================
🚨 RESPONSE AGENT
====================================

{response_analysis}


====================================
🚦 SEVERITY AGENT
====================================

{severity}


====================================
🤖 COORDINATOR AGENT
====================================

{ai_response}
"""

    # ============================================
    # STEP 8 : SAVE REPORT
    # ============================================

    report_path = save_report(final_report)
        # ============================================
    # STEP 9 : APPEND REPORT STATUS
    # ============================================

    final_report += f"""

====================================
📁 REPORT STATUS
====================================

✅ SOC Report saved successfully.

Report Location:

{report_path}

====================================
END OF REPORT
====================================
"""

    # ============================================
    # STEP 10 : RETURN REPORT
    # ============================================

    return final_report