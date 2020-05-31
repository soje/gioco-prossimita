from mina.gest_gpio.sensore_ultrasuoni import SensoreUltrasuoni
from mina.gest_gpio.schermo_lcd import SchermoLCD
import time


def avvia():
    
    lcd = SchermoLCD()
    su = SensoreUltrasuoni()

    try:
        lcd.print_message(0,0, 'Distanza cm:')
        
        while(True):
            distance = int(su.getSonar())    
            lcd.print_message(0,1, '{:02d}'.format(distance))
            time.sleep(0.5)

    except KeyboardInterrupt:
        lcd.clear_screen()
        su.destroy()
