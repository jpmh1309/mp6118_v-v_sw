from registers import Registers
import time 
#import threading

class Keyboard(object):
    def __init__(self, view):
        self.view = view
        self.state = "INACTIVE"
        print("Keyboard State: {}".format(self.state))

    def key_pressed(self,value):
        if(self.state == "INACTIVE"):
            if(value in ['1','2','3','4','5','6','7','8','9','0', '*', '#', 'ENTER']):

                Registers.TEMP_PIN.append(value)
                Registers.KEY_COUNT+=1

                if Registers.KEY_COUNT <= 4:
                    self.view.lcd_screen.display('-'*Registers.KEY_COUNT)
                if Registers.KEY_COUNT == 7:
                    print("CHECK SEQUENCE")
                
            elif value in ['FIRE', 'PANIC']:
                if(Registers.ALERT):
                    self.state = "ALARM_CONDITION"
                print("Fire or Panic")
            elif value == 'ESC':
                self.view.lcd_screen.display('ESC')
                Registers.KEY_COUNT = 0 
                Registers.TEMP_PIN = [ ]
                time.sleep(2)
                #event = threading.Event()
                #event.wait(1)
                # self.view.lcd_screen.display(value)
                #self.view.lcd_screen.display('*')
                print("Escape")
            elif value == 'ENTER':
                print("Enter")

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