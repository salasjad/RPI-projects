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
    #average = reduce(lambda x, y: x + y, r_sensor)/len(r_sensor)
    average = sum(r_sensor)/len(r_sensor) if len(r_sensor) > 0 else 0
    return average

try:   
    GPIO.setup(TRIG1, GPIO.OUT)
    #GPIO.setup(TRIG2, GPIO.OUT)
    GPIO.setup(ECHO1, GPIO.IN)
    #GPIO.setup(ECHO2, GPIO.IN)

    #GPIO.output(TRIG1, False)
    #GPIO.output(TRIG2, Flase)
    print ("Venter paa sensorene")
    #time.sleep(1)
   

    prev_average = 0
    r_sensor1 = collections.deque(maxlen=10)
    r_sensor2 = collections.deque(maxlen=10)

    while True: 

	print(len(r_sensor1))
        GPIO.output(TRIG1, True)
        #GPIO.output(TRIG2, True)
        time.sleep(0.00001)
        GPIO.output(TRIG1, False)
        #GPIO.output(TRIG2, False)
        
        while GPIO.input(ECHO1)== 0:
            pulse_start1 = time.time()
            
        while GPIO.input(ECHO1)==1:
            pulse_end1 = time.time()
        
        '''while GPIO.input(ECHO2)== 0:
            pulse_start2 = time.time()
            
        while GPIO.input(ECHO2)==1:
            pulse_end2 = time.time()
        '''
        try:
                pulse_duration1 = pulse_end1 - pulse_start1
                #pulse_duration2 = pulse_end2 - pulse_start2
        except NameError:
                pulse_duration1 = 0
                #pulse_duration2 = 0

        distance1 = pulse_duration1 * 17150
        distance1 = round(distance1, 2)
        
        '''distance2 = pulse_duration2 * 17150
        distance2 = round(distance2, 2) '''
      
        #print("Distance1: " + distance1)

        r_sensor1.append(distance1)
        #r_sensor2.append(distance2)
        average1 = sensor_average(r_sensor1)
        #average2 = sensor_average(r_sensor2)
        average2 = 0 #FIXME fjern senere
        average = max(average1, average2)

        if average != prev_average:
            send_update(average)
            prev_average = average
        
        time.sleep(2)

except KeyboardInterrupt:
    GPIO.cleanup()

