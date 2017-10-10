import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

TRIG = 23
ECHO = 24

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

print("distance measurement in progress")

def distMeas():

    GPIO.output(TRIG, False)
    time.sleep(2)
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO) == False:
        pulse_start = time.time()

    while GPIO.input(ECHO) == True:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration * 17150

    distance = round(distance, 2)

    print(distance)

while True:
    distMeas()
    time.sleep(0.25)

'''
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
'''

