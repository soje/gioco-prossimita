from mina.gest_gpio.PCF8574 import PCF8574_GPIO
from mina.gest_gpio.Adafruit_LCD1602 import Adafruit_CharLCD

PCF8574_address = 0x27  # I2C address of the PCF8574 chip.
PCF8574A_address = 0x3f  # I2C address of the PCF8574A chip.


class SchermoLCD:

    def __init__(self):
        
        try:
            self.__mcp = PCF8574_GPIO(PCF8574_address)
        except:
            try:
                self.__mcp = PCF8574_GPIO(PCF8574A_address)
            except:
                print('Errore I2CS')

        self.__lcd = Adafruit_CharLCD(pin_rs=0, pin_e=2, pins_db=[4,5,6,7], GPIO=self.__mcp)

        self.__mcp.output(3,1)
        self.__lcd.begin(16,2)

    def print_message(self, colonna, riga, msg):
        self.__lcd.setCursor(colonna, riga)
        self.__lcd.message(msg)
    
    def clear_screen(self):
        self.__lcd.clear()
