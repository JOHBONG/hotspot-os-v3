from fastapi import FastAPI

app = FastAPI(title="HotspotOS V3 API")

@app.get("/")
def read_root():
    return {"msg": "Welcome to HotspotOS V3 API"}
