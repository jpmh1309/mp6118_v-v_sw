from registers import Registers

class Keyboard(object):
    def __init__(self, view):
        self.view = view
        self.state = "INACTIVE"
        print("Keyboard State: {}".format(self.state))

    def key_pressed(self,value):
        if(self.state == "INACTIVE"):
            if(value in ['1','2','3','4','5','6','7','8','9','0', '*', '#']):

                Registers.TEMP_PIN.append(value)
                # KEY_COUNT+=1
                self.view.lcd_screen.display('-'*len(Registers.TEMP_PIN))
            elif value in ['FIRE', 'PANIC']:
                if(Registers.ALERT):
                    self.state = "ALARM_CONDITION"
                print("Fire or Panic")
            elif value == 'ESC':
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