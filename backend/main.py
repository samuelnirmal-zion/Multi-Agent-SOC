from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from agents.coordinator import coordinator

app = FastAPI(title="Multi-Agent SOC")

templates = Jinja2Templates(directory="frontend")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request,
        "index.html",
        {"response": ""},
    )


@app.post("/", response_class=HTMLResponse)
async def analyze(request: Request, security_log: str = Form(...)):
    response = coordinator(security_log)
    return templates.TemplateResponse(
        request,
        "index.html",
        {"response": response},
    )
