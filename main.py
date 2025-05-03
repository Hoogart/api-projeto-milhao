from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.routers import sugestoes
from fastapi.responses import HTMLResponse

app = FastAPI(title="API Apostas Inteligente")

app.include_router(sugestoes.router, prefix="/sugestoes", tags=["Sugestoes"])

app.mount("/static", StaticFiles(directory="frontend/static"), name="static")
templates = Jinja2Templates(directory="frontend/templates")

@app.get("/web", response_class=HTMLResponse)
async def dashboard(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})