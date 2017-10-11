import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

TRIG = 23
ECHO = 24
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
#test stress

def distMeas():
    # ensure that the Trigger pin is set low
    # and gives the sensor time to settle
    GPIO.output(TRIG, False)
    time.sleep(0.0005)
    # The HC-SR04 sensor requires a short 10uS pulse to trigger the module
    # 8 ultrasound bursts at 40 kHz
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO) == False:
        pulse_start = time.time()

    while GPIO.input(ECHO) == True:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration * 17150

    distance = round(distance, 1) # we will round our distance to 1 decimal places (for neatness!)

    if distance > 400:
        return None
    else:
        return distance

while True:
    distanceToObject = distMeas()
    print("Distance to object is {} cm".format(distanceToObject))
    time.sleep(0.25)

