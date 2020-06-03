from mina.gest_gpio.sensore_ultrasuoni import SensoreUltrasuoni
from mina.gest_gpio.schermo_lcd import SchermoLCD
from mina.gest_gpio.led import Led
import time


def avvia():
    
    lcd = SchermoLCD()
    su = SensoreUltrasuoni()

    locks = [False]*5

    try:
        lcd.print_message(0,0, 'AVVIO')

        led1 = Led(32)
        led2 = Led(36)
        led3 = Led(29)
        led4 = Led(40)

        time.sleep(3)
        
        while(True):

            distance = int(su.getSonar())

            if 101 <= distance <= 220 or distance is 0:
                
                if locks[0] is False:
                    lcd.print_message(0,0, '                ')
                    lcd.print_message(0,0, 'Safe')
            
                    led1.spegni()
                    led2.spegni()
                    led3.spegni()
                    led4.spegni()

                    locks[0] = True
                
                    locks[1] = False
                    locks[2] = False
                    locks[3] = False
                    locks[4] = False

            elif 41 <= distance <= 100:
                
                if locks[1] is False:
                    lcd.print_message(0,0, '                ')
                    lcd.print_message(0,0, 'Avviso 1')

                    led1.accendi()
                    led2.spegni()
                    led3.spegni()
                    led4.spegni()

                    locks[1] = True
                
                    locks[0] = False
                    locks[2] = False
                    locks[3] = False
                    locks[4] = False
                
            elif 31 <= distance <= 40:

                if locks[2] is False:
                    lcd.print_message(0,0, '                ')
                    lcd.print_message(0,0, 'Avviso 2')

                    led1.accendi()
                    led2.accendi()
                    led3.spegni()
                    led4.spegni()

                    locks[2] = True

                    locks[0] = False
                    locks[1] = False
                    locks[3] = False
                    locks[4] = False
            
            elif 21 <= distance <= 30:
                
                if locks[3] is False:
                    lcd.print_message(0,0, '                ')
                    lcd.print_message(0,0, 'Avviso 3')
                    
                    led1.accendi()
                    led2.accendi()
                    led3.accendi()
                    led4.spegni()

                    locks[3] = True

                    locks[0] = False
                    locks[1] = False
                    locks[2] = False
                    locks[4] = False                    
                
            elif 1 <= distance <= 20:
                
                if locks[4] is False:
                    lcd.print_message(0,0, '                ')
                    lcd.print_message(0,0, 'Limite Raggiunto')

                    led1.accendi()
                    led2.accendi()
                    led3.accendi()
                    led4.accendi()

                    locks[4] = True

                    locks[0] = False
                    locks[1] = False
                    locks[2] = False
                    locks[3] = False

            else:
                print('fuori range')

            time.sleep(0.5)

    except KeyboardInterrupt:
        lcd.clear_screen()
        su.destroy()
