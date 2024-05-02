import fastapi as _fastapi
import create 
import read 
import update
import delete

app = _fastapi.FastAPI()


@app.get("/")
async def root():
    return {"Welecome":"user"}

@app.post("/signup", response_model=dict)
async def signup(
    name: str = _fastapi.Form(...),
    email: str = _fastapi.Form(...),
    password: str = _fastapi.Form(...),
):
    return create.user(name=name, email=email, password=password)

@app.get("/UID/{email}")
async def get_UID(email : str ):
    return read.UID(email=email)

@app.post("/task/create", response_model= dict)
async def create_task(
    UID: str = _fastapi.Form(...),
    name : str = _fastapi.Form(...),
    description : str = _fastapi.Form(None),
    due : str = _fastapi.Form(None),
):
    return create.task(UID=UID, name=name, description=description, due=due)

@app.get("/task/all/{UID}")
async def get_task_all(UID : str):
    return read.alltask(UID)

@app.delete("/task/delete/{TID}")
async def delete_task(TID : str):
    return delete.task(TID)




