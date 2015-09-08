# !/usr/bin/env python
# -*- coding: utf-8 -*- 
 
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import time
from itertools import count

def reply():
	global count
	publish_mqtt('I heard you!')
	count = 0

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
	print("Connected with result code "+str(rc))
	# Subscribing in on_connect() means that if we lose the connection and
	# reconnect then subscriptions will be renewed.
	client.subscribe("uicomm/j-p")
 
# The callback for when a message is received from the server.
def on_message(client, userdata, msg):
	print("recieved: "+msg.topic+" "+str(msg.payload))
	words = msg.payload.split()
	if words[0] == 'run': #  If 'run' is the first word of the message
		globals()[words[1]]() #  Run the function named by the second word in the message
	
def publish_mqtt(payload):
    """
    Send an MQTT mesage to javaScript client
    """
    topic = 'uicomm/p-j'
    try:
        publish.single(topic, payload, hostname='127.0.0.1', port=1883, retain=False, qos=0)
    except Exception as err:
            print "Couldn't publish :" + str(err)
            pass	
	 
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("127.0.0.1")
 
#Start Loop
client.loop_start()

count = 0
try:
	while True:
		publish_mqtt("message number: " + str(count) )
		count += 1
		time.sleep(2)
except Exception as err:
    print 'Error: ', err
finally:
	print ''
	print 'Cleaning up'
	client.loop_stop()
    # GPIO.cleanup() anyone?