from langgraph.graph import StateGraph, START, END

from graph.state import SOCState

from graph.nodes import (
    log_node,
    threat_node,
    malware_node,
    severity_node,
    response_node,
    coordinator_node,
    report_node,
)


# -----------------------------------
# Conditional Router
# -----------------------------------

def threat_router(state: SOCState):

    threat = state["threat"].lower()


    if (
        "no known threat" in threat
        or "no threat" in threat
        or "no suspicious" in threat
    ):

        return "report"


    else:

        return "malware"



# Create workflow

workflow = StateGraph(SOCState)



# Add nodes

workflow.add_node("log", log_node)

workflow.add_node("threat", threat_node)

workflow.add_node("malware", malware_node)

workflow.add_node("severity", severity_node)

workflow.add_node("response", response_node)

workflow.add_node("coordinator", coordinator_node)

workflow.add_node("report", report_node)



# Starting point

workflow.add_edge(
    START,
    "log"
)



# Normal flow

workflow.add_edge(
    "log",
    "threat"
)



# Conditional routing

workflow.add_conditional_edges(
    "threat",
    threat_router,
    {
        "malware": "malware",
        "report": "report"
    }
)



# Threat detected path

workflow.add_edge(
    "malware",
    "severity"
)


workflow.add_edge(
    "severity",
    "response"
)


workflow.add_edge(
    "response",
    "coordinator"
)



workflow.add_edge(
    "coordinator",
    "report"
)



# End

workflow.add_edge(
    "report",
    END
)



# Compile

graph = workflow.compile()



# Generate visualization

try:

    png = graph.get_graph().draw_mermaid_png()

    with open(
        "soc_langgraph_workflow.png",
        "wb"
    ) as file:

        file.write(png)


    print(
        "LangGraph workflow diagram created successfully."
    )


except Exception as e:

    print(
        "Visualization error:",
        e
    )