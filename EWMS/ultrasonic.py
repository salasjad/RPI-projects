import RPi.GPIO as GPIO
import paho.mqtt.publish as publish
import time
import collections
import math

GPIO.setmode(GPIO.BCM)
    
TOPIC = "ewms/1"
HOSTNAME = "10.0.0.129"

#ULTRASONIC
TRIG1 = 23 #gul
ECHO1 = 24 #gronn
TRIG2 = 20 #oransje
ECHO2 = 21 #brun

#RGB
RED = 17
GREEN = 18
BLUE = 27

def color(B, G, R): #R,G,B
    RED_C.ChangeDutyCycle(R) 
    GREEN_C.ChangeDutyCycle(G) 
    BLUE_C.ChangeDutyCycle(B) 
 
def send_update(message):
    print("Updated server with average:", message)
    publish.single(TOPIC, message, hostname=HOSTNAME)

def sensor_average(r_sensor):
    average = sum(r_sensor)/len(r_sensor) if len(r_sensor) > 0 else 0
    return average

def gpio_output(TRIG, ECHO):
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO)== 0:
        pulse_start = time.time()
		    
    while GPIO.input(ECHO)==1:
        pulse_end = time.time()

    try:
        pulse_duration = pulse_end - pulse_start
    except NameError:
        pulse_duration = 0

    distance = pulse_duration * 17150
    distance = round(distance, 2)
    return distance

try:   
    GPIO.setup(RED, GPIO.OUT)
    GPIO.setup(GREEN, GPIO.OUT)
    GPIO.setup(BLUE, GPIO.OUT)
    GPIO.setup(TRIG1, GPIO.OUT)
    GPIO.setup(TRIG2, GPIO.OUT)
    GPIO.setup(ECHO1, GPIO.IN)
    GPIO.setup(ECHO2, GPIO.IN)

    #initialize the RGB to off
    RED_C = GPIO.PWM(RED, 100)
    RED_C.start(0)
    GREEN_C = GPIO.PWM(GREEN, 100)
    GREEN_C.start(0)
    BLUE_C = GPIO.PWM(BLUE, 100)
    BLUE_C.start(0)

    GPIO.output(TRIG1, False)
    GPIO.output(TRIG2, False)
    print ("Venter paa sensorene")
    time.sleep(1)
   
    prev_average = 0
    r_sensor1 = collections.deque(maxlen=10)
    r_sensor2 = collections.deque(maxlen=10)

    while True: 
	distance1 = gpio_output(TRIG1, ECHO1)
        distance2 = gpio_output(TRIG2, ECHO2)

        r_sensor1.append(distance1)
        r_sensor2.append(distance2)
        average1 = sensor_average(r_sensor1)
        average2 = sensor_average(r_sensor2)
        #average2 = 0 #FIXME fjern senere
        average = int(min(average1, average2))
		
	print "Average1: ",average1
	print "Average2: ",average2
	print "Min average: ",average
	print ""
        if average>(prev_average+10) or average<(prev_average-10):
            send_update(average)
            prev_average = average
            color(100,0,0)
        time.sleep(1)	
	color(20,30,40)

except KeyboardInterrupt:
    GPIO.cleanup()
