from fastapi import APIRouter, Form, Request
from fastapi.templating import Jinja2Templates

from app.services.analyzer import IncidentAnalyzer

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

analyzer = IncidentAnalyzer()


@router.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "result": None,
            "title": "",
            "logs": "",
        },
    )


@router.post("/")
def analyze(
    request: Request,
    incident_title: str = Form(...),
    logs: str = Form(...),
):
    result = analyzer.analyze(incident_title, logs)

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "result": result,
            "title": incident_title,
            "logs": logs,
        },
    )