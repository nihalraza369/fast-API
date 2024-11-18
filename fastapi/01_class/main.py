from fastapi import FastAPI

app = FastAPI()
@app.get("/")
def index():
    return("hello : world")

@app.get("/9270")
def piaic():
    return {"sory app nhi hn":"nihal raza"}