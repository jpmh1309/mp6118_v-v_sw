# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'alarm.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(768, 457)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lcd_screen = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_screen.setGeometry(QtCore.QRect(20, 60, 271, 81))
        self.lcd_screen.setStyleSheet("font: bold 11pt \"Tlwg Mono\";")
        self.lcd_screen.setObjectName("lcd_screen")
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
        self.key_start = QtWidgets.QToolButton(self.layoutWidget2)
        self.key_start.setStyleSheet("QToolButton {\n"
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
        self.key_start.setObjectName("key_start")
        self.gridLayout.addWidget(self.key_start, 3, 0, 1, 1)
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
        self.layoutWidget3.setGeometry(QtCore.QRect(20, 330, 741, 57))
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
        self.battery_percentage.setProperty("value", 24)
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
        self.led_battery.setStyleSheet("QLabel {background-color : yellow; border-color : black; border-width : 1px; border-style : solid; border-radius : 10px; min-height: 20px; min-width: 20px}")
        self.led_battery.setText("")
        self.led_battery.setObjectName("led_battery")
        self.led_armed = QtWidgets.QLabel(self.centralwidget)
        self.led_armed.setGeometry(QtCore.QRect(80, 150, 41, 41))
        self.led_armed.setStyleSheet("QLabel {background-color : yellow; border-color : black; border-width : 1px; border-style : solid; border-radius : 10px; min-height: 20px; min-width: 20px}")
        self.led_armed.setText("")
        self.led_armed.setObjectName("led_armed")
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
        self.sensor_2.stateChanged['int'].connect(self.led_battery.hide)
        self.sensor_2.stateChanged['int'].connect(self.led_battery.show)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.key_escape.setText(_translate("MainWindow", "ESC"))
        self.key_enter.setText(_translate("MainWindow", "ENTER"))
        self.key_panic.setText(_translate("MainWindow", "PANICO"))
        self.key_fire.setText(_translate("MainWindow", "BOMBEROS"))
        self.label.setText(_translate("MainWindow", "SIMULACION ESTADO DE LA BATERIA "))
        self.key_1.setText(_translate("MainWindow", "1"))
        self.key_4.setText(_translate("MainWindow", "4"))
        self.key_9.setText(_translate("MainWindow", "9"))
        self.key_0.setText(_translate("MainWindow", "0"))
        self.key_2.setText(_translate("MainWindow", "2"))
        self.key_3.setText(_translate("MainWindow", "3"))
        self.key_8.setText(_translate("MainWindow", "8"))
        self.key_5.setText(_translate("MainWindow", "5"))
        self.key_pound.setText(_translate("MainWindow", "#"))
        self.key_start.setText(_translate("MainWindow", "*"))
        self.key_6.setText(_translate("MainWindow", "6"))
        self.key_7.setText(_translate("MainWindow", "7"))
        self.label_5.setText(_translate("MainWindow", "SIMULACION ESTADO DE LOS SENSORES"))
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
        self.label_6.setText(_translate("MainWindow", "BATERIA"))
        self.lcd_mode_0.setText(_translate("MainWindow", "MODO 0"))
        self.lcd_mode_1.setText(_translate("MainWindow", "MODO 1"))
        self.lcd_error.setText(_translate("MainWindow", "ERROR"))
        self.label_4.setText(_translate("MainWindow", "ARMADA"))
        self.label_3.setText(_translate("MainWindow", "BATERIA"))
        self.menuSISTEMA_DE_ALARMA.setTitle(_translate("MainWindow", "SISTEMA DE SEGURIDAD PARA HOGARES SSH-101"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
