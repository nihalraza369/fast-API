1.[tool.poetry]
name = "fastapi_classes"
version = "0.1.0"
description = ""
authors = ["nihalraza369 <nihalraza369@gmail.com>"]
readme = "README.md"

2.[tool.poetry.dependencies]
python = "^3.12"
fastapi = "^0.115.5"
uvicorn = {extras = ["standerd"], version = "^0.32.0"}



3.[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"


4.install new packages in poetry project
  `poetry add fastapi`
  `poetry add uvicorn["standerd"]`
create `main.py` location `FASTAPI` 

5.Create `HELLO WORLD`
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return("hello : world")

@app.get("/9270")
def piaic():
    return {"sory app nhi hn":"nihal raza"}

`run services `
(fastapi-py3.12) C:\Users\asdf\OneDrive\Desktop\fast-api\fastapi>`poetry run uvicorn 01_class.main:app --port 8000 `
INFO:     Started server process [6332]
INFO:     Waiting for application startup.`
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     127.0.0.1:53863 - "GET / HTTP/1.1" 200 OK
INFO:     127.0.0.1:53863 - "GET /favicon.ico HTTP/1.1" 404 Not Found

