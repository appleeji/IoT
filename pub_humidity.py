import paho.mqtt.client as mqtt
import random
import time

#습도를 30~95까지 받아들이는 함수
def getMsg():
    msg = str(random.randrange(30, 95))                
    return msg                

mqttc = mqtt.Client()

# YOU NEED TO CHANGE THE IP ADDRESS OR HOST NAME
mqttc.connect("192.168.43.125")
#mqttc.connect("localhost")
mqttc.loop_start()

try:
    while True:
        t = getMsg()
	print("sending humidity value : "+t+"%")
        (result, m_id) = mqttc.publish("environment/humidity", t)
        time.sleep(2)
		
except KeyboardInterrupt:
    print("Finished!")
    mqttc.loop_stop()
    mqttc.disconnect()
