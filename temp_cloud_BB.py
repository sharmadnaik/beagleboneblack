import Adafruit_DHT
import time  
import httplib, urllib  

sensor = Adafruit_DHT.DHT11

sensor_pin = 'P8_11'


for i in range(0,5):
	hum, temp = Adafruit_DHT.read_retry(sensor, sensor_pin)

	if hum is not None and temp is not None:  
		print 'Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temp, hum)
		params = urllib.urlencode({'field1':hum,'field2':temp,'key':'VOEUHAOQINEJWA99'}) 
		headers = {"Content-type": "application/x-www-form-urlencoded","Accept":"text/plain"}  
     		conn = httplib.HTTPConnection("api.thingspeak.com:80")  
		conn.request("POST", "/update", params, headers)  
		res = conn.getresponse()  
		print res.status, res.reason  	
	time.sleep(3)  
