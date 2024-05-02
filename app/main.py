import fastapi as _fastapi

app = _fastapi.FastAPI()


@app.get("/")
async def index():
    return {"Welecome":"user"}


