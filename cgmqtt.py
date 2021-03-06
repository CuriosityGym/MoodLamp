import os, sys
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
	
	

	

@app.route("/", methods=["POST"])	
def cgmqtt():
	
	client = mqtt.Client()
	client.on_connect = on_connect	
	client.connect("iot.eclipse.org", 1883, 60)
	client.loop_start()
	response=""
	tweetcontent=request.data
	#data="Hi I Like this Lamp #red#blue#green"
	sys.stdout.write(tweetcontent)
	#response=response+data+"<br>"
	foundColours=""
	matchobj= findHashTag('violet')(tweetcontent)
	if matchobj:
		foundColours=foundColours+"violet: "
		client.publish(topicName+"/violet", True)		

	matchobj= findHashTag('indigo')(tweetcontent)
	if matchobj:
		foundColours=foundColours+"indigo: "
		client.publish(topicName+"/indigo", True)

	matchobj= findHashTag('blue')(tweetcontent)
	if matchobj:
		foundColours=foundColours+"blue: "
		client.publish(topicName+"/blue", True)

	matchobj= findHashTag('green')(tweetcontent)
	if matchobj:
		foundColours=foundColours+"green: "
		client.publish(topicName+"/green", True)

	matchobj= findHashTag('yellow')(tweetcontent)
	if matchobj:
		foundColours=foundColours+"yellow: "
		client.publish(topicName+"/yellow", True)

	matchobj= findHashTag('orange')(tweetcontent)
	if matchobj:
		foundColours=foundColours+"orange: "
		client.publish(topicName+"/orange", True)

	matchobj= findHashTag('red')(tweetcontent)
	if matchobj:
		foundColours=foundColours+"red: "	
		client.publish(topicName+"/red", True)
		
	sys.stdout.write("Colours are: "+foundColours + "\n")	
	return (str(0))
	
	
	
	#client.publish(topicName, foundColours)
	client.loop_stop()
	#return ("Published")
	return ""
	
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port,debug=True)
	


