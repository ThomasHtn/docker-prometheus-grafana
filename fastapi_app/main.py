from fastapi import FastAPI, Form
from loguru import logger

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World from FastAPI"}


@app.post("/data")
async def receive_color(data: str = Form(...)):
    logger.info(f"Received data: {data}")
    return {"message": f"data {data} received"}


@app.get("/metrics")
async def metrics():
    return "toto"


@app.get("/health")
async def health():
    return {"status": "ok"}
