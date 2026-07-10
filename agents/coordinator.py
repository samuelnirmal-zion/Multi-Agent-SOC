import os
from dotenv import load_dotenv

from agents.log_agent import analyze_log
from agents.threat_agent import analyze_threat

load_dotenv()

try:
    from langchain_groq import ChatGroq
except ImportError:
    ChatGroq = None


def _build_fallback_response(message: str) -> str:
    return (
        "SOC Coordinator is running in Offline Mode.\n\n"
        f"Original Log:\n{message}"
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

    if not message or not str(message).strip():
        return "Please provide a security log."

    # =====================================
    # STEP 1 : LOG AGENT
    # =====================================
    log_analysis = analyze_log(message)

    # =====================================
    # STEP 2 : THREAT AGENT
    # =====================================
    threat_analysis = analyze_threat(message)

    # =====================================
    # STEP 3 : COORDINATOR AGENT
    # =====================================

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

You receive outputs from multiple specialized agents.

Create one professional SOC report.

Your report MUST contain these sections:

1. Incident Summary

2. Threat Level

3. Affected Asset

4. Recommended Actions

5. Final Decision

Do not repeat the same information.

Keep the report professional.
                        """,
                    ),
                    (
                        "human",
                        f"""
Original Security Log

{message}


Log Agent Output

{log_analysis}


Threat Agent Output

{threat_analysis}
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

    # =====================================
    # FINAL RESPONSE
    # =====================================

    return f"""
====================================
📝 LOG AGENT
====================================

{log_analysis}


====================================
🛡️ THREAT AGENT
====================================

{threat_analysis}


====================================
🤖 COORDINATOR AGENT
====================================

{ai_response}
"""