from registers import Registers
from keyboard import Keyboard
import threading
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
            elif(Registers.OP_MODE == 1):
                Registers.ACTIVE_SENSOR = Registers.ZONE_1
                self.state = "MODE_1"
        self.view.lcd_screen.display(8888)
        print("ALARM in {} state".format(self.state))
    
    def key_pressed(self,value):
        if(self.state == "UNARMED" or self.state == "MODE_0" or self.state == "MODE_1" or self.state == "MAIN_ENTRANCE" or self.state == "ALARM"):
            self.keyboard.key_pressed(value)
        else:
            pass
        print("ALARM in {} state".format(self.state))
    def sensor_activated(self, sensor):
        print("Sensor {} activated".format(sensor))
        print("ALARM in {} state".format(self.state))
        if(self.state == "MODE_0"):
            self.start_alarm(sensor)
        elif(self.state == "MODE_1"):
            print("Active sensors {}".format(Registers.ACTIVE_SENSOR))
            if(sensor in Registers.ACTIVE_SENSOR):
                self.keyboard.abort()
                if(sensor == Registers.MAIN_ENTRANCE):
                    self.state = "MAIN_ENTRANCE"
                    #Start the timer  and wait for the interrumption.
                    self.timer = threading.Timer(30.0, self.start_alarm)
                    print("Starting 30s timer")
                    self.timer.start()
                else:
                   self.start_alarm(sensor) 
            else:
                pass
        else:
            pass
        print("ALARM in {} state".format(self.state))
    def start_alarm(self,sensor = 1):
        self.state = "ALARM"
        self.keyboard.abort()
        Registers.ACTIVATE_BOCINA = True
        print("Llamando al {} : centro de supervision... Numero de usuario: {}, Numero de Sensor:{}"\
            .format(Registers.CALL_CENTER_NUMBER,
                Registers.USER_NUMBER, 
                sensor
            )
        )
        print("ALARM in {} state".format(self.state))

            

