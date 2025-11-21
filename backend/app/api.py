from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from pathlib import Path
from databases.database import login_col
from fastapi.staticfiles import StaticFiles


app = FastAPI()
root_path=Path(__file__).resolve().parent.parent.parent
app.mount("/static", StaticFiles(directory=root_path/"frontend/static"), name="static")
templates=Jinja2Templates(directory=root_path/"frontend/templates")

@app.get("/")
async def load(request: Request):
    return templates.TemplateResponse(request= request, name="login.html")

@app.post("/submit")
async def login(request: Request, nm: str = Form(...), pwd: str = Form(...)):
    if login_col.find_one({"name":nm, "password": pwd}):
        return templates.TemplateResponse(request=request,name="submit.html")
    else:
        return {"status":"Login Failed"}

@app.get("/register")
async def register (request: Request):
    return templates.TemplateResponse(request= request, name="register.html")

@app.post("/do-register")
async def do_register(request: Request, nm: str = Form(...), pwd: str = Form(...), confirm_pwd: str = Form(...)):
    if login_col.find_one({"name":nm}):
        return {"status":"Username da ton tai"}
    elif pwd != confirm_pwd:
        return {"status":"Password and Confirm Password khong giong nhau"}
    else:
        login_col.insert_one({"name":nm, "password": pwd})
    return templates.TemplateResponse(request=request,name="login.html")