from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse

from frontend import render_frontend_page
from graph.runner import run_soc_workflow


def create_app() -> FastAPI:
    app = FastAPI(title="Multi-Agent SOC Assistant")

    # Allow frontend connection
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Store incident history temporarily
    incident_history = []

    def _handle_analysis(security_log: str) -> str:
        try:
            report = run_soc_workflow(security_log)
            return report or "No report was generated."
        except Exception as exc:
            return f"Analysis could not be completed: {exc}"

    @app.get("/", response_class=HTMLResponse)
    def home() -> str:
        return render_frontend_page()

    @app.post("/", response_class=HTMLResponse)
    def analyze_from_home(security_log: str = Form(...)) -> str:
        report = _handle_analysis(security_log)
        incident_history.append({"log": security_log, "report": report})
        return render_frontend_page(result=report, submitted_log=security_log)

    @app.get("/analyze", response_class=HTMLResponse)
    @app.post("/analyze", response_class=HTMLResponse)
    def analyze_log(security_log: str | None = None) -> str:
        if security_log is None:
            return render_frontend_page()
        report = _handle_analysis(security_log)
        incident_history.append({"log": security_log, "report": report})
        return render_frontend_page(result=report, submitted_log=security_log)

    @app.get("/history-page", response_class=HTMLResponse)
    def history_page() -> str:
        with open("frontend/history.html", "r", encoding="utf-8") as file:
            return file.read()

    @app.get("/api/history")
    def api_history() -> dict:
        return {"incidents": incident_history}

    return app


app = create_app()