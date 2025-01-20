import RPi.GPIO as GPIO
import time

# GPIO ustawienia
AIN1 = 23  # Kierunek 1
AIN2 = 24  # Kierunek 2
PWMA = 12  # PWM
STBY = 25  # Standby

GPIO.setmode(GPIO.BCM)
GPIO.setup(AIN1, GPIO.OUT)
GPIO.setup(AIN2, GPIO.OUT)
GPIO.setup(PWMA, GPIO.OUT)
GPIO.setup(STBY, GPIO.OUT)

# PWM konfiguracja
pwm = GPIO.PWM(PWMA, 100)  # 100 Hz
pwm.start(0)

# Funkcja sterująca
def test_motor(speed, direction):
    GPIO.output(STBY, GPIO.HIGH)  # Włącz moduł
    if direction == "forward":
        GPIO.output(AIN1, GPIO.HIGH)
        GPIO.output(AIN2, GPIO.LOW)
    elif direction == "backward":
        GPIO.output(AIN1, GPIO.LOW)
        GPIO.output(AIN2, GPIO.HIGH)
    pwm.ChangeDutyCycle(speed)  # Ustaw prędkość

# Test
try:
    test_motor(50, "forward")  # 50% prędkości w przód
    time.sleep(3)
    test_motor(50, "backward")  # 50% prędkości w tył
    time.sleep(3)
finally:
    pwm.ChangeDutyCycle(0)  # Zatrzymaj PWM
    pwm.stop()              # Zatrzymaj sygnał PWM
    GPIO.output(STBY, GPIO.LOW)  # Wyłącz TB6612FNG
    GPIO.cleanup()          # Zwolnij GPIO

