import fastapi as _fastapi
import fastapi.security as _security
import datetime as _datetime

import create 
import read 
import update
import delete

import auth

app = _fastapi.FastAPI()


@app.get("/")
async def root(token : str = _fastapi.Depends(auth.oauth2_scheme)):
    return auth.ALGORITHM(token=token)


@app.post("/signup", response_model=dict)
async def signup(
    name: str = _fastapi.Form(...),
    email: str = _fastapi.Form(...),
    password: str = _fastapi.Form(...),
):
    return create.user(name=name, email=email, password=password)
# ?hello
@app.post("/token")
def login(form_data : _security.OAuth2PasswordRequestForm = _fastapi.Depends()):
    email = form_data.username
    password = form_data.password

    if auth.user_auth(email, password):
        access_token = auth.generate(
            data = {"sub":email}, expires_delta = _datetime.timedelta(minutes=30)
        )
        return {"access_token" : access_token, "token_type": "bearer"}
    else:
        raise _fastapi.HTTPException(status_code=400, detail="Incorrect email or password")
 

@app.get("/UID/{email}")
async def get_UID(email : str, token : str = _fastapi.Depends(auth.oauth2_scheme) ):
    return read.UID(email=email)

@app.post("/task/create", response_model= dict)
async def create_task(
    UID: str = _fastapi.Form(...),
    name : str = _fastapi.Form(...),
    description : str = _fastapi.Form(None),
    due : str = _fastapi.Form(None),
    token : str = _fastapi.Depends(auth.oauth2_scheme)
):
    return create.task(UID=UID, name=name, description=description, due=due)

@app.get("/task/all/{UID}")
async def get_task_all(UID : str, token : str = _fastapi.Depends(auth.oauth2_scheme)):
    return read.alltask(UID)

@app.delete("/task/delete/{TID}")
async def delete_task(TID : str, token : str = _fastapi.Depends(auth.oauth2_scheme)):
    return delete.task(TID)


@app.put("/task/update/", response_model=dict)
async def update_task(
    UID: str = _fastapi.Form(...),
    name : str = _fastapi.Form(...),
    description : str = _fastapi.Form(...),
    due : str = _fastapi.Form(...),
    token : str = _fastapi.Depends(auth.oauth2_scheme)
):
    return update.task(UID=UID, name=name, description=description, due=due)




