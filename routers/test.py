import RPi.GPIO as GPIO
import time

# Define the GPIO pins you want to use
pin1 = 17
pin2 = 18
pin3 = 27
pin4 = 22

# Set the GPIO mode to BCM numbering
GPIO.setmode(GPIO.BCM)

# Set the pins as outputs
GPIO.setup(pin1, GPIO.OUT)
GPIO.setup(pin2, GPIO.OUT)
GPIO.setup(pin3, GPIO.OUT)
GPIO.setup(pin4, GPIO.OUT)

def generate_pulse(pin, duration_high, duration_low):
    """Generates a single pulse on the specified pin."""
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(duration_high)
    GPIO.output(pin, GPIO.LOW)
    time.sleep(duration_low)

if __name__ == "__main__":
    try:
        # Example: Generate different pulses on each pin
        print("Generating pulses...")
        generate_pulse(pin1, 0.01, 0.02)  # Pin 1: High for 10ms, Low for 20ms
        generate_pulse(pin2, 0.005, 0.015) # Pin 2: High for 5ms, Low for 15ms
        generate_pulse(pin3, 0.02, 0.008)  # Pin 3: High for 20ms, Low for 8ms
        generate_pulse(pin4, 0.012, 0.012) # Pin 4: High for 12ms, Low for 12ms
        print("Pulses generated.")

        # You can create loops or more complex logic to generate sequences of pulses
        # independently on each pin.
        for _ in range(5): # Example: Generate 5 pulses on each pin
            generate_pulse(pin1, 0.01, 0.02)
            generate_pulse(pin2, 0.005, 0.015)
            generate_pulse(pin3, 0.02, 0.008)
            generate_pulse(pin4, 0.012, 0.012)
            time.sleep(0.5) # Wait a bit between sets of pulses

    except KeyboardInterrupt:
        print("Program interrupted.")
    finally:
        GPIO.cleanup() # Clean up GPIO settings