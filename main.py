from fastapi import FastAPI
from Parte1.routes.llms import gpt2_router

app = FastAPI()

@app.get("/")
def read_root():
    return {"message":"This is an API for LLMs"}

app.include_router(gpt2_router)