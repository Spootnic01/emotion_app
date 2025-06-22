from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from app.emotion import analyze_emotions
from app.lia import analyze_lia

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
async def form_get(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/", response_class=HTMLResponse)
async def form_post(request: Request, text: str = Form(...)):
    emotions = analyze_emotions(text)
    lia = analyze_lia(text)

    return templates.TemplateResponse("index.html", {
        "request": request,
        "text": text,
        "emotions": emotions,
        "lia": lia
    })
