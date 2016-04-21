Testing inside bash:

For the subscriber:
mosquitto_sub -h 127.0.0.1 -i testSub -t debug

For the publisher:
mosquitto_pub -h 127.0.0.1 -i testPublish -t debug -m 'wohooooo'

