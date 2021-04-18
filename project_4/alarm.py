from registers import Registers
from keyboard import Keyboard
import threading
from repeatedtimer import RepeatedTimer
class Alarm(object):
    def __init__(self, view):
        self.view = view
        self.keyboard = Keyboard(view)
        self.state = "INITIAL_STATE"
        self.check_battery()
        self.view.lcd_error.setHidden(True)
        self.rt = {}
        #Evaluate the ALARM_STATE.
        if(Registers.ALARM_STATE == "UNARMED"):
            self.start_state_unarmed()
        elif(Registers.ALARM_STATE == "ARMED"):
            #Evaluate the operation mode.
            if(Registers.OP_MODE == 0):
                self.start_state_mode_0()
            elif(Registers.OP_MODE == 1):
                self.start_state_mode_1()
                # Registers.ACTIVE_SENSOR = Registers.ZONE_1
                # self.state = "MODE_1"
        # self.view.lcd_screen.display('ok')
        # self.view.led_battery.hide()
        # self.view.led_armed.hide()
        print("ALARM in {} state".format(self.state))
    
    def key_pressed(self,value):
        if(value == '3'):
            self.blink_led(self.view.led_battery,1)
        if(value == '4'):
            self.stop_blink_led(self.view.led_battery)
        if(value == '5'):
            self.display_lcd('1234',3)
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
        self.view.sound_activated.setHidden(False)
        self.view.sound_deactivated.setHidden(True)
        print("Llamando al {} : centro de supervision... Numero de usuario: {}, Numero de Sensor:{}"\
            .format(Registers.CALL_CENTER_NUMBER,
                Registers.USER_NUMBER, 
                sensor
            )
        )
        print("ALARM in {} state".format(self.state))
    def start_state_mode_0(self):
        #ACTIVE_SENSORS are all the sensors.
        Registers.ACTIVE_SENSOR = list(range(1,16))
        self.state = "MODE_0"
        self.view.lcd_mode_0.setHidden(False)
        self.view.lcd_mode_1.setHidden(True)
        self.view.led_armed.setHidden(False)
        self.view.sound_activated.setHidden(True)
        self.view.sound_deactivated.setHidden(False)

    def start_state_mode_1(self):
        Registers.ACTIVE_SENSOR = Registers.ZONE_1
        self.state = "MODE_1"
        self.view.lcd_mode_0.setHidden(True)
        self.view.lcd_mode_1.setHidden(False)
        self.view.led_armed.setHidden(False)
        self.view.sound_activated.setHidden(True)
        self.view.sound_deactivated.setHidden(False)

    def start_state_unarmed(self):
        self.state = "UNARMED"
        self.view.led_armed.setHidden(True)
        self.view.lcd_mode_0.setHidden(True)
        self.view.lcd_mode_1.setHidden(True)
        self.view.sound_activated.setHidden(True)
        self.view.sound_deactivated.setHidden(False)

    def check_battery(self):
        if(self.view.battery_percentage.value() > 50):
            self.view.led_battery.setHidden(True)
        else:
            self.view.led_battery.setHidden(False)
    
    def refresh_alarm(self):
        self.__init__(self.view)

    def toggle_led(led_label):
        led_label.setHidden(not led_label.isHidden())
        

    def blink_led(self,led_label, period):
        print("Starting {}s timer for led {}".format(period,led_label.objectName()))
        self.rt[led_label.objectName()] = RepeatedTimer(period, Alarm.toggle_led, led_label)


    def stop_blink_led(self,led_label):
        self.rt[led_label.objectName()].stop()

    #if period == 0 message will be shown until cleared or overwriten.
    def display_lcd(self,message,period):
        self.view.lcd_screen.display(message)
        if(period != 0):
            self.lcd_timer = threading.Timer(period, self.clear_display)
            print("Starting {}s timer for LCD".format(period))
            self.lcd_timer.start()

    def clear_display(self):
        self.view.lcd_screen.display('')


            

        


            

