from registers import Registers
from keyboard import Keyboard
class Alarm(object):
    def __init__(self, view):
        self.view = view
        self.keyboard = Keyboard(view)
        self.state = "INITIAL_STATE"
        #Evaluate the ALARM_STATE.
        if(Registers.ALARM_STATE == "UNARMED"):
            self.state = "UNARMED"
        elif(Registers.ALARM_STATE == "ARMED"):
            #Evaluate the operation mode.
            if(Registers.OP_MODE == 0):
                #ACTIVE_SENSORS are all the sensors.
                Registers.ACTIVE_SENSOR = list(range(1,16))
                self.state = "MODE_0"
            elif(Register.OP_MODE == 1):
                Registers.ACTIVE_SENSOR = Registers.ZONE_1
                self.state = "MODE_1"
        self.view.lcd_screen.display(8888)
        print("ALARM in {} state".format(self.state))
    
    def key_pressed(self,value):
        if(self.state == "UNARMED" or self.state == "ARMED"):
            self.keyboard.key_pressed(value)
        else:
            pass