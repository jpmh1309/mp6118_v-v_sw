from registers import Registers, Alarm_Mode
import time 
#import threading

PROGRAMMING_ZONES_SEQ = ['*', '*', 'ENTER']
CHANGE_PIN_SEQ = ['*', '#', 'ENTER']
CHANGE_NUMBER_SEQ = ['#', '*', 'ENTER']
ARMED_SEQ = ['*', 'ENTER']
ALARM_SEQ = ['#', 'ENTER']
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
                        reset_keyboard(self)

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

                        if Registers.TEMP_PIN == (Registers.PIN + ALARM_SEQ):
                            Registers.ALARM_MODE = Alarm_Mode.ALARM_ACTIVE
                            self.alarm_active(value)

                        if Registers.TEMP_PIN == (Registers.PIN + DISABLED_SEQ):
                            Registers.ALARM_MODE = Alarm_Mode.CHANGE_NUMBER
                            self.disable_emergency(value)                      
                
                    if Registers.KEY_COUNT >= 8:
                        print("Error")
                                    # Clean LCD display 
                        self.view.lcd_screen.display('*')
                        self.reset_keyboard()
                # Operation Mode: Changing PIN
                elif Registers.ALARM_MODE == Alarm_Mode.CHANGE_PIN:
                    self.change_pin(value)
            
            elif value in ['FIRE', 'PANIC']:
                if value == 'FIRE':
                    Registers.ALARM_MODE = Alarm_Mode.FIRE_ACTIVE
                else:
                    Registers.ALARM_MODE = Alarm_Mode.PANIC_ACTIVE

                # if(Registers.ALERT):
                #    self.state = "ALARM_CONDITION"
                print("Fire or Panic")
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
        Registers.IN_CHANGE_MODE = False 
        Registers.NEW_PIN = []
        Registers.NEW_PIN_COUNT = 0
        Registers.NEW_PIN_CONFIRMATION = []
        Registers.NEW_PIN_CONFIRMATION_COUNT = 0
        Registers.CONFIRMATION = False

    # LLR-013, LLR-014, LLR-015, LLR-016, LLR-017
    def change_pin(self, value):
        print("CHANGE PIN MODE")
        if not Registers.IN_CHANGE_MODE:
            print("CHANGE PIN MODE")
            Registers.IN_CHANGE_MODE = True
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
     
    # LLR-018, LLR-019, LLR-020, LLR-021, LLR-022, LLR-023, LLR-024, LLR-025, LLR-026, LLR-027
    def change_phone_number(self, value):
        print("CHANGE PHONE NUMBER")

    # LLR-028, LLR-029, LLR-030, LLR-031, LLR-032, LLR-033, LLR-034, LLR-035, LLR-036, LLR-037, 
    # LLR-038, LLR-039, LLR-040, LLR-041
    def armed_system(self, value):
        print("CHANGE PHONE NUMBER")

    # LLR-042, LLR-043, LLR-044, LLR-045, LLR-046, LLR-047, LLR-048, LLR-049, LLR-050, LLR-051,
    # LLR-052, LLR-053, LLR-054
    def alarm_active(self, value):
        print("CHANGE PHONE NUMBER")
    
    def disable_emergency(self, value):
        print("DISABLE EMERGENCY")

    def change_zones(self, value):
        print("CHANGE ZONES")