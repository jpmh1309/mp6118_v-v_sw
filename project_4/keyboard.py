# MP-6118 Validation and Verification in Software Engineering
# Students: 
#           - David Martínez
#           - Jose Martínez
# Project:  Smart Embedded Systems Security Alarm  
from registers import Registers, Alarm_Mode
import logging
import time

logger = logging.getLogger(__name__) 

PROGRAMMING_ZONES_SEQ = ['*', '*', 'ENTER']
CHANGE_PIN_SEQ = ['*', '#', 'ENTER']
CHANGE_NUMBER_SEQ = ['#', '*', 'ENTER']
ARMED_SEQ = ['*', 'ENTER']
DISARMED_SEQ = ['#', 'ENTER']
DISABLED_SEQ = ['ENTER']

class Keyboard(object):
    def __init__(self, view):
        self.view = view
        self.state = "INACTIVE"
        logger.info("Keyboard State: {}".format(self.state))

    def key_pressed(self,value):

        if(self.state == "INACTIVE"):

            # Press any value from the keyboard
            if(value in ['1','2','3','4','5','6','7','8','9','0', '*', '#', 'ENTER']):

                # Operation Mode: Reading keyboard and selecting mode 
                if Registers.ALARM_MODE == Alarm_Mode.NONE:
                    # Save to TEMP_PIN
                    Registers.KEY_COUNT+=1
                    Registers.TEMP_PIN.append(value)    

                    # Sanity. Waiting for PIN, if not, restart TEMP_PIN
                    if(value in ['*', '#', 'ENTER']) and Registers.KEY_COUNT <= 4:
                        # Registers.KEY_COUNT = 0
                        # Registers.TEMP_PIN = []
                        self.reset_keyboard()

                    # LLR-019
                    if Registers.KEY_COUNT <= 4:
                        self.view.lcd_screen.display('-'*Registers.KEY_COUNT)
                    
                    # Check sequence to see it is valid for any mode
                    if 4 < Registers.KEY_COUNT < 8:
                        logger.info("Checking sequence")

                        if Registers.TEMP_PIN == (Registers.PIN + PROGRAMMING_ZONES_SEQ):
                            Registers.ALARM_MODE = Alarm_Mode.CHANGE_ZONES
                            self.change_zones(value)

                        if Registers.TEMP_PIN == (Registers.PIN + CHANGE_PIN_SEQ):
                            Registers.ALARM_MODE = Alarm_Mode.CHANGE_PIN
                            self.change_pin(value)
                        
                        if Registers.TEMP_PIN == (Registers.PIN + CHANGE_NUMBER_SEQ):
                            Registers.ALARM_MODE = Alarm_Mode.CHANGE_NUMBER
                            self.change_phone_number(value)

                        if Registers.TEMP_PIN == (Registers.PIN + ARMED_SEQ):
                            Registers.ALARM_MODE = Alarm_Mode.ARMED_ACTIVE
                            self.armed_system(value)

                        if Registers.TEMP_PIN == (Registers.PIN + DISARMED_SEQ):
                            Registers.ALARM_MODE = Alarm_Mode.DISARMED_ACTIVE
                            self.disarmed_system()

                        if Registers.TEMP_PIN == (Registers.PIN + DISABLED_SEQ):
                            Registers.ALARM_MODE = Alarm_Mode.DISABLED
                            self.disable_emergency(value)                      
                
                    if Registers.KEY_COUNT >= 8:
                        logger.info("Error")
                        # Clean LCD display
                        self.print_error()
                        self.reset_keyboard()

                # Operation Mode: Changing zones of the sensors
                elif Registers.ALARM_MODE == Alarm_Mode.CHANGE_ZONES:
                    self.change_zones(value)

                # Operation Mode: Changing emergency number
                elif Registers.ALARM_MODE == Alarm_Mode.CHANGE_NUMBER:
                    self.change_phone_number(value)
      
                # Operation Mode: Changing PIN
                elif Registers.ALARM_MODE == Alarm_Mode.CHANGE_PIN:
                    self.change_pin(value)

                # Operation Mode: Selecting armed mode 0 or mode 1 
                elif Registers.ALARM_MODE == Alarm_Mode.ARMED_ACTIVE:
                    self.armed_system(value)
            # LLR-061, LLR-062, LLR-063, LLR-064, LLR-065, LLR-066
            elif value in ['FIRE', 'PANIC']:
                if value == 'FIRE':
                    Registers.ALARM_MODE = Alarm_Mode.FIRE_ACTIVE
                    self.view.start_alarm("fire")
                else:
                    Registers.ALARM_MODE = Alarm_Mode.PANIC_ACTIVE
                    self.view.start_alarm("panic")

                logger.info("Fire or Panic")
                self.reset_keyboard()

            # LLR-024, LLR-039, LLR-051, LLR-059, LLR-065,  
            elif value == 'ESC':
                self.view.display_lcd("Esc", 3)
                self.reset_keyboard()
                logger.info("Escape")

        logger.info("Keyboard State: {}".format(self.state))
        logger.info("Registers.TEMP_PIN: {}".format(Registers.TEMP_PIN))
    
    def print_keyboard(self, view):
        view.lcd_screen.display(1337)
        logger.info("Keyboard reading register: ALARM_STATE: {}".format(Registers.ALARM_STATE))
        logger.info("Keyboard Changing register: ALARM_STATE to UNARMED")
        Registers.ALARM_STATE = "UNARMED"
    
    def abort(self):
        pass

    def reset_keyboard(self):
        Registers.ALARM_MODE = Alarm_Mode.NONE
        Registers.KEY_COUNT = 0
        Registers.TEMP_PIN = []
        Registers.IN_CHANGE_PIN = False 
        Registers.IN_CHANGE_ZONE = False
        Registers.IN_CHANGE_ZONE_0 = False
        Registers.IN_CHANGE_ZONE_1 = False
        Registers.IN_CHANGE_ZONE_COUNT = 0   
        Registers.NEW_PIN = []
        Registers.NEW_PIN_COUNT = 0
        Registers.NEW_PIN_CONFIRMATION = []
        Registers.NEW_PIN_CONFIRMATION_COUNT = 0
        Registers.CONFIRMATION = False
        Registers.IN_CHANGE_NUMBER = False
        Registers.TEMP_CALL_CENTER_NUMBER = []
        Registers.NEW_NUMBER_COUNT = 0
        Registers.IN_ARMED_SELECT = False
        Registers.MODE_SELECTED = False
        Registers.MODE_SELECTED = False
        Registers.SENSOR_COUNT = 0
        Registers.SENSOR_NUMBER = []
        self.view.stop_blink_led(self.view.led_battery)

    # LLR-018, LLR-019, LLR-020, LLR-021, LLR-022, LLR-023, LLR-024,
    # LLR-025, LLR-026, LLR-027
    def change_zones(self, value):
        logger.info("CHANGE ZONES")
        if not Registers.IN_CHANGE_ZONE:
            self.view.blink_led(self.view.led_battery, 0.5)
            Registers.IN_CHANGE_ZONE = True
            # Clean LCD display 
            self.view.lcd_screen.display('*')
        else:
            if Registers.CONFIRMATION == False:
                if value == '0' and Registers.IN_CHANGE_ZONE_COUNT < 1:
                    logger.info("ZONE 0")
                    Registers.IN_CHANGE_ZONE_COUNT+=1
                    Registers.IN_CHANGE_ZONE_0 = True
                    self.view.lcd_screen.display(value)
                elif value == '1' and Registers.IN_CHANGE_ZONE_COUNT < 1:
                    logger.info("ZONE 1")
                    Registers.IN_CHANGE_ZONE_COUNT+=1
                    Registers.IN_CHANGE_ZONE_1 = True
                    self.view.lcd_screen.display(value)
                elif value == 'ENTER' and Registers.IN_CHANGE_ZONE_COUNT == 1:
                    Registers.CONFIRMATION = True
                    self.view.lcd_screen.display('*')
                else:
                    logger.info("Invalid zone.")
                    logger.info("Error")
                    self.print_error()
                    self.reset_keyboard()
            else:
                logger.info("Waiting sensor(s) to change")
                if value in ['1','2','3','4','5','6','7','8','9'] and Registers.SENSOR_COUNT < 1:
                    Registers.SENSOR_COUNT+=1
                    Registers.SENSOR_NUMBER.append(value)
                    self.view.lcd_screen.display(value)  
                elif value in ['1','2','3','4','5','6','0'] and Registers.SENSOR_COUNT == 1:
                    Registers.SENSOR_NUMBER.append(value)
                    self.view.lcd_screen.display(''.join(Registers.SENSOR_NUMBER))  
                elif value == 'ENTER' and Registers.SENSOR_COUNT == 1:
                    sensor = int(''.join(Registers.SENSOR_NUMBER))
                    if Registers.IN_CHANGE_ZONE_0:
                        logger.info("Moving to zone 0")
                        if not sensor in Registers.ZONE_0:
                            Registers.ZONE_0.append(sensor)
                            Registers.ZONE_1.remove(sensor)
                            logger.info("Sensor to change: {}".format(sensor))

                    if Registers.IN_CHANGE_ZONE_1:
                        logger.info("Moving to zone 1")
                        if not sensor in Registers.ZONE_1:
                            Registers.ZONE_1.append(sensor)
                            Registers.ZONE_0.remove(sensor)
                            logger.info("Sensor to change: {}".format(sensor))
                    
                    Registers.SENSOR_COUNT = 0
                    Registers.SENSOR_NUMBER = []
                else:
                    logger.info("Invalid sensor number. It should be beetwen 1-16.")
                    logger.info("Error")
                    self.print_error()
                    self.reset_keyboard() 


    # LLR-028, LLR-029, LLR-030, LLR-031, LLR-032, LLR-033, LLR-034, 
    # LLR-035, LLR-036, LLR-037, LLR-038, LLR-039, LLR-040, LLR-041
    def change_pin(self, value):
        logger.info("CHANGE PIN MODE")
        if not Registers.IN_CHANGE_PIN:
            logger.info("CHANGE PIN MODE")
            self.view.blink_led(self.view.led_battery, 0.5)
            Registers.IN_CHANGE_PIN = True
            # Clean LCD display 
            self.view.lcd_screen.display('*')
        else:
            if not Registers.CONFIRMATION:
                if value in ['1','2','3','4','5','6','7','8','9','0'] and Registers.NEW_PIN_COUNT < 4:
                    Registers.NEW_PIN_COUNT+=1
                    Registers.NEW_PIN.append(value)
                    self.view.lcd_screen.display('-'*Registers.NEW_PIN_COUNT)
                elif value == '*':
                    Registers.NEW_PIN_COUNT-=1
                    Registers.NEW_PIN.pop()
                    self.view.lcd_screen.display('-'*Registers.NEW_PIN_COUNT)
                elif value == 'ENTER' and Registers.NEW_PIN_COUNT == 4:
                    Registers.CONFIRMATION = True
                else:
                    logger.info("Invalid input.")
                    logger.info("Error")
                    self.print_error()
                    self.reset_keyboard()
            else:
                # Clean LCD display
                self.view.lcd_screen.display('-'*Registers.NEW_PIN_CONFIRMATION_COUNT)
                
                if value in ['1','2','3','4','5','6','7','8','9','0'] and Registers.NEW_PIN_CONFIRMATION_COUNT < 4: 
                    Registers.NEW_PIN_CONFIRMATION_COUNT+=1
                    Registers.NEW_PIN_CONFIRMATION.append(value)
                    self.view.lcd_screen.display('-'*Registers.NEW_PIN_CONFIRMATION_COUNT)   
                elif value == '*':
                    Registers.NEW_PIN_CONFIRMATION_COUNT-=1
                    Registers.NEW_PIN_CONFIRMATION.pop()
                    self.view.lcd_screen.display('-'*Registers.NEW_PIN_CONFIRMATION_COUNT)  
                elif value == 'ENTER' and Registers.NEW_PIN_CONFIRMATION_COUNT == 4:
                    if Registers.NEW_PIN == Registers.NEW_PIN_CONFIRMATION: 
                        logger.info("New pin change successfully")
                        # self.view.lcd_screen.display('OK') 
                        Registers.PIN = Registers.NEW_PIN
                        self.reset_keyboard()
                    else:
                        logger.info("New pin and its confirmation don't match")
                        logger.info("Error")
                        self.print_error()
                        self.reset_keyboard()
                else: 
                    logger.info("Invalid input.")
                    logger.info("Error")
                    self.print_error()
                    self.reset_keyboard()

            # Debug prints
            logger.info("Registers.NEW_PIN: {}".format(Registers.NEW_PIN))
            logger.info("Registers.NEW_PIN_COUNT: {}".format(Registers.NEW_PIN_COUNT))
            logger.info("Registers.NEW_PIN_CONFIRMATION: {}".format(Registers.NEW_PIN_CONFIRMATION))
            logger.info("Registers.NEW_PIN_CONFIRMATION_COUNT: {}".format(Registers.NEW_PIN_CONFIRMATION_COUNT))
     
    # LLR-042, LLR-043, LLR-044, LLR-045, LLR-046, LLR-047, LLR-048, LLR-049, LLR-050, 
    # LLR-051, LLR-052, LLR-053, LLR-054
    def change_phone_number(self, value):
        logger.info("CHANGE PHONE NUMBER")
        if not Registers.IN_CHANGE_NUMBER:
            self.view.blink_led(self.view.led_battery, 0.5)
            Registers.IN_CHANGE_NUMBER = True
            # Clean LCD display 
            self.view.lcd_screen.display('*')
        else:
            if value in ['1','2','3','4','5','6','7','8','9','0'] and Registers.NEW_NUMBER_COUNT < 8:
                Registers.NEW_NUMBER_COUNT+=1
                Registers.TEMP_CALL_CENTER_NUMBER.append(value)
                self.view.lcd_screen.display(''.join(Registers.TEMP_CALL_CENTER_NUMBER))   
            elif value == '*':
                Registers.NEW_NUMBER_COUNT-=1
                Registers.TEMP_CALL_CENTER_NUMBER.pop()
                self.view.lcd_screen.display(''.join(Registers.TEMP_CALL_CENTER_NUMBER)) 
            elif value == 'ENTER' and Registers.NEW_NUMBER_COUNT == 8:
                logger.info("New number change successfully")
                Registers.CALL_CENTER_NUMBER = Registers.TEMP_CALL_CENTER_NUMBER
                self.view.lcd_screen.display('OK')
                self.reset_keyboard() 
            else: 
                logger.info("Invalid input or failed to change number.")
                logger.info("Error")
                self.print_error()
                self.reset_keyboard()

        # Debug prints
        logger.info("Registers.TEMP_CALL_CENTER_NUMBER: {}".format(Registers.TEMP_CALL_CENTER_NUMBER))
        logger.info("Registers.NEW_NUMBER_COUNT: {}".format(Registers.NEW_NUMBER_COUNT))
        logger.info("Registers.CALL_CENTER_NUMBER: {}".format(Registers.CALL_CENTER_NUMBER))

    # LLR-055, LLR-056, LLR-057, LLR-058, LLR-059, LLR-060
    def armed_system(self, value):
        logger.info("ARMED SYSTEM")
        if not Registers.IN_ARMED_SELECT:
            Registers.ALARM_STATE = "ARMED"
            self.view.refresh_alarm()
            Registers.IN_ARMED_SELECT = True
        else:
            # mode 0 or 1
            if value == '0':
                Registers.OP_MODE = 0
                Registers.MODE_SELECTED = True
            elif value == '1':
                Registers.OP_MODE = 1
                Registers.MODE_SELECTED = True
            elif value == 'ENTER' and Registers.MODE_SELECTED:
                logger.info("ok")
                self.view.refresh_alarm()
                self.reset_keyboard()
                self.reset_keyboard()
            else:
                logger.info("Invalid input or failed to change number.")
                logger.info("Error")
                self.print_error()
                self.reset_keyboard()

    # LLR-061, LLR-062, LLR-063, LLR-064, LLR-065, LLR-066
    def disarmed_system(self):
        logger.info("DISARMED SYSTEM")
        Registers.ALARM_STATE = "UNARMED"
        Registers.OP_MODE = 0
        self.view.refresh_alarm()
        self.reset_keyboard()
    
    def disable_emergency(self, value):
        logger.info("DISABLED EMERGENCY")
        self.view.refresh_alarm()
        self.reset_keyboard()

    def print_error(self):
        self.view.stop_blink_led(self.view.led_battery)
        self.view.display_lcd("Error", 3)