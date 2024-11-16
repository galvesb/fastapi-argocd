from fastapi import FastAPI, HTTPException
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
app = FastAPI()



@app.get("/")
async def hello_world():
    return {"message": "Hello ArgoCD!"}


