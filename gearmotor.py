import Adafruit_BBIO.GPIO as GPIO
outMotor1Pin = "P8_7"
outMotor2Pin = "P8_9"
GPIO.setup(outMotor1Pin,GPIO.OUT)
GPIO.setup(outMotor2Pin,GPIO.OUT)
from time import sleep

print "Both Motor Low"
GPIO.output(outMotor1Pin, GPIO.LOW)
GPIO.output(outMotor2Pin, GPIO.LOW)
sleep(3)
print "Motor1 High"
GPIO.output(outMotor1Pin, GPIO.HIGH)
GPIO.output(outMotor2Pin, GPIO.LOW)
sleep(3)
print "Both Motor High"
GPIO.output(outMotor1Pin, GPIO.HIGH)
GPIO.output(outMotor2Pin, GPIO.HIGH)
sleep(3)
print "Motor2 High"
GPIO.output(outMotor1Pin, GPIO.LOW)
GPIO.output(outMotor2Pin, GPIO.HIGH)
sleep(3)

GPIO.cleanup()
