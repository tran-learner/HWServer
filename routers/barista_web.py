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
    Sugar: int
    Coffee: int
    Milk: int
    Tea: int

@barista_web_router.post('/pumphandle')
async def pump_handle(data: PumpData):
    print("Received:")
    print(f"Sugar: {data.Sugar}")
    print(f"Coffee: {data.Coffee}")
    print(f"Milk: {data.Milk}")
    print(f"Tea: {data.Tea}")

    
    run_pumps(data.Coffee, data.Milk, data.Tea, data.Sugar)

    return {"status": "success"}