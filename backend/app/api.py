from urllib import request
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from pathlib import Path
from databases.database import login_col


app = FastAPI()
cur_path=Path(__file__).resolve().parent.parent.parent
templates=Jinja2Templates(directory=cur_path/"frontend/templates")

@app.get("/")
async def load(request: Request):
    return templates.TemplateResponse(request= request, name="login.html")

@app.post("/submit")
async def login(request: Request, nm: str = Form(...), pwd: str = Form(...)):
    if login_col.find_one({"name":nm, "password": pwd}):
        return templates.TemplateResponse(request=request,name="submit.html")
    else:
        return {"status":"Login Failed"}