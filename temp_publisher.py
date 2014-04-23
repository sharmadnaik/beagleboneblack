import Adafruit_DHT
import time  
import httplib, urllib  
import paho.mqtt.client as mqtt

sensor = Adafruit_DHT.DHT11

sensor_pin = 'P8_11'


mqttc = mqtt.Client()

mqttc.connect("iot.eclipse.org")
mqttc.loop_start()



while True:
	hum, temp = Adafruit_DHT.read_retry(sensor, sensor_pin)

	if hum is not None and temp is not None:  
    		mqttc.publish("bangalore/indoor/temperature", temp)
    		mqttc.publish("bangalore/indoor/humidity", hum)
		print 'Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temp, hum)
	time.sleep(3)  
