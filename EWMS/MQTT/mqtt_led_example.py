import paho.mqtt.publish as publish
import time
print("Sending 0...")
publish.single("debug", "0", hostname="10.0.0.129")
print("Sending 1...")
publish.single("debug", "1", hostname="10.0.0.129")
