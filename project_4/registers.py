from enum import Enum, unique

@unique
class Alarm_Mode(Enum):
    NONE = 0
    CHANGE_PIN = 1
    CHANGE_ZONES = 2
    CHANGE_NUMBER = 3
    CHANGE_NUMBER_FIRE = 4
    CHANGE_NUMBER_PANIC = 5
    ARMED_ACTIVE = 6
    DISARMED_ACTIVE = 7
    FIRE_ACTIVE = 8
    PANIC_ACTIVE = 9
    DISABLED = 10
    CHANGE_ZONES_0 = 11
    CHANGE_ZONES_1 = 12
    # EMERGENCY_ACTIVE = 10
    # ERROR = 11

class Registers(object):
    ALARM_STATE = "UNARMED"
    OP_MODE = 0
    ACTIVE_SENSOR = [1]
    USER_NUMBER = 1
    CALL_CENTER_NUMBER = ['1', '2', '3', '4', '5', '6', '7', '8']
    TEMP_CALL_CENTER_NUMBER = []
    NEW_NUMBER_COUNT = 0
    IN_CHANGE_NUMBER = False
    PIN = ['1', '2', '3', '4']
    ZONE_0 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    ZONE_1 = []
    IN_CHANGE_ZONE = False
    IN_CHANGE_ZONE_0 = False
    IN_CHANGE_ZONE_1 = False
    IN_CHANGE_ZONE_COUNT = 0
    SENSOR_COUNT = 0
    SENSOR_NUMBER = []
    ALERT = False
    MAIN_ENTRANCE = 1
    TEMP_PIN = []
    NEW_PIN = []
    NEW_PIN_COUNT = 0
    NEW_PIN_CONFIRMATION = []
    NEW_PIN_CONFIRMATION_COUNT = 0
    CONFIRMATION = False
    IN_CHANGE_PIN = False
    ERROR_STATE: False
    KEY_COUNT = 0
    ALARM_MODE = Alarm_Mode.NONE
    IN_ARMED_SELECT = False
    MODE_SELECTED = False
    
