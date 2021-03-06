# Costa Rica Institute of Technology
# MP-6118 Validation and Verification in Software Engineering
# Students: 
#           - David Martínez
#           - Jose Martínez
# Project:  Smart Embedded Systems Security Alarm         
from PyQt5 import QtCore, QtGui, QtWidgets
from keyboard import Keyboard
from registers import Registers
from alarm import Alarm
from functools import partial
import logging

logger = logging.getLogger(__name__) 

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(768, 593)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lcd_screen = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_screen.setGeometry(QtCore.QRect(20, 60, 271, 81))
        self.lcd_screen.setStyleSheet("font: bold 4pt \"Tlwg Mono\";")
        self.lcd_screen.setObjectName("lcd_screen")
        self.lcd_screen.setDigitCount(8)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(-90, 250, 1051, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(630, 10, 131, 231))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.key_escape = QtWidgets.QPushButton(self.layoutWidget)
        self.key_escape.setStyleSheet("font: 18pt \"Tlwg Mono\";")
        self.key_escape.setObjectName("key_escape")
        self.verticalLayout.addWidget(self.key_escape)
        self.key_enter = QtWidgets.QPushButton(self.layoutWidget)
        self.key_enter.setStyleSheet("font: 18pt \"Tlwg Mono\";")
        self.key_enter.setObjectName("key_enter")
        self.verticalLayout.addWidget(self.key_enter)
        self.key_panic = QtWidgets.QPushButton(self.layoutWidget)
        self.key_panic.setStyleSheet("font: 18pt \"Tlwg Mono\";")
        self.key_panic.setObjectName("key_panic")
        self.verticalLayout.addWidget(self.key_panic)
        self.key_fire = QtWidgets.QPushButton(self.layoutWidget)
        self.key_fire.setStyleSheet("font: 18pt \"Tlwg Mono\";")
        self.key_fire.setObjectName("key_fire")
        self.verticalLayout.addWidget(self.key_fire)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 270, 341, 51))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.layoutWidget1)
        self.label.setStyleSheet("font: bold 11pt \"Tlwg Mono\";")
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.battery_percentage_simulation = QtWidgets.QSlider(self.layoutWidget1)
        self.battery_percentage_simulation.setStyleSheet("QSlider::groove:horizontal {\n"
"    border: 1px solid #999999;\n"
"    height: 8px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #B1B1B1, stop:1 #c4c4c4);\n"
"    margin: 2px 0;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
"    border: 1px solid #5c5c5c;\n"
"    width: 18px;\n"
"    margin: -2px 0; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */\n"
"    border-radius: 3px;\n"
"}")
        self.battery_percentage_simulation.setOrientation(QtCore.Qt.Horizontal)
        self.battery_percentage_simulation.setObjectName("battery_percentage_simulation")
        self.verticalLayout_2.addWidget(self.battery_percentage_simulation)
        self.layoutWidget2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(380, 10, 241, 231))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget2)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.key_1 = QtWidgets.QToolButton(self.layoutWidget2)
        self.key_1.setStyleSheet("QToolButton {\n"
"font: 18pt \"Tlwg Mono\"; \n"
"border-radius: 10px; \n"
"border-color: black;\n"
"border-width: 2px;\n"
"border-style: outset;\n"
"background-color: rgb(211, 215, 207); \n"
"}\n"
"QToolButton::pressed {\n"
"  font: 18pt \"Tlwg Mono\"; \n"
"  border-radius: 10px; \n"
"  border-color: black;\n"
"  border-width: 2px;\n"
"  border-style: inset;\n"
"  background-color: rgb(238, 238, 236);\n"
"}")
        self.key_1.setAutoRepeatDelay(305)
        self.key_1.setAutoRaise(False)
        self.key_1.setObjectName("key_1")
        self.gridLayout.addWidget(self.key_1, 0, 0, 1, 1)
        self.key_4 = QtWidgets.QToolButton(self.layoutWidget2)
        self.key_4.setStyleSheet("QToolButton {\n"
"font: 18pt \"Tlwg Mono\"; \n"
"border-radius: 10px; \n"
"border-color: black;\n"
"border-width: 2px;\n"
"border-style: outset;\n"
"background-color: rgb(211, 215, 207); \n"
"}\n"
"QToolButton::pressed {\n"
"  font: 18pt \"Tlwg Mono\"; \n"
"  border-radius: 10px; \n"
"  border-color: black;\n"
"  border-width: 2px;\n"
"  border-style: inset;\n"
"  background-color: rgb(238, 238, 236);\n"
"}")
        self.key_4.setObjectName("key_4")
        self.gridLayout.addWidget(self.key_4, 1, 0, 1, 1)
        self.key_9 = QtWidgets.QToolButton(self.layoutWidget2)
        self.key_9.setStyleSheet("QToolButton {\n"
"font: 18pt \"Tlwg Mono\"; \n"
"border-radius: 10px; \n"
"border-color: black;\n"
"border-width: 2px;\n"
"border-style: outset;\n"
"background-color: rgb(211, 215, 207); \n"
"}\n"
"QToolButton::pressed {\n"
"  font: 18pt \"Tlwg Mono\"; \n"
"  border-radius: 10px; \n"
"  border-color: black;\n"
"  border-width: 2px;\n"
"  border-style: inset;\n"
"  background-color: rgb(238, 238, 236);\n"
"}")
        self.key_9.setObjectName("key_9")
        self.gridLayout.addWidget(self.key_9, 2, 2, 1, 1)
        self.key_0 = QtWidgets.QToolButton(self.layoutWidget2)
        self.key_0.setStyleSheet("QToolButton {\n"
"font: 18pt \"Tlwg Mono\"; \n"
"border-radius: 10px; \n"
"border-color: black;\n"
"border-width: 2px;\n"
"border-style: outset;\n"
"background-color: rgb(211, 215, 207); \n"
"}\n"
"QToolButton::pressed {\n"
"  font: 18pt \"Tlwg Mono\"; \n"
"  border-radius: 10px; \n"
"  border-color: black;\n"
"  border-width: 2px;\n"
"  border-style: inset;\n"
"  background-color: rgb(238, 238, 236);\n"
"}")
        self.key_0.setObjectName("key_0")
        self.gridLayout.addWidget(self.key_0, 3, 1, 1, 1)
        self.key_2 = QtWidgets.QToolButton(self.layoutWidget2)
        self.key_2.setStyleSheet("QToolButton {\n"
"font: 18pt \"Tlwg Mono\"; \n"
"border-radius: 10px; \n"
"border-color: black;\n"
"border-width: 2px;\n"
"border-style: outset;\n"
"background-color: rgb(211, 215, 207); \n"
"}\n"
"QToolButton::pressed {\n"
"  font: 18pt \"Tlwg Mono\"; \n"
"  border-radius: 10px; \n"
"  border-color: black;\n"
"  border-width: 2px;\n"
"  border-style: inset;\n"
"  background-color: rgb(238, 238, 236);\n"
"}")
        self.key_2.setObjectName("key_2")
        self.gridLayout.addWidget(self.key_2, 0, 1, 1, 1)
        self.key_3 = QtWidgets.QToolButton(self.layoutWidget2)
        self.key_3.setStyleSheet("QToolButton {\n"
"font: 18pt \"Tlwg Mono\"; \n"
"border-radius: 10px; \n"
"border-color: black;\n"
"border-width: 2px;\n"
"border-style: outset;\n"
"background-color: rgb(211, 215, 207); \n"
"}\n"
"QToolButton::pressed {\n"
"  font: 18pt \"Tlwg Mono\"; \n"
"  border-radius: 10px; \n"
"  border-color: black;\n"
"  border-width: 2px;\n"
"  border-style: inset;\n"
"  background-color: rgb(238, 238, 236);\n"
"}")
        self.key_3.setObjectName("key_3")
        self.gridLayout.addWidget(self.key_3, 0, 2, 1, 1)
        self.key_8 = QtWidgets.QToolButton(self.layoutWidget2)
        self.key_8.setStyleSheet("QToolButton {\n"
"font: 18pt \"Tlwg Mono\"; \n"
"border-radius: 10px; \n"
"border-color: black;\n"
"border-width: 2px;\n"
"border-style: outset;\n"
"background-color: rgb(211, 215, 207); \n"
"}\n"
"QToolButton::pressed {\n"
"  font: 18pt \"Tlwg Mono\"; \n"
"  border-radius: 10px; \n"
"  border-color: black;\n"
"  border-width: 2px;\n"
"  border-style: inset;\n"
"  background-color: rgb(238, 238, 236);\n"
"}")
        self.key_8.setObjectName("key_8")
        self.gridLayout.addWidget(self.key_8, 2, 1, 1, 1)
        self.key_5 = QtWidgets.QToolButton(self.layoutWidget2)
        self.key_5.setStyleSheet("QToolButton {\n"
"font: 18pt \"Tlwg Mono\"; \n"
"border-radius: 10px; \n"
"border-color: black;\n"
"border-width: 2px;\n"
"border-style: outset;\n"
"background-color: rgb(211, 215, 207); \n"
"}\n"
"QToolButton::pressed {\n"
"  font: 18pt \"Tlwg Mono\"; \n"
"  border-radius: 10px; \n"
"  border-color: black;\n"
"  border-width: 2px;\n"
"  border-style: inset;\n"
"  background-color: rgb(238, 238, 236);\n"
"}")
        self.key_5.setObjectName("key_5")
        self.gridLayout.addWidget(self.key_5, 1, 1, 1, 1)
        self.key_pound = QtWidgets.QToolButton(self.layoutWidget2)
        self.key_pound.setStyleSheet("QToolButton {\n"
"font: 18pt \"Tlwg Mono\"; \n"
"border-radius: 10px; \n"
"border-color: black;\n"
"border-width: 2px;\n"
"border-style: outset;\n"
"background-color: rgb(211, 215, 207); \n"
"}\n"
"QToolButton::pressed {\n"
"  font: 18pt \"Tlwg Mono\"; \n"
"  border-radius: 10px; \n"
"  border-color: black;\n"
"  border-width: 2px;\n"
"  border-style: inset;\n"
"  background-color: rgb(238, 238, 236);\n"
"}")
        self.key_pound.setObjectName("key_pound")
        self.gridLayout.addWidget(self.key_pound, 3, 2, 1, 1)
        self.key_star = QtWidgets.QToolButton(self.layoutWidget2)
        self.key_star.setStyleSheet("QToolButton {\n"
"font: 18pt \"Tlwg Mono\"; \n"
"border-radius: 10px; \n"
"border-color: black;\n"
"border-width: 2px;\n"
"border-style: outset;\n"
"background-color: rgb(211, 215, 207); \n"
"}\n"
"QToolButton::pressed {\n"
"  font: 18pt \"Tlwg Mono\"; \n"
"  border-radius: 10px; \n"
"  border-color: black;\n"
"  border-width: 2px;\n"
"  border-style: inset;\n"
"  background-color: rgb(238, 238, 236);\n"
"}")
        self.key_star.setObjectName("key_star")
        self.gridLayout.addWidget(self.key_star, 3, 0, 1, 1)
        self.key_6 = QtWidgets.QToolButton(self.layoutWidget2)
        self.key_6.setStyleSheet("QToolButton {\n"
"font: 18pt \"Tlwg Mono\"; \n"
"border-radius: 10px; \n"
"border-color: black;\n"
"border-width: 2px;\n"
"border-style: outset;\n"
"background-color: rgb(211, 215, 207); \n"
"}\n"
"QToolButton::pressed {\n"
"  font: 18pt \"Tlwg Mono\"; \n"
"  border-radius: 10px; \n"
"  border-color: black;\n"
"  border-width: 2px;\n"
"  border-style: inset;\n"
"  background-color: rgb(238, 238, 236);\n"
"}")
        self.key_6.setObjectName("key_6")
        self.gridLayout.addWidget(self.key_6, 1, 2, 1, 1)
        self.key_7 = QtWidgets.QToolButton(self.layoutWidget2)
        self.key_7.setStyleSheet("QToolButton {\n"
"font: 18pt \"Tlwg Mono\"; \n"
"border-radius: 10px; \n"
"border-color: black;\n"
"border-width: 2px;\n"
"border-style: outset;\n"
"background-color: rgb(211, 215, 207); \n"
"}\n"
"QToolButton::pressed {\n"
"  font: 18pt \"Tlwg Mono\"; \n"
"  border-radius: 10px; \n"
"  border-color: black;\n"
"  border-width: 2px;\n"
"  border-style: inset;\n"
"  background-color: rgb(238, 238, 236);\n"
"}")
        self.key_7.setObjectName("key_7")
        self.gridLayout.addWidget(self.key_7, 2, 0, 1, 1)
        self.layoutWidget3 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget3.setGeometry(QtCore.QRect(20, 340, 731, 61))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_5.setStyleSheet("font: bold 11pt \"Tlwg Mono\";")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.sensor_1 = QtWidgets.QCheckBox(self.layoutWidget3)
        self.sensor_1.setStyleSheet("font: 12pt \"Tlwg Mono\";")
        self.sensor_1.setObjectName("sensor_1")
        self.horizontalLayout_3.addWidget(self.sensor_1)
        self.sensor_2 = QtWidgets.QCheckBox(self.layoutWidget3)
        self.sensor_2.setStyleSheet("font: 12pt \"Tlwg Mono\";")
        self.sensor_2.setObjectName("sensor_2")
        self.horizontalLayout_3.addWidget(self.sensor_2)
        self.sensor_3 = QtWidgets.QCheckBox(self.layoutWidget3)
        self.sensor_3.setStyleSheet("font: 12pt \"Tlwg Mono\";")
        self.sensor_3.setObjectName("sensor_3")
        self.horizontalLayout_3.addWidget(self.sensor_3)
        self.sensor_4 = QtWidgets.QCheckBox(self.layoutWidget3)
        self.sensor_4.setStyleSheet("font: 12pt \"Tlwg Mono\";")
        self.sensor_4.setObjectName("sensor_4")
        self.horizontalLayout_3.addWidget(self.sensor_4)
        self.sensor_5 = QtWidgets.QCheckBox(self.layoutWidget3)
        self.sensor_5.setStyleSheet("font: 12pt \"Tlwg Mono\";")
        self.sensor_5.setObjectName("sensor_5")
        self.horizontalLayout_3.addWidget(self.sensor_5)
        self.sensor_6 = QtWidgets.QCheckBox(self.layoutWidget3)
        self.sensor_6.setStyleSheet("font: 12pt \"Tlwg Mono\";")
        self.sensor_6.setObjectName("sensor_6")
        self.horizontalLayout_3.addWidget(self.sensor_6)
        self.sensor_7 = QtWidgets.QCheckBox(self.layoutWidget3)
        self.sensor_7.setStyleSheet("font: 12pt \"Tlwg Mono\";")
        self.sensor_7.setObjectName("sensor_7")
        self.horizontalLayout_3.addWidget(self.sensor_7)
        self.sensor_8 = QtWidgets.QCheckBox(self.layoutWidget3)
        self.sensor_8.setStyleSheet("font: 12pt \"Tlwg Mono\";")
        self.sensor_8.setObjectName("sensor_8")
        self.horizontalLayout_3.addWidget(self.sensor_8)
        self.sensor_9 = QtWidgets.QCheckBox(self.layoutWidget3)
        self.sensor_9.setStyleSheet("font: 12pt \"Tlwg Mono\";")
        self.sensor_9.setObjectName("sensor_9")
        self.horizontalLayout_3.addWidget(self.sensor_9)
        self.sensor_10 = QtWidgets.QCheckBox(self.layoutWidget3)
        self.sensor_10.setStyleSheet("font: 12pt \"Tlwg Mono\";")
        self.sensor_10.setObjectName("sensor_10")
        self.horizontalLayout_3.addWidget(self.sensor_10)
        self.sensor_11 = QtWidgets.QCheckBox(self.layoutWidget3)
        self.sensor_11.setStyleSheet("font: 12pt \"Tlwg Mono\";")
        self.sensor_11.setObjectName("sensor_11")
        self.horizontalLayout_3.addWidget(self.sensor_11)
        self.sensor_12 = QtWidgets.QCheckBox(self.layoutWidget3)
        self.sensor_12.setStyleSheet("font: 12pt \"Tlwg Mono\";")
        self.sensor_12.setObjectName("sensor_12")
        self.horizontalLayout_3.addWidget(self.sensor_12)
        self.sensor_13 = QtWidgets.QCheckBox(self.layoutWidget3)
        self.sensor_13.setStyleSheet("font: 12pt \"Tlwg Mono\";")
        self.sensor_13.setObjectName("sensor_13")
        self.horizontalLayout_3.addWidget(self.sensor_13)
        self.sensor_14 = QtWidgets.QCheckBox(self.layoutWidget3)
        self.sensor_14.setStyleSheet("font: 12pt \"Tlwg Mono\";")
        self.sensor_14.setObjectName("sensor_14")
        self.horizontalLayout_3.addWidget(self.sensor_14)
        self.sensor_15 = QtWidgets.QCheckBox(self.layoutWidget3)
        self.sensor_15.setStyleSheet("font: 12pt \"Tlwg Mono\";")
        self.sensor_15.setObjectName("sensor_15")
        self.horizontalLayout_3.addWidget(self.sensor_15)
        self.sensor_16 = QtWidgets.QCheckBox(self.layoutWidget3)
        self.sensor_16.setStyleSheet("font: 12pt \"Tlwg Mono\";")
        self.sensor_16.setObjectName("sensor_16")
        self.horizontalLayout_3.addWidget(self.sensor_16)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(21, 31, 16, 17))
        self.label_2.setStyleSheet("font: 11pt bold \"Tlwg Mono\";")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.layoutWidget4 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget4.setGeometry(QtCore.QRect(20, 20, 341, 35))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.battery_percentage = QtWidgets.QProgressBar(self.layoutWidget4)
        self.battery_percentage.setStyleSheet("QProgressBar {\n"
"    font: bold 11pt \"Tlwg Mono\";\n"
"    border: 2px solid grey;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk {\n"
"    font: bold 11pt \"Tlwg Mono\";\n"
"    background-color: rgb(196, 233, 190);\n"
"    width: 10px;\n"
"    margin: 0.5px;\n"
"}")
        self.battery_percentage.setProperty("value", 100)
        self.battery_percentage.setObjectName("battery_percentage")
        self.horizontalLayout.addWidget(self.battery_percentage)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget4)
        self.label_6.setStyleSheet("font: bold 11pt \"Tlwg Mono\";")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.layoutWidget5 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget5.setGeometry(QtCore.QRect(290, 60, 71, 81))
        self.layoutWidget5.setObjectName("layoutWidget5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget5)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lcd_mode_0 = QtWidgets.QLabel(self.layoutWidget5)
        self.lcd_mode_0.setStyleSheet("font: bold 11pt \"Tlwg Mono\";")
        self.lcd_mode_0.setObjectName("lcd_mode_0")
        self.verticalLayout_4.addWidget(self.lcd_mode_0, 0, QtCore.Qt.AlignHCenter)
        self.lcd_mode_1 = QtWidgets.QLabel(self.layoutWidget5)
        self.lcd_mode_1.setStyleSheet("font: bold 11pt \"Tlwg Mono\";")
        self.lcd_mode_1.setObjectName("lcd_mode_1")
        self.verticalLayout_4.addWidget(self.lcd_mode_1, 0, QtCore.Qt.AlignHCenter)
        self.lcd_error = QtWidgets.QLabel(self.layoutWidget5)
        self.lcd_error.setStyleSheet("font: bold 11pt \"Tlwg Mono\";")
        self.lcd_error.setObjectName("lcd_error")
        self.verticalLayout_4.addWidget(self.lcd_error, 0, QtCore.Qt.AlignHCenter)
        self.layoutWidget6 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget6.setGeometry(QtCore.QRect(20, 200, 351, 41))
        self.layoutWidget6.setObjectName("layoutWidget6")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget6)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget6)
        self.label_4.setStyleSheet("font: 12pt bold \"Tlwg Mono\";")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4, 0, QtCore.Qt.AlignHCenter)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget6)
        self.label_3.setStyleSheet("font: 12pt bold \"Tlwg Mono\";")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3, 0, QtCore.Qt.AlignHCenter)
        self.led_battery = QtWidgets.QLabel(self.centralwidget)
        self.led_battery.setGeometry(QtCore.QRect(260, 150, 41, 41))
        self.led_battery.setStyleSheet("")
        self.led_battery.setText("")
        self.led_battery.setPixmap(QtGui.QPixmap("./icon/rsz_165-1653782_green-led-icon-png.png"))
        self.led_battery.setObjectName("led_battery")
        self.led_armed = QtWidgets.QLabel(self.centralwidget)
        self.led_armed.setGeometry(QtCore.QRect(80, 150, 41, 41))
        self.led_armed.setStyleSheet("")
        self.led_armed.setText("")
        self.led_armed.setPixmap(QtGui.QPixmap("./icon/rsz_165-1653782_green-led-icon-png.png"))
        self.led_armed.setObjectName("led_armed")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 420, 339, 28))
        self.label_7.setStyleSheet("font: bold 11pt \"Tlwg Mono\";")
        self.label_7.setObjectName("label_7")
        self.sound_activated = QtWidgets.QLabel(self.centralwidget)
        self.sound_activated.setGeometry(QtCore.QRect(220, 450, 120, 80))
        self.sound_activated.setStyleSheet("border-radius: 10px; \n"
"border-color: black;\n"
"border-width: 2px;\n"
"border-style: outset;")
        self.sound_activated.setText("")
        self.sound_activated.setPixmap(QtGui.QPixmap("./icon/rsz_download.jpg"))
        self.sound_activated.setObjectName("sound_activated")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(-150, 320, 1051, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(-20, 400, 1051, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.sound_deactivated = QtWidgets.QLabel(self.centralwidget)
        self.sound_deactivated.setGeometry(QtCore.QRect(450, 450, 120, 80))
        self.sound_deactivated.setStyleSheet("border-radius: 10px; \n"
"border-color: black;\n"
"border-width: 2px;\n"
"border-style: outset;")
        self.sound_deactivated.setText("")
        self.sound_deactivated.setPixmap(QtGui.QPixmap("./icon/rsz_11download.png"))
        self.sound_deactivated.setObjectName("sound_deactivated")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 768, 22))
        self.menubar.setObjectName("menubar")
        self.menuSISTEMA_DE_ALARMA = QtWidgets.QMenu(self.menubar)
        self.menuSISTEMA_DE_ALARMA.setObjectName("menuSISTEMA_DE_ALARMA")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.menubar.addAction(self.menuSISTEMA_DE_ALARMA.menuAction())

        self.retranslateUi(MainWindow)
        self.battery_percentage_simulation.sliderMoved['int'].connect(self.battery_percentage.setValue)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        self.battery_percentage_simulation.setValue(100)

        self.alarm = Alarm(self)
   
        self.key_1.clicked.connect(partial(self.key_clicked, self.key_1))
        self.key_2.clicked.connect(partial(self.key_clicked, self.key_2))
        self.key_3.clicked.connect(partial(self.key_clicked, self.key_3))
        self.key_4.clicked.connect(partial(self.key_clicked, self.key_4))
        self.key_5.clicked.connect(partial(self.key_clicked, self.key_5))
        self.key_6.clicked.connect(partial(self.key_clicked, self.key_6))
        self.key_7.clicked.connect(partial(self.key_clicked, self.key_7))
        self.key_8.clicked.connect(partial(self.key_clicked, self.key_8))
        self.key_9.clicked.connect(partial(self.key_clicked, self.key_9))
        self.key_0.clicked.connect(partial(self.key_clicked, self.key_0))
        self.key_pound.clicked.connect(partial(self.key_clicked, self.key_pound))
        self.key_star.clicked.connect(partial(self.key_clicked, self.key_star))
        self.key_escape.clicked.connect(partial(self.key_clicked, self.key_escape))
        self.key_enter.clicked.connect(partial(self.key_clicked, self.key_enter))
        self.key_panic.clicked.connect(partial(self.key_clicked, self.key_panic))
        self.key_fire.clicked.connect(partial(self.key_clicked, self.key_fire))

        self.sensor_1.clicked.connect(partial(self.sensor_activated, self.sensor_1))
        self.sensor_2.clicked.connect(partial(self.sensor_activated, self.sensor_2))
        self.sensor_3.clicked.connect(partial(self.sensor_activated, self.sensor_3))
        self.sensor_4.clicked.connect(partial(self.sensor_activated, self.sensor_4))
        self.sensor_5.clicked.connect(partial(self.sensor_activated, self.sensor_5))
        self.sensor_6.clicked.connect(partial(self.sensor_activated, self.sensor_6))
        self.sensor_7.clicked.connect(partial(self.sensor_activated, self.sensor_7))
        self.sensor_8.clicked.connect(partial(self.sensor_activated, self.sensor_8))
        self.sensor_9.clicked.connect(partial(self.sensor_activated, self.sensor_9))
        self.sensor_10.clicked.connect(partial(self.sensor_activated, self.sensor_10))
        self.sensor_11.clicked.connect(partial(self.sensor_activated, self.sensor_11))
        self.sensor_12.clicked.connect(partial(self.sensor_activated, self.sensor_12))
        self.sensor_13.clicked.connect(partial(self.sensor_activated, self.sensor_13))
        self.sensor_14.clicked.connect(partial(self.sensor_activated, self.sensor_14))
        self.sensor_15.clicked.connect(partial(self.sensor_activated, self.sensor_15))
        self.sensor_16.clicked.connect(partial(self.sensor_activated, self.sensor_16))

        self.battery_percentage.valueChanged.connect(self.battery_changed)

    # Function that reads information from the keyboard 
    def key_clicked(self,key):
        if (key == self.key_1): self.alarm.key_pressed('1')
        if (key == self.key_2): self.alarm.key_pressed('2')
        if (key == self.key_3): self.alarm.key_pressed('3')
        if (key == self.key_4): self.alarm.key_pressed('4')
        if (key == self.key_5): self.alarm.key_pressed('5')
        if (key == self.key_6): self.alarm.key_pressed('6')
        if (key == self.key_7): self.alarm.key_pressed('7')
        if (key == self.key_8): self.alarm.key_pressed('8')
        if (key == self.key_9): self.alarm.key_pressed('9')
        if (key == self.key_0): self.alarm.key_pressed('0')
        if (key == self.key_pound): self.alarm.key_pressed('#')
        if (key == self.key_star): self.alarm.key_pressed('*')
        if (key == self.key_escape): self.alarm.key_pressed('ESC')
        if (key == self.key_enter): self.alarm.key_pressed('ENTER')
        if (key == self.key_panic): self.alarm.key_pressed('PANIC')
        if (key == self.key_fire): self.alarm.key_pressed('FIRE')


    # Function that reads information from the sensors button
    def sensor_activated(self,sensor):
        if (sensor == self.sensor_1 and self.sensor_1.isChecked()): self.alarm.sensor_activated(1)
        if (sensor == self.sensor_2 and self.sensor_2.isChecked()): self.alarm.sensor_activated(2)
        if (sensor == self.sensor_3 and self.sensor_3.isChecked()): self.alarm.sensor_activated(3)
        if (sensor == self.sensor_4 and self.sensor_4.isChecked()): self.alarm.sensor_activated(4)
        if (sensor == self.sensor_5 and self.sensor_5.isChecked()): self.alarm.sensor_activated(5)
        if (sensor == self.sensor_6 and self.sensor_6.isChecked()): self.alarm.sensor_activated(6)
        if (sensor == self.sensor_7 and self.sensor_7.isChecked()): self.alarm.sensor_activated(7)
        if (sensor == self.sensor_8 and self.sensor_8.isChecked()): self.alarm.sensor_activated(8)
        if (sensor == self.sensor_9 and self.sensor_9.isChecked()): self.alarm.sensor_activated(9)
        if (sensor == self.sensor_10 and self.sensor_10.isChecked()): self.alarm.sensor_activated(10)
        if (sensor == self.sensor_11 and self.sensor_11.isChecked()): self.alarm.sensor_activated(11)
        if (sensor == self.sensor_12 and self.sensor_12.isChecked()): self.alarm.sensor_activated(12)
        if (sensor == self.sensor_13 and self.sensor_13.isChecked()): self.alarm.sensor_activated(13)
        if (sensor == self.sensor_14 and self.sensor_14.isChecked()): self.alarm.sensor_activated(14)
        if (sensor == self.sensor_15 and self.sensor_15.isChecked()): self.alarm.sensor_activated(15)
        if (sensor == self.sensor_16 and self.sensor_16.isChecked()): self.alarm.sensor_activated(16)

    def battery_changed(self):
        self.alarm.check_battery()

    def start_alarm(self, sensor):
        self.alarm.start_alarm(sensor)

    def refresh_alarm(self):
        self.alarm.refresh_alarm()

    def blink_led(self, led_label, period):
        self.alarm.blink_led(led_label, period)

    def stop_blink_led(self, led_label):
        self.alarm.stop_blink_led(led_label)

    def display_lcd(self,message,period):
        self.alarm.display_lcd(message,period)

    # Retranslate UI
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.key_escape.setText(_translate("MainWindow", "ESC"))
        self.key_enter.setText(_translate("MainWindow", "ENTER"))
        self.key_panic.setText(_translate("MainWindow", "PÁNICO"))
        self.key_fire.setText(_translate("MainWindow", "BOMBEROS"))
        self.label.setText(_translate("MainWindow", "SIMULACIÓN ESTADO DE LA BATERÍA "))
        self.key_1.setText(_translate("MainWindow", "1"))
        self.key_4.setText(_translate("MainWindow", "4"))
        self.key_9.setText(_translate("MainWindow", "9"))
        self.key_0.setText(_translate("MainWindow", "0"))
        self.key_2.setText(_translate("MainWindow", "2"))
        self.key_3.setText(_translate("MainWindow", "3"))
        self.key_8.setText(_translate("MainWindow", "8"))
        self.key_5.setText(_translate("MainWindow", "5"))
        self.key_pound.setText(_translate("MainWindow", "#"))
        self.key_star.setText(_translate("MainWindow", "*"))
        self.key_6.setText(_translate("MainWindow", "6"))
        self.key_7.setText(_translate("MainWindow", "7"))
        self.label_5.setText(_translate("MainWindow", "SIMULACIÓN ESTADO DE LOS SENSORES"))
        self.sensor_1.setText(_translate("MainWindow", "1"))
        self.sensor_2.setText(_translate("MainWindow", "2"))
        self.sensor_3.setText(_translate("MainWindow", "3"))
        self.sensor_4.setText(_translate("MainWindow", "4"))
        self.sensor_5.setText(_translate("MainWindow", "5"))
        self.sensor_6.setText(_translate("MainWindow", "6"))
        self.sensor_7.setText(_translate("MainWindow", "7"))
        self.sensor_8.setText(_translate("MainWindow", "8"))
        self.sensor_9.setText(_translate("MainWindow", "9"))
        self.sensor_10.setText(_translate("MainWindow", "10"))
        self.sensor_11.setText(_translate("MainWindow", "11"))
        self.sensor_12.setText(_translate("MainWindow", "12"))
        self.sensor_13.setText(_translate("MainWindow", "13"))
        self.sensor_14.setText(_translate("MainWindow", "14"))
        self.sensor_15.setText(_translate("MainWindow", "15"))
        self.sensor_16.setText(_translate("MainWindow", "16"))
        self.label_6.setText(_translate("MainWindow", "BATERÍA"))
        self.lcd_mode_0.setText(_translate("MainWindow", "MODO 0"))
        self.lcd_mode_1.setText(_translate("MainWindow", "MODO 1"))
        self.lcd_error.setText(_translate("MainWindow", "ERROR"))
        self.label_4.setText(_translate("MainWindow", "ARMADA"))
        self.label_3.setText(_translate("MainWindow", "BATERÍA"))
        self.label_7.setText(_translate("MainWindow", "SIMULACIÓN ESTADO DE LA BOCINA "))
        self.menuSISTEMA_DE_ALARMA.setTitle(_translate("MainWindow", "SISTEMA DE SEGURIDAD PARA HOGARES SSH-101"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
