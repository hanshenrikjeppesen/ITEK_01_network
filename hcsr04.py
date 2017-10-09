import time
import datetime
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(15,GPIO.OUT)
GPIO.setup(16,GPIO.IN)


def reading(sensor):
    pingtime = 0
    echotime = 0
    if sensor == 0:
        GPIO.output(15,GPIO.LOW)
        GPIO.output(15,GPIO.HIGH)
        pingtime = datetime.time()
        time.sleep(0.00001)
        GPIO.output(15,GPIO.LOW)
        while GPIO.input(16)==0:
            pingtime = datetime.time()
        while GPIO.input(16)==1:
            echotime = datetime.time()
        if (echotime is not None) and (pingtime is not None):
            elapsedtime = echotime - pingtime
            distance = elapsedtime * 17000
        else:
            distance = 0
        print(pingtime)
        print(echotime)
        return distance


while True:
    distance = reading(0)
    print(distance)
    print()
    time.sleep(0.25)

