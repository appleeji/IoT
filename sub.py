import paho.mqtt.client as mqtt

def on_connect(client, userdata, rc):
    client.subscribe("controller")
 
def on_message(client, userdata, msg):
	if msg.topic == "controller":
		if msg.payload == "Start":
			print("Start air conditioning")
		elif msg.payload == "Stop":
			print("Stop air conditioning")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# YOU NEED TO CHANGE THE IP ADDRESS OR HOST NAME
client.connect("192.168.43.125", 1883, 60)
#client.connect("localhost")

try:
    client.loop_forever()
except KeyboardInterrupt:
    print("Finished!")
    client.unsubscribe(["controller"])
    client.disconnect()
