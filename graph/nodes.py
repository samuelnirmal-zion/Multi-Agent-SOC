from graph.state import SOCState

from agents.log_agent import analyze_log
from agents.threat_agent import analyze_threat
from agents.malware_agent import analyze_malware
from agents.severity_agent import analyze_severity
from agents.response_agent import response_action
from reports.report_generator import save_report

import os
from dotenv import load_dotenv

try:
    from langchain_groq import ChatGroq
except ImportError:
    ChatGroq = None


load_dotenv()



# ============================================
# LOG NODE
# ============================================

def log_node(state: SOCState):
    """
    LangGraph Node - Log Analysis
    """

    log = state["log"]

    result = analyze_log(log)

    state["log_analysis"] = result

    return state



# ============================================
# THREAT NODE
# ============================================

def threat_node(state: SOCState):
    """
    LangGraph Node - Threat Analysis
    """

    log = state["log"]

    result = analyze_threat(log)

    state["threat"] = result

    return state



# ============================================
# MALWARE NODE
# ============================================

def malware_node(state: SOCState):
    """
    LangGraph Node - Malware Analysis
    """

    log = state["log"]

    result = analyze_malware(log)

    state["malware"] = result

    return state



# ============================================
# SEVERITY NODE
# ============================================

def severity_node(state: SOCState):
    """
    LangGraph Node - Severity Analysis
    """

    log = state["log"]

    result = analyze_severity(log)

    state["severity"] = result

    return state



# ============================================
# RESPONSE NODE
# ============================================

def response_node(state: SOCState):
    """
    LangGraph Node - Response Generation
    """

    threat_result = state["threat"]

    result = response_action(threat_result)

    state["response"] = result

    return state



# ============================================
# COORDINATOR AI NODE
# ============================================

def coordinator_node(state: SOCState):
    """
    LangGraph Node - Coordinator AI
    """

    api_key = os.getenv("GROQ_API_KEY")


    if not api_key or ChatGroq is None:

        state["coordinator"] = (
            "Coordinator AI running in offline mode."
        )

        return state



    model = ChatGroq(
        model="llama-3.3-70b-versatile",
        api_key=api_key
    )


    try:

        response = model.invoke(
            [
                (
                    "system",
                    """
You are the Coordinator Agent of a Multi-Agent Security Operations Center.

Create a professional SOC incident report.

Include:

1. Incident Summary

2. Threat Level

3. Malware Analysis

4. Response Recommendation

5. Final Decision

Keep it concise and professional.
"""
                ),

                (
                    "human",
                    f"""
Security Log:

{state.get("log")}


Log Analysis:

{state.get("log_analysis")}


Threat Analysis:

{state.get("threat")}


Malware Analysis:

{state.get("malware", "Not performed")}


Severity:

{state.get("severity", "Not calculated")}


Response:

{state.get("response", "Not generated")}
"""
                )
            ]
        )


        state["coordinator"] = (
            response.content
            if hasattr(response, "content")
            else str(response)
        )


    except Exception as e:

        state["coordinator"] = (
            f"Coordinator AI Error: {str(e)}"
        )


    return state



# ============================================
# REPORT NODE
# ============================================

def report_node(state: SOCState):
    """
    LangGraph Node - Report Generation
    """


    report = f"""
===========================
SOC INCIDENT REPORT
===========================


Original Log:

{state.get("log") or "N/A"}



--------------------------------
Log Analysis:

{state.get("log_analysis") or "N/A"}



--------------------------------
Threat Analysis:

{state.get("threat") or "N/A"}



--------------------------------
Malware Analysis:

{state.get("malware") or "No malware analysis required."}



--------------------------------
Severity:

{state.get("severity") or "🟢 Low"}



--------------------------------
Recommended Response:

{state.get("response") or "No immediate action required."}



--------------------------------
Coordinator AI Report:

{state.get("coordinator") or "Coordinator AI analysis not required for this event."}



--------------------------------
Report Status:

SOC report generated successfully.

"""



    filepath = save_report(report)



    state["report"] = report

    state["report_path"] = filepath



    return state