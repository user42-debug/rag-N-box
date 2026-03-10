import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)

GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.add_event_detect(4, GPIO.RISING)

last = 1

while True:
    if GPIO.input(4) == 0 and last == 1:
        print("Bouton appuye")
        os.system(f'rpicam-jpeg --output image.jpg --timeout 10')

    last = GPIO.input(4)
    time.sleep(2)