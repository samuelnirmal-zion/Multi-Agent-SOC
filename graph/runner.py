from graph.workflow import graph


def run_soc_workflow(log: str):
    """
    Runs the LangGraph workflow.
    """

    initial_state = {
        "log": log,
        "log_analysis": "",
        "threat": "",
        "malware": "",
        "severity": "",
        "response": "",
        "report": "",
        "report_path": "",
    }

    final_state = graph.invoke(initial_state)

    return final_state["report"]