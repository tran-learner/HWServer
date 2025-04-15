# from fastapi import APIRouter
# from pydantic import BaseModel
# barista_web_router = APIRouter()

# class PumpData(BaseModel):
#     sugar: int
#     coffee: int

# @barista_web_router.post('/pumphandle')
# async def pump_handle(data: PumpData):
#     print("Recieved:")
#     print(f"Sugar: {data.sugar}")
#     print(f"Coffee: {data.coffee}")

from fastapi import APIRouter
from pydantic import BaseModel
from routers.DemoStep import run_pumps

barista_web_router = APIRouter()

class PumpData(BaseModel):
    sugar: int
    coffee: int
    milk: int
    tea: int

@barista_web_router.post('/pumphandle')
async def pump_handle(data: PumpData):
    print("Received:")
    print(f"Sugar: {data.sugar}")
    print(f"Coffee: {data.coffee}")
    print(f"Sugar: {data.milk}")
    print(f"Coffee: {data.sugar}")

    
    run_pumps(data.coffee, data.milk, data.tea, data.sugar)

    return {"status": "success"}