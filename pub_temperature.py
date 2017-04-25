import paho.mqtt.client as mqtt
import random
import time

#20~35까지 온도를 랜덤하게 받아들이는 함수
def getMsg():
	msg = str(random.randrange(20, 35))                
	return msg                

mqttc = mqtt.Client()

# YOU NEED TO CHANGE THE IP ADDRESS OR HOST NAME
#연결할 ip주소
mqttc.connect("192.168.43.125")
#mqttc.connect("localhost")
mqttc.loop_start()

try:
	while True:
		t = getMsg()
		print("sending temperature value : "+t)
		(result, m_id) = mqttc.publish("environment/temperature", t)
		time.sleep(2)
		
except KeyboardInterrupt:
	print("Finished!")
	mqttc.loop_stop()
	mqttc.disconnect()
