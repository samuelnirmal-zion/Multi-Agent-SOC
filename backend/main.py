from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from graph.runner import run_soc_workflow

app = FastAPI(title="Multi-Agent SOC")

templates = Jinja2Templates(directory="frontend")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "result": ""
        }
    )


@app.post("/", response_class=HTMLResponse)
async def analyze(request: Request, security_log: str = Form(...)):

    result = run_soc_workflow(security_log)

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "result": result
        }
    )