import RPi.GPIO as GPIO
import time
import threading

# Define the GPIO pins
pin1 = 23
pin2 = 25
pin3 = 7
pin4 = 12

# Set the GPIO mode
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False) # To avoid "channel is already in use" warnings

# Set the pins as outputs
GPIO.setup(pin1, GPIO.OUT)
GPIO.setup(pin2, GPIO.OUT)
GPIO.setup(pin3, GPIO.OUT)
GPIO.setup(pin4, GPIO.OUT)

def generate_independent_pulses(pin, frequency, duration_high_ratio):
    """Generates continuous pulses with specified frequency and high duration ratio."""
    period = 1.0 / frequency
    duration_high = period * duration_high_ratio
    duration_low = period - duration_high
    try:
        while True:
            GPIO.output(pin, GPIO.HIGH)
            time.sleep(duration_high)
            GPIO.output(pin, GPIO.LOW)
            time.sleep(duration_low)
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup(pin) # Clean up individual pin on thread exit

if __name__ == "__main__":
    try:
        # Define the desired frequency and duty cycle (high duration ratio) for each pin
        freq1 = 10  # Hz
        duty1 = 0.3 # 30% high

        freq2 = 5   # Hz
        duty2 = 0.7 # 70% high

        freq3 = 20  # Hz
        duty3 = 0.5 # 50% high

        freq4 = 8   # Hz
        duty4 = 0.2 # 20% high

        # Create and start threads for each pin
        thread1 = threading.Thread(target=generate_independent_pulses, args=(pin1, freq1, duty1))
        thread2 = threading.Thread(target=generate_independent_pulses, args=(pin2, freq2, duty2))
        thread3 = threading.Thread(target=generate_independent_pulses, args=(pin3, freq3, duty3))
        thread4 = threading.Thread(target=generate_independent_pulses, args=(pin4, freq4, duty4))

        thread1.start()
        thread2.start()
        thread3.start()
        thread4.start()

        # Keep the main thread alive to allow the others to run until interrupted
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        print("Program interrupted. Cleaning up...")
    finally:
        GPIO.cleanup() # Clean up all GPIO settings