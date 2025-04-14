from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from routers.barista_web import barista_web_router
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "https://baristaweb.onrender.com/drinks"
    ],  # Only accept request from this address
    allow_credentials=True,
    allow_methods=["*"],  # accept all methods
    allow_headers=["*"],  # accept all headers
)

allow_origins=["http://localhost:3000"]
@app.get("/")
async def welcome():
    return "Server is running at"
app.include_router(barista_web_router)