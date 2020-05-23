import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)


class SensoreUltrasuoni:

    def __init__(self):
        self.__PinTrigger = 22
        self.__PinEcho = 32

    def inizializza(self):
        GPIO.setup(self.__PinTrigger, GPIO.OUT)
        GPIO.setup(self.__PinEcho, GPIO.IN)

    def get_distanza(self):

        GPIO.output(self.__PinTrigger, True)
        time.sleep(0.00001)
        GPIO.output(self.__PinTrigger, False)
    
        StartTime = time.time()
        StopTime = time.time()

        while GPIO.input(self.__PinEcho) == 0:
            StartTime = time.time()
        
        while GPIO.input(self.__PinEcho) == 1:
            StopTime = time.time()
        
        TimeElapsed = StopTime - StartTime
        distance = (TimeElapsed * 34300) / 2
