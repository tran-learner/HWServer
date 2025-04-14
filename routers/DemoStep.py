import RPi.GPIO as GPIO
import time
import threading

# Khai báo các chân GPIO
step_enpin = [23, 25, 7, 12]
step_dirpin = [24, 8, 1, 16]



def run_step(pin, dir, steps, dutycycle=100):
    try:
        for step in range(steps):
            GPIO.output(step_dirpin[pin], dir)
            GPIO.output(step_enpin[pin], GPIO.HIGH)
            time.sleep(0.001 * dutycycle / 100)
            GPIO.output(step_enpin[pin], GPIO.LOW)
            time.sleep(0.001 * (100 - dutycycle) / 100)
    finally:
        GPIO.output(step_enpin[pin], GPIO.LOW)

def run_pumps(coffee: int, sugar: int):
    GPIO.setmode(GPIO.BCM)
    for a in range(len(step_enpin)):
        GPIO.setup(step_enpin[a], GPIO.OUT)
        GPIO.setup(step_dirpin[a], GPIO.OUT)
        GPIO.output(step_dirpin[a], 0)
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
    GPIO.cleanup()