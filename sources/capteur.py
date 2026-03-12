import RPi.GPIO as GPIO
import os
import time

class Capteur:
    def __init__(self, pin):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        
        GPIO.add_event_detect(self.pin, GPIO.RISING)

    def __bool__(self):
        return not GPIO.input(self.pin)
