import RPi.GPIO as GPIO
import time

trigPin = 22
echoPin = 18
MAX_DISTANCE = 220          # define the maximum measuring distance, unit: cm
timeOut = MAX_DISTANCE*60   # calculate timeout according to the maximum measuring distance


class SensoreUltrasuoni:

    def __init__(self):
        self.__setup()

    def __setup(self):
        GPIO.setmode(GPIO.BOARD)      # use PHYSICAL GPIO Numbering
        GPIO.setup(trigPin, GPIO.OUT)   # set trigPin to OUTPUT mode
        GPIO.setup(echoPin, GPIO.IN)    # set echoPin to INPUT mode

    def getSonar(self):     # get the measurement results of ultrasonic module,with unit: cm
        GPIO.output(trigPin,GPIO.HIGH)      # make trigPin output 10us HIGH level 
        time.sleep(0.00001)     # 10us
        GPIO.output(trigPin,GPIO.LOW) # make trigPin output LOW level 
        pingTime = self.pulseIn(echoPin,GPIO.HIGH,timeOut)   # read plus time of echoPin
        distance = pingTime * 340.0 / 2.0 / 10000.0     # calculate distance with sound speed 340m/s 
        return distance
    
    def pulseIn(self, pin,level,timeOut): # obtain pulse time of a pin under timeOut
        t0 = time.time()
        while(GPIO.input(pin) != level):
            if((time.time() - t0) > timeOut*0.000001):
                return 0;
        t0 = time.time()
        while(GPIO.input(pin) == level):
            if((time.time() - t0) > timeOut*0.000001):
                return 0;
        pulseTime = (time.time() - t0)*1000000
        return pulseTime

    def destroy(self):
        GPIO.cleanup()
        
    def loop(self):
        while(True):
            distance = getSonar() # get distance
            print ("The distance is : %.2f cm"%(distance))
            time.sleep(1)
