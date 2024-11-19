from fastapi import FastAPI
import uvicorn

app = FastAPI()

student=[{
"name":"nihalraza",
"rollnum":9890849
},
{
    "name":"khurram",
    "rollnum":767878
}
]
@app.get("/student")
def studentall():
    return student

@app.get("/addstudent")
def addstudent(username:str,rollnum:str):
    global student
    student.append({"username":username,"rollnum":rollnum})
    return student

@app.get("/")
def home():
    return "Hello Welcome to the main page"


@app.get("/getuser")
def postuser(name4: str):
    return f"welcome to user page {name4}"

@app.post("/")
def post():
    return f"hello path"


@app.get("/anynum/{id}")
def get8(id):
    print("get  todos call",id)
    return id

@app.get("/get/{username}/{rollnumber}")
def gettodo(username:str,rollnumber:str): 
    print("get todos call",username,rollnumber)
    return username+rollnumber

@app.get("/get7")
def ngjn(username:str,rollnumber:str):
    print("get calling",username,rollnumber)
    return "njbhjbthje"



def start():
    uvicorn.run("learn_fastapi.main:app",host="127.0.0.1",port=7575, reload=True)

#==================================================================== Class 03 ============================================================================