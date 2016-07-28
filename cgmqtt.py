import os
from flask import Flask
from flask import request
import re
import paho.mqtt.client as mqtt
import time

global foundColours
global colorList
global mqttConnected
mqttConnected=False

topicName="/CG/colors"
app = Flask(__name__)
def findHashTag(w):
    return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search
	
def on_connect(client, userdata, flags, rc):
	print("Connected with result code "+str(rc))
	#mqttConnected=True
	
	

	

@app.route("/", methods=["GET"])	
def cgmqtt():
	
	client = mqtt.Client()
	client.on_connect = on_connect	
	client.connect("iot.eclipse.org", 1883, 60)
	client.loop_start()
	
	#data=str(request.data)
	data="Hi I Like this Lamp #red #blue #green"
	#print (data)
	
	foundColours=""
	matchobj= findHashTag('violet')(data)
	if matchobj:
		foundColours=foundColours+"violet: "			

	matchobj= findHashTag('indigo')(data)
	if matchobj:
		foundColours=foundColours+"indigo: "

	matchobj= findHashTag('blue')(data)
	if matchobj:
		foundColours=foundColours+"blue: "

	matchobj= findHashTag('green')(data)
	if matchobj:
		foundColours=foundColours+"green: "

	matchobj= findHashTag('yellow')(data)
	if matchobj:
		foundColours=foundColours+"yellow: "

	matchobj= findHashTag('orange')(data)
	if matchobj:
		foundColours=foundColours+"orange: "

	matchobj= findHashTag('red')(data)
	if matchobj:
		foundColours=foundColours+"red: "	
		
	#return ("foundColours: "+foundColours)
	
	
	
	client.publish(topicName, foundColours)
	client.loop_stop()
	#return ("Published")
	return ""
	
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port,debug=True)
	


