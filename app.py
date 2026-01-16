from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "title": "LogHaven"
        }
    )


@app.get("/changelog", response_class=HTMLResponse)
async def changelog(request: Request):
    changes = [
        {
            "version": "1.0",
            "date": "16-01-2026",
            "items": ["Version 1.0!\n\nVelkommen til :-)"]
        }
    ]

    return templates.TemplateResponse(
        "changelog.html",
        {
            "request": request,
            "title": "Changelog",
            "changes": changes
        }
    )
