import paho.mqtt.client as mqtt

#습도 온도 불쾨지수값을 저장하기 위한 전역변수들
humidity = 0.0
temperature = 0.0
value = 0.0

def on_connect(client, userdata, rc):
    client.subscribe("environment/temperature")
    client.subscribe("environment/humidity")

def on_message(client, userdata, msg):
	global humidity
	global temperature
	global value

	if msg.topic == "environment/humidity":
		humidity = float(msg.payload)/100
	elif msg.topic == "environment/temperature":
		temperature = float(msg.payload)
	value = 9*temperature/5 - 0.55*(1 - humidity)*(9*temperature/5 -26) + 32
	if value >= 80:
		print(str(value)+"(Very High)[temperature: "+ str(temperature) + ", humidity: "+str(humidity) )
	elif value >= 75 and value < 80:
		print(str(value)+"(High)[temperature: "+ str(temperature) + ", humidity: "+str(humidity) )
	elif value >= 68 and value < 75:
		print(str(value)+"(Mid)[temperature: "+ str(temperature) + ", humidity: "+str(humidity) )
	elif value < 68:
		print(str(value)+"(Low)[temperature: "+ str(temperature) + ", humidity: "+str(humidity) )

	if value >= 75:
		client.publish("controller","Start")
	elif value < 68:
		client.publish("controller","Stop")
	

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
    client.unsubscribe(["environment/temperature", "environment/humidity"])
    client.disconnect()



