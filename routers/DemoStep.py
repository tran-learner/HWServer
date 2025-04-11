import RPi.GPIO as gpio
import time
import threading
from fastapi import APIRouter
from pydantic import BaseModel
barista_web_router = APIRouter()

class PumpData(BaseModel):
    sugar: int
    coffee: int

@barista_web_router.post('/pumphandle')
async def pump_handle(data: PumpData):
    print("Recieved:")
    print(f"Sugar: {data.sugar}")
    print(f"Coffee: {data.coffee}")
step_enpin = [23,25,7,12]
step_dirpin = [24,8,1,16]

gpio.setmode(gpio.BCM)
for a in range(len(step_enpin)):
    gpio.setup(step_enpin[a], gpio.OUT)
    gpio.setup(step_dirpin[a], gpio.OUT)
    gpio.output(step_dirpin[a],0)

def run_step(pin,dir,times):
    try:
        while True:
            gpio.output(step_dirpin[pin],dir)
            gpio.output(step_enpin[pin],gpio.HIGH)
            time.sleep(times*98/100)
            gpio.output(step_enpin[pin],gpio.LOW)
            time.sleep(times*2/100)
    except KeyboardInterrupt:
        print("Dmm dang chay, bam bam cai quan que ne he")
    finally:
        gpio.cleanup(pin) # Clean up individual pin on thread exit

if __name__ == "__main__":
    try:
        # Create and start threads for each pin
        thread1 = threading.Thread(target=run_step, args=(0,1,0.0000005))
        thread2 = threading.Thread(target=run_step, args=(1,1,2))
        thread3 = threading.Thread(target=run_step, args=(2,1,3))
        thread4 = threading.Thread(target=run_step, args=(3,1,4))

        thread1.start()
        thread2.start()
        thread3.start()
        thread4.start()

        while True:
            time.sleep(1)
        
    except KeyboardInterrupt:
        gpio.cleanup()