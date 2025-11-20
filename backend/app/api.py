from fastapi import FastAPI
from fastapi.responses import FileResponse,Jinja2Templates


app = FastAPI()
@app.get("/")
async def login():
    return FileResponse("login.html")
