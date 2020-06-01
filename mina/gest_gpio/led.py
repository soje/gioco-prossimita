import RPi.GPIO as GPIO
import time

class Led:

    def __init__(self, pin_led):
        self.__pin_led = pin_led
        self.__inizializza()
    
    def __inizializza(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.__pin_led, GPIO.OUT)
        GPIO.output(self.__pin_led, GPIO.HIGH)
    
    def accendi(self):
        GPIO.output(self.__pin_led, GPIO.LOW)
    
    def spegni(self):
        GPIO.output(self.__pin_led, GPIO.HIGH)
