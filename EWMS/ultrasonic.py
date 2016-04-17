try:
    import RPi.GPIO as GPIO
    import paho.mqtt.publish as publish
    import time
    GPIO.setmode(GPIO.BCM)
    
    TRIG = 23
    ECHO = 24
    
    print ("Distance Measurement In Progress")
    
    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)

    #GPIO.output(TRIG, False)
    print ("Waiting for sensor")
    #time.sleep(1)
    
    while True:
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
        print ("Distance:" , distance, " cm")
        publish.single("ewms", distance, hostname="10.0.0.129")
        
        time.sleep(2)

except KeyboardInterrupt:
    GPIO.cleanup()
