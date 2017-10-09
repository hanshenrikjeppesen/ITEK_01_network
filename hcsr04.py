import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

TRIG = 23
ECHO = 24

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)


def reading():
    pingtime = 0
    echotime = 0
    GPIO.output(TRIG,GPIO.LOW)
    GPIO.output(TRIG,GPIO.HIGH)
    pingtime = time.time()
    time.sleep(.00001)
    GPIO.output(TRIG,GPIO.LOW)
    while GPIO.input(ECHO) == 0:
        pingtime = time.time()
    while GPIO.input(ECHO) == 1:
        echotime = time.time()
    if (echotime is not None) and (pingtime is not None):
        elapsedtime = echotime - pingtime
        distance = elapsedtime * 17000
    else:
        distance = 0
    return distance


while True:
    distMeas = reading()
    print(distMeas)
    print("")
    time.sleep(0.25)

