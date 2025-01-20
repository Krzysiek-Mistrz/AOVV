import RPi.GPIO as GPIO
import time

# Pin definitions
DIGITAL_PIN = 12
# Connect to D0 pin of TCRT5000

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(DIGITAL_PIN, GPIO.IN)

def main():
    print("TCRT5000 Digital Sensor Test Starting...")
    try:
        while True:
            # Read digital value
            digital_value = GPIO.input(DIGITAL_PIN)

            # Print the value
            if digital_value == 0:
                print("Object detected!")
            else:
                print("No object detected.")

            # Delay for readability
            time.sleep(0.5)
    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    main()
