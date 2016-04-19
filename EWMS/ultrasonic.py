import RPi.GPIO as GPIO
import paho.mqtt.publish as publish
import time
import collections

GPIO.setmode(GPIO.BCM)
    
TOPIC = "ewms/1"
HOSTNAME = "10.0.0.129"

TRIG1 = 23 #gul
ECHO1 = 24 #gronn
TRIG2 = 20 #oransje
ECHO2 = 21 #brun

def send_update(message):
    print("Distance:", message, " cm")
    publish.single(TOPIC, message, hostname=HOSTNAME)

def sensor_average(r_sensor):
    average = reduce(lambda x, y: x + y, r_sensor)/len(r_sensor)
    return average

try:   
    GPIO.setup(TRIG1, GPIO.OUT)
    GPIO.setup(TRIG2, GPIO.OUT)
    GPIO.setup(ECHO1, GPIO.IN)
    GPIO.setup(ECHO2, GPIO.IN)

    #GPIO.output(TRIG1, False)
    #GPIO.output(TRIG2, Flase)
    print ("Venter paa sensorene")
    #time.sleep(1)
   

    prev_average = 0
    while True: 

        r_sensor1 = collections.deque(maxlen=10)
        r_sensor2 = collections.deque(maxlen=10)

        GPIO.output(TRIG1, True)
        GPIO.output(TRIG2, True)
        time.sleep(0.00001)
        GPIO.output(TRIG1, False)
        GPIO.output(TRIG2, False)
        
        while GPIO.input(ECHO1)== 0:
            pulse_start = time.time()
            
        while GPIO.input(ECHO1)==1:
            pulse_end = time.time()
            
        try:
                pulse_duration = pulse_end - pulse_start
        except NameError:
                pulse_duration = 0

        distance = pulse_duration * 17150
        distance = round(distance, 2)
        
        average1 = sensor_average(r_sensor1)
        average2 = sensor_average(r_sensor2)
        average = max(average1, average2)

        if average != prev_average:
            send_update(average)
            prev_average = average
        
        time.sleep(2)

except KeyboardInterrupt:
    GPIO.cleanup()

