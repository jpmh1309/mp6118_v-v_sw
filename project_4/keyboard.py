from registers import Registers, Alarm_Mode
import time 
#import threading

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
        print("Keyboard State: {}".format(self.state))

    def key_pressed(self,value):
        # print(PROGRAMMING_ZONES_SEQ)

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
                        print("Checking sequence")

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
                        print("Error")
                        # Clean LCD display 
                        self.view.lcd_screen.display('*')
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

            elif value in ['FIRE', 'PANIC']:
                if value == 'FIRE':
                    Registers.ALARM_MODE = Alarm_Mode.FIRE_ACTIVE
                    self.view.start_alarm("fire")
                else:
                    Registers.ALARM_MODE = Alarm_Mode.PANIC_ACTIVE
                    self.view.start_alarm("panic")

                # if(Registers.ALERT):
                #    self.state = "ALARM_CONDITION"
                print("Fire or Panic")
                # self.view.refresh_alarm()
                self.reset_keyboard()
            # LLR-024, LLR-039, LLR-051, LLR-059, LLR-065,  
            elif value == 'ESC':
                self.view.lcd_screen.display('Esc')
                self.reset_keyboard()
                # time.sleep(2)
                # event = threading.Event()
                # event.wait(1)
                # self.view.lcd_screen.display(value)
                #self.view.lcd_screen.display('*')
                print("Escape")
            # elif value == 'ENTER':
            #    print("Enter")

        print("Keyboard State: {}".format(self.state))
        print("Registers.TEMP_PIN: {}".format(Registers.TEMP_PIN))
        # self.view.lcd_screen.display(value)
    
    def print_keyboard(self, view):
        view.lcd_screen.display(1337)
        print("Keyboard reading register: ALARM_STATE: {}".format(Registers.ALARM_STATE))
        print("Keyboard Changing register: ALARM_STATE to UNARMED")
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

    # LLR-028, LLR-029, LLR-030, LLR-031, LLR-032, LLR-033, LLR-034, 
    # LLR-035, LLR-036, LLR-037, LLR-038, LLR-039, LLR-040, LLR-041
    def change_zones(self, value):
        print("CHANGE ZONES")
        if not Registers.IN_CHANGE_ZONE:
            Registers.IN_CHANGE_ZONE = True
            # Clean LCD display 
            self.view.lcd_screen.display('*')
        else:
            if Registers.CONFIRMATION == False:
                if value == '0' and Registers.IN_CHANGE_ZONE_COUNT < 1:
                    print("ZONE 0")
                    Registers.IN_CHANGE_ZONE_COUNT+=1
                    Registers.IN_CHANGE_ZONE_0 = True
                    self.view.lcd_screen.display(value)
                elif value == '1' and Registers.IN_CHANGE_ZONE_COUNT < 1:
                    print("ZONE 1")
                    Registers.IN_CHANGE_ZONE_COUNT+=1
                    Registers.IN_CHANGE_ZONE_1 = True
                    self.view.lcd_screen.display(value)
                elif value == 'ENTER' and Registers.IN_CHANGE_ZONE_COUNT == 1:
                    Registers.CONFIRMATION = True
                    self.view.lcd_screen.display('*')
                else:
                    print("Invalid zone.")
                    print("Error")
                    self.reset_keyboard()
            else:
                print("Waiting sensor(s) to change")
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
                        print("Moving to zone 0")
                        if not sensor in Registers.ZONE_0:
                            Registers.ZONE_0.append(sensor)
                            Registers.ZONE_1.remove(sensor)
                            print("Sensor to change: ", sensor)

                    if Registers.IN_CHANGE_ZONE_1:
                        print("Moving to zone 1")
                        if not sensor in Registers.ZONE_1:
                            Registers.ZONE_1.append(sensor)
                            Registers.ZONE_0.remove(sensor)
                            print("Sensor to change: ", sensor)
                    
                    Registers.SENSOR_COUNT = 0
                    Registers.SENSOR_NUMBER = []
                else:
                    print("Invalid sensor number. It should be beetwen 1-16.")
                    print("Error")
                    self.reset_keyboard() 


    # LLR-013, LLR-014, LLR-015, LLR-016, LLR-017
    def change_pin(self, value):
        print("CHANGE PIN MODE")
        if not Registers.IN_CHANGE_PIN:
            print("CHANGE PIN MODE")
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
                    print("Invalid input.")
                    print("Error")
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
                        print("New pin change successfully")
                        # self.view.lcd_screen.display('OK') 
                        Registers.PIN = Registers.NEW_PIN
                        self.reset_keyboard()
                    else:
                        print("New pin and its confirmation don't match")
                        print("Error")
                        self.reset_keyboard()
                else: 
                    print("Invalid input.")
                    print("Error")
                    self.reset_keyboard()

            # Debug prints
            print("Registers.NEW_PIN:", Registers.NEW_PIN)
            print("Registers.NEW_PIN_COUNT:", Registers.NEW_PIN_COUNT)
            print("Registers.NEW_PIN_CONFIRMATION:", Registers.NEW_PIN_CONFIRMATION)
            print("Registers.NEW_PIN_CONFIRMATION_COUNT:", Registers.NEW_PIN_CONFIRMATION_COUNT)
     
    # LLR-042, LLR-043, LLR-044, LLR-045, LLR-046, LLR-047, LLR-048, LLR-049, LLR-050, 
    # LLR-051, LLR-052, LLR-053, LLR-054
    def change_phone_number(self, value):
        print("CHANGE PHONE NUMBER")
        if not Registers.IN_CHANGE_NUMBER:
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
                print("New number change successfully")
                Registers.CALL_CENTER_NUMBER = Registers.TEMP_CALL_CENTER_NUMBER
                self.view.lcd_screen.display('OK')
                self.reset_keyboard() 
            else: 
                print("Invalid input or failed to change number.")
                print("Error")
                self.reset_keyboard()

        # Debug prints
        print("Registers.TEMP_CALL_CENTER_NUMBER:", Registers.TEMP_CALL_CENTER_NUMBER)
        print("Registers.NEW_NUMBER_COUNT:", Registers.NEW_NUMBER_COUNT)
        print("Registers.CALL_CENTER_NUMBER:", Registers.CALL_CENTER_NUMBER)

    # LLR-055, LLR-056, LLR-057, LLR-058, LLR-059, LLR-060
    def armed_system(self, value):
        print("ARMED SYSTEM")
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
                print("ok")
                self.view.refresh_alarm()
                self.reset_keyboard()
                self.reset_keyboard()
            else:
                print("Invalid input or failed to change number.")
                print("Error")
                self.reset_keyboard()

    def disarmed_system(self):
        print("DISARMED SYSTEM")
        Registers.ALARM_STATE = "UNARMED"
        Registers.OP_MODE = 0
        self.view.refresh_alarm()
        self.reset_keyboard()

    # LLR-061, LLR-062, LLR-063, LLR-064, LLR-065, LLR-066
    # def disarmed_system(self, value):
    #    print("ALARM ACTIVE")
    #    self.reset_keyboard()
    
    def disable_emergency(self, value):
        print("DISABLED EMERGENCY")
        self.view.refresh_alarm()
        self.reset_keyboard()