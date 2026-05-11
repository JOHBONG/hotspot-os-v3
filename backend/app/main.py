from fastapi import FastAPI
from backend.app.api import routes, auth

app = FastAPI(title="HotspotOS V3 API")

app.include_router(routes.router)
app.include_router(auth.router)

@app.get("/")
def read_root():
    return {"msg": "Welcome to HotspotOS V3 API"}
