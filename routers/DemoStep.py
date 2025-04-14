import RPi.GPIO as gpio
import time
import threading

# Khai báo các chân GPIO
step_enpin = [23, 25, 7, 12]
step_dirpin = [24, 8, 1, 16]

gpio.setmode(gpio.BCM)
for a in range(len(step_enpin)):
    gpio.setup(step_enpin[a], gpio.OUT)
    gpio.setup(step_dirpin[a], gpio.OUT)
    gpio.output(step_dirpin[a], 0)

def run_step(pin, dir, steps, dutycycle=50):
    try:
        for step in range(steps):
            gpio.output(step_dirpin[pin], dir)
            gpio.output(step_enpin[pin], gpio.HIGH)
            time.sleep(0.001 * dutycycle / 100)
            gpio.output(step_enpin[pin], gpio.LOW)
            time.sleep(0.001 * (100 - dutycycle) / 100)
    finally:
        gpio.output(step_enpin[pin], gpio.LOW)

def run_pumps(coffee: int, sugar: int):
    # Tạo và chạy các thread để điều khiển bơm
    thread1 = threading.Thread(target=run_step, args=(0, 1, coffee * 10))
    thread2 = threading.Thread(target=run_step, args=(1, 1, sugar * 10))
    thread3 = threading.Thread(target=run_step, args=(2, 1, 30))
    thread4 = threading.Thread(target=run_step, args=(3, 1, 40))

    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()

    # Đợi tất cả thread hoàn thành
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()

    # Clean up sau khi chạy xong
    gpio.cleanup()