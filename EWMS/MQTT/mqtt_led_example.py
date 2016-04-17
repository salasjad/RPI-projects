import paho.mqtt.publish as publish
import time
print("Sender verdi 0...")
publish.single("ewms", "0", hostname="10.0.0.129")
print("Sender verdi 1...")
publish.single("ewms", "1", hostname="10.0.0.129")
