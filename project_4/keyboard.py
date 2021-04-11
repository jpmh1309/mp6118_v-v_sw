from registers import Registers
class Keyboard(object):
    def __init__(self, view):
        self.view = view
        self.state = "INACTIVE"
        print("Keyboard State: {}".format(self.state))
    def key_pressed(self,value):
        if(self.state == "INACTIVE"):
            if(value in ['1','2','3','4','5','6','7','8','9','0']):
                if(Registers.ALERT):
                    self.state = "ALARM_CONDITION"
        print("Keyboard State: {}".format(self.state))
    def print_keyboard(self, view):
        view.lcd_screen.display(1337)
        print("Keyboard reading register: ALARM_STATE: {}".format(Registers.ALARM_STATE))
        print("Keyboard Changing register: ALARM_STATE to UNARMED")
        Registers.ALARM_STATE = "UNARMED"
    def abort(self):
        pass