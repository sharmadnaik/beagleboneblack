import paho.mqtt.client as mqtt

mqttc = mqtt.Client()

mqttc.connect("iot.eclipse.org")
mqttc.loop_start()

while True:
    mqttc.publish("hello/world", "Hello Sharmad")
