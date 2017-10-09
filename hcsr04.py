import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(15, GPIO.OUT)
GPIO.setup(16, GPIO.IN)


def reading():
    pingtime = 0
    echotime = 0
    GPIO.output(15,GPIO.LOW)
    GPIO.output(15,GPIO.HIGH)
    pingtime = time.time()
    time.sleep(.00001)
    GPIO.output(15,GPIO.LOW)
    while GPIO.input(16) == 0:
        pingtime = time.time()
    while GPIO.input(16) == 1:
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

