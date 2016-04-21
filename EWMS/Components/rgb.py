import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

RED = 17
GREEN = 18
BLUE = 27

GPIO.setup(RED, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)
GPIO.setup(BLUE, GPIO.OUT)

Freq = 100 #Hz

RED_C = GPIO.PWM(RED, Freq)
RED_C.start(0)
GREEN_C = GPIO.PWM(GREEN, Freq)
GREEN_C.start(0)
BLUE_C = GPIO.PWM(BLUE, Freq)
BLUE_C.start(0)

def color(R, G, B, on_time):
    RED_C.ChangeDutyCycle(R)
    GREEN_C.ChangeDutyCycle(G)
    BLUE_C.ChangeDutyCycle(B)
    time.sleep(on_time)

    RED_C.ChangeDutyCycle(0)
    GREEN_C.ChangeDutyCycle(0)
    BLUE_C.ChangeDutyCycle(0)

try:
    color(50, 10, 40, 0.1)

finally:
    GPIO.cleanup()


