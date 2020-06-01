from mina.gest_gpio.sensore_ultrasuoni import SensoreUltrasuoni
from mina.gest_gpio.schermo_lcd import SchermoLCD
from mina.gest_gpio.led import Led
import time


def avvia():
    
    lcd = SchermoLCD()
    su = SensoreUltrasuoni()

    try:
        lcd.print_message(0,0, 'AVVIO')

        led1 = Led(32)
        led2 = Led(36)
        led3 = Led(29)
        led4 = Led(40)

        time.sleep(3)
        
        while(True):

            distance = int(su.getSonar())
            time.sleep(1)

            if 101 <= distance <= 220 or distance is 0:
                
                lcd.print_message(0,0, '                ')
                lcd.print_message(0,0, 'Safe')
            
                led1.spegni()
                led2.spegni()
                led3.spegni()
                led4.spegni()

            elif 41 <= distance <= 100:
                
                lcd.print_message(0,0, '                ')
                lcd.print_message(0,0, 'Avviso 1')

                led1.accendi()
                led2.spegni()
                led3.spegni()
                led4.spegni()
            
            elif 31 <= distance <= 40:

                lcd.print_message(0,0, '                ')
                lcd.print_message(0,0, 'Avviso 2')
                
                led2.accendi()
                led3.spegni()
                led4.spegni()
            
            elif 21 <= distance <= 30:

                lcd.print_message(0,0, '                ')
                lcd.print_message(0,0, 'Avviso 3')
                
                led3.accendi()
                led4.spegni()
            
            elif 1 <= distance <= 20:
                
                lcd.print_message(0,0, '                ')
                lcd.print_message(0,0, 'Limite Raggiunto')

                led4.accendi()

            else:
                print('fuori range')

    except KeyboardInterrupt:
        lcd.clear_screen()
        su.destroy()
