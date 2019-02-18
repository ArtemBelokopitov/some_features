#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import smtplib

from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtGui import *
import Parameters as Parameters
import SendEmail as SendEmail

class SendEmailButton():

    def button(self):

        send_button = QPushButton('Отправить письмо', self)
        button_color = Parameters.Color().whatcolor()
        send_button.setStyleSheet("background-color: {0}".format(button_color))
        return send_button


class SendEmailWindow(QWidget):

    def __init__(self):

        self.homepath = QtCore.QDir.homePath()

        super(QWidget, self).__init__()

        self.setFont(QFont('Century Gothic', 10))

        windowW1 = Parameters.ParameterSize().ww()
        windowH1 = Parameters.ParameterSize().wh()

        button_color = Parameters.Color().whatcolor()

        self.setFixedSize(windowW1 * 0.2395833333333333, windowH1 * 0.4259259259259259)

        log_pas = QHBoxLayout()
        btns = QHBoxLayout()
        vbox = QVBoxLayout()

        self.uremail_line = QLineEdit()
        self.urpassword_line = QLineEdit()
        self.urpassword_line.setEchoMode(QLineEdit.Password)
        self.address_line = QLineEdit()
        btn_send = QPushButton('Отправить', self)

        btn_send.setStyleSheet("background-color: {0}".format(button_color))

        log_pas.addWidget(self.uremail_line)
        log_pas.addWidget(self.urpassword_line)
        btns.addWidget(btn_send)

        vbox.addLayout(log_pas)
        vbox.addWidget(self.address_line, alignment=QtCore.Qt.AlignHCenter)
        vbox.addLayout(btns)

        self.setLayout(vbox)

        btn_send.clicked.connect(self.send)


    def send(self):

        uremail = self.uremail_line.text()
        urpassword = self.urpassword_line.text()
        address = self.address_line.text()

        with open(self.homepath + "/Desktop/проект/ProgrammFiles/Mail.txt", "w") as mailfile:

            mailfile.write(uremail+"\n"+urpassword+"\n"+address)

        SendEmail.send_letter()

        self.close()


class Tema1(QWidget):

    def __init__(self):

        super(QWidget, self).__init__()

        button_color = Parameters.Color().whatcolor()

        self.setFont(QFont('Century Gothic', 10))

        self.windowW1 = Parameters.ParameterSize().ww()
        self.windowH1 = Parameters.ParameterSize().wh()

        self.setWindowTitle('Tema 1')

        self.setFixedSize(self.windowW1*0.2395833333333333, self.windowH1*0.4259259259259259)

        topleft1 = QPushButton("Tema 1.1", self)
        topleft1.setStyleSheet("background-color: {0}".format(button_color))
        topleft1.setGeometry(self.windowW1*0.0104166666666667, self.windowH1*0.0185185185185185, self.windowW1*0.104166666666667, self.windowH1*0.185185185185185)

        topleft1.clicked.connect(self.show_tema1_1)

        topleft2 = QPushButton("Tema 1.2", self)
        topleft2.setStyleSheet("background-color: {0}".format(button_color))
        topleft2.setGeometry(self.windowW1*0.125, self.windowH1*0.0185185185185185, self.windowW1*0.104166666666667, self.windowH1*0.185185185185185)

        topleft2.clicked.connect(self.show_tema1_2)

        topleft3 = QPushButton("Tema 1.3", self)
        topleft3.setStyleSheet("background-color: {0}".format(button_color))
        topleft3.setGeometry(self.windowW1*0.0104166666666667, self.windowH1*0.2222222222222222, self.windowW1*0.104166666666667, self.windowH1*0.185185185185185)

        topleft3.clicked.connect(self.show_tema1_3)

        topleft4 = QPushButton("Tema 1.4", self)
        topleft4.setStyleSheet("background-color: {0}".format(button_color))
        topleft4.setGeometry(self.windowW1*0.125, self.windowH1*0.2222222222222222, self.windowW1*0.104166666666667, self.windowH1*0.185185185185185)

        topleft4.clicked.connect(self.show_tema1_4)

    def show_tema1_1(self):
        self.w11 = Tema1_1()
        self.w11.show()

    def show_tema1_2(self):
        self.w12 = Tema1_2()
        self.w12.show()

    def show_tema1_3(self):
        self.w13 = Tema1_3()
        self.w13.show()

    def show_tema1_4(self):
        self.w14 = Tema1_4()
        self.w14.show()


class Tema1_1(QWidget):

    def __init__(self):

        self.homepath = QtCore.QDir.homePath()

        self.windowW1 = Parameters.ParameterSize().ww()
        self.windowH1 = Parameters.ParameterSize().wh()

        super(QWidget, self).__init__()

        self.setFont(QFont('Century Gothic', 10))

        self.setWindowTitle('Tema 1.1')
        self.setFont(QFont('Century Gothic', 10))
        self.setFixedSize(self.windowW1*0.15625, self.windowH1*0.2777777777777778)

        self.txt = "1.1"

        answer1_1 = QLabel(self.txt, self)

        btn = SendEmailButton.button(self)
        btn.clicked.connect(self.show_send)

        vbox = QVBoxLayout()
        vbox.addWidget(answer1_1, alignment=QtCore.Qt.AlignHCenter)
        vbox.addWidget(btn, alignment=QtCore.Qt.AlignHCenter)

        self.setLayout(vbox)

    def show_send(self):

        self.send_mail = SendEmailWindow()
        self.send_mail.show()

        with open(self.homepath + "/Desktop/проект/ProgrammFiles/Text.txt", "w") as textfile:

            textfile.write(self.txt)

class Tema1_2(QWidget):

    def __init__(self):

        self.homepath = QtCore.QDir.homePath()

        self.windowW1 = Parameters.ParameterSize().ww()
        self.windowH1 = Parameters.ParameterSize().wh()

        super(QWidget, self).__init__()

        self.setFont(QFont('Century Gothic', 10))

        self.setWindowTitle('Tema 1.2')

        self.setFixedSize(self.windowW1*0.15625, self.windowH1*0.2777777777777778)

        self.txt = '1.2'

        answer1_2 = QLabel(self.txt, self)

        btn = SendEmailButton.button(self)
        btn.clicked.connect(self.show_send)

        vbox = QVBoxLayout()
        vbox.addWidget(answer1_2, alignment=QtCore.Qt.AlignHCenter)
        vbox.addWidget(btn, alignment=QtCore.Qt.AlignHCenter)

        self.setLayout(vbox)

    def show_send(self):

        self.send_mail = SendEmailWindow()
        self.send_mail.show()

        with open(self.homepath + "/Desktop/проект/ProgrammFiles/Text.txt", "w") as textfile:

            textfile.write(self.txt)


class Tema1_3(QWidget):

    def __init__(self):

        self.homepath = QtCore.QDir.homePath()

        self.windowW1 = Parameters.ParameterSize().ww()
        self.windowH1 = Parameters.ParameterSize().wh()

        super(QWidget, self).__init__()

        self.setFont(QFont('Century Gothic', 10))

        self.setWindowTitle('Tema 1.3')

        self.setFixedSize(self.windowW1*0.15625, self.windowH1*0.2777777777777778)

        self.txt = "1.3"
        answer1_3 = QLabel(self.txt, self)

        btn = SendEmailButton.button(self)
        btn.clicked.connect(self.show_send)

        vbox = QVBoxLayout()
        vbox.addWidget(answer1_3, alignment=QtCore.Qt.AlignHCenter)
        vbox.addWidget(btn, alignment=QtCore.Qt.AlignHCenter)

        self.setLayout(vbox)

    def show_send(self):

        self.send_mail = SendEmailWindow()
        self.send_mail.show()

        with open(self.homepath + "/Desktop/проект/ProgrammFiles/Text.txt", "w") as textfile:

            textfile.write(self.txt)


class Tema1_4(QWidget):

    def __init__(self):

        self.homepath = QtCore.QDir.homePath()

        self.windowW1 = Parameters.ParameterSize().ww()
        self.windowH1 = Parameters.ParameterSize().wh()

        super(QWidget, self).__init__()

        self.setFont(QFont('Century Gothic', 10))

        self.setWindowTitle('Tema 1.4')

        self.setFixedSize(self.windowW1*0.15625, self.windowH1*0.2777777777777778)

        self.txt = '1.4'
        answer1_4 = QLabel(self.txt, self)

        btn = SendEmailButton.button(self)
        btn.clicked.connect(self.show_send)

        vbox = QVBoxLayout()
        vbox.addWidget(answer1_4, alignment=QtCore.Qt.AlignHCenter)
        vbox.addWidget(btn, alignment=QtCore.Qt.AlignHCenter)

        self.setLayout(vbox)

    def show_send(self):

        self.send_mail = SendEmailWindow()
        self.send_mail.show()

        with open(self.homepath + "/Desktop/проект/ProgrammFiles/Text.txt", "w") as textfile:

            textfile.write(self.txt)


class Tema2(QWidget):

    def __init__(self):

        self.homepath = QtCore.QDir.homePath()

        self.windowW1 = Parameters.ParameterSize().ww()
        self.windowH1 = Parameters.ParameterSize().wh()

        button_color = Parameters.Color().whatcolor()

        super(QWidget, self).__init__()

        self.setFont(QFont('Century Gothic', 10))

        self.setWindowTitle('Tema 2')

        self.setFixedSize(self.windowW1*0.2395833333333333, self.windowH1*0.4259259259259259)

        topcenter1 = QPushButton("Tema 2.1", self)
        topcenter1.setStyleSheet("background-color: {0}".format(button_color))
        topcenter1.setGeometry(self.windowW1*0.0104166666666667, self.windowH1*0.0185185185185185, self.windowW1*0.104166666666667, self.windowH1*0.185185185185185)

        topcenter1.clicked.connect(self.show_tema2_1)

        topcenter2 = QPushButton("Tema 2.2", self)
        topcenter2.setStyleSheet("background-color: {0}".format(button_color))
        topcenter2.setGeometry(self.windowW1*0.125, self.windowH1*0.0185185185185185, self.windowW1*0.104166666666667, self.windowH1*0.185185185185185)

        topcenter2.clicked.connect(self.show_tema2_2)

        topcenter3 = QPushButton("Tema 2.3", self)
        topcenter3.setStyleSheet("background-color: {0}".format(button_color))
        topcenter3.setGeometry(self.windowW1*0.0104166666666667, self.windowH1*0.2222222222222222, self.windowW1*0.104166666666667, self.windowH1*0.185185185185185)

        topcenter3.clicked.connect(self.show_tema2_3)

        topcenter4 = QPushButton("Tema 2.4", self)
        topcenter4.setStyleSheet("background-color: {0}".format(button_color))
        topcenter4.setGeometry(self.windowW1*0.125, self.windowH1*0.2222222222222222, self.windowW1*0.104166666666667, self.windowH1*0.185185185185185)

        topcenter4.clicked.connect(self.show_tema2_4)

    def show_tema2_1(self):
        self.w21 = Tema2_1()
        self.w21.show()

    def show_tema2_2(self):
        self.w22 = Tema2_2()
        self.w22.show()

    def show_tema2_3(self):
        self.w23 = Tema2_3()
        self.w23.show()

    def show_tema2_4(self):
        self.w24 = Tema2_4()
        self.w24.show()


class Tema2_1(QWidget):

    def __init__(self):

        self.windowW1 = Parameters.ParameterSize().ww()
        self.windowH1 = Parameters.ParameterSize().wh()

        super(QWidget, self).__init__()

        self.setFont(QFont('Century Gothic', 10))

        self.setWindowTitle('Tema 2.1')

        self.setFixedSize(self.windowW1*0.15625, self.windowH1*0.2777777777777778)

        self.txt = '2.1'
        answer2_1 = QLabel(self.txt, self)

        btn = SendEmailButton.button(self)
        btn.clicked.connect(self.show_send)

        vbox = QVBoxLayout()
        vbox.addWidget(answer2_1, alignment=QtCore.Qt.AlignHCenter)
        vbox.addWidget(btn, alignment=QtCore.Qt.AlignHCenter)

        self.setLayout(vbox)

    def show_send(self):
        self.send_mail = SendEmailWindow()
        self.send_mail.show()

        with open(self.homepath + "/Desktop/проект/ProgrammFiles/Text.txt", "w") as textfile:
            textfile.write(self.txt)


class Tema2_2(QWidget):

    def __init__(self):

        self.homepath = QtCore.QDir.homePath()

        self.windowW1 = Parameters.ParameterSize().ww()
        self.windowH1 = Parameters.ParameterSize().wh()

        super(QWidget, self).__init__()

        self.setFont(QFont('Century Gothic', 10))

        self.setWindowTitle('Tema 2.2')

        self.setFixedSize(self.windowW1*0.15625, self.windowH1*0.2777777777777778)

        self.txt = '2.2'
        answer2_2 = QLabel(self.txt, self)

        btn = SendEmailButton.button(self)
        btn.clicked.connect(self.show_send)

        vbox = QVBoxLayout()
        vbox.addWidget(answer2_2, alignment=QtCore.Qt.AlignHCenter)
        vbox.addWidget(btn, alignment=QtCore.Qt.AlignHCenter)

        self.setLayout(vbox)

    def show_send(self):
        self.send_mail = SendEmailWindow()
        self.send_mail.show()

        with open(self.homepath + "/Desktop/проект/ProgrammFiles/Text.txt", "w") as textfile:
            textfile.write(self.txt)


class Tema2_3(QWidget):

    def __init__(self):

        self.homepath = QtCore.QDir.homePath()

        self.windowW1 = Parameters.ParameterSize().ww()
        self.windowH1 = Parameters.ParameterSize().wh()

        super(QWidget, self).__init__()

        self.setFont(QFont('Century Gothic', 10))

        self.setWindowTitle('Tema 2.3')

        self.setFixedSize(self.windowW1*0.15625, self.windowH1*0.2777777777777778)

        self.txt = '2.3'
        answer2_3 = QLabel(self.txt, self)

        btn = SendEmailButton.button(self)
        btn.clicked.connect(self.show_send)

        vbox = QVBoxLayout()
        vbox.addWidget(answer2_3, alignment=QtCore.Qt.AlignHCenter)
        vbox.addWidget(btn, alignment=QtCore.Qt.AlignHCenter)

        self.setLayout(vbox)

    def show_send(self):

        self.send_mail = SendEmailWindow()
        self.send_mail.show()

        with open(self.homepath + "/Desktop/проект/ProgrammFiles/Text.txt", "w") as textfile:

            textfile.write(self.txt)


class Tema2_4(QWidget):

    def __init__(self):

        self.homepath = QtCore.QDir.homePath()

        self.windowW1 = Parameters.ParameterSize().ww()
        self.windowH1 = Parameters.ParameterSize().wh()

        super(QWidget, self).__init__()

        self.setFont(QFont('Century Gothic', 10))

        self.setWindowTitle('Tema 2.4')

        self.setFixedSize(self.windowW1*0.15625, self.windowH1*0.2777777777777778)

        self.txt = '2.4'
        answer2_4 = QLabel(self.txt, self)

        btn = SendEmailButton.button(self)
        btn.clicked.connect(self.show_send)

        vbox = QVBoxLayout()
        vbox.addWidget(answer2_4, alignment=QtCore.Qt.AlignHCenter)
        vbox.addWidget(btn, alignment=QtCore.Qt.AlignHCenter)

        self.setLayout(vbox)

    def show_send(self):

        self.send_mail = SendEmailWindow()
        self.send_mail.show()

        with open(self.homepath + "/Desktop/проект/ProgrammFiles/Text.txt", "w") as textfile:

            textfile.write(self.txt)


class Tema3(QWidget):

    def __init__(self):

        button_color = Parameters.Color().whatcolor()

        self.windowW1 = Parameters.ParameterSize().ww()
        self.windowH1 = Parameters.ParameterSize().wh()

        super(QWidget, self).__init__()

        self.setFont(QFont('Century Gothic', 10))

        self.setWindowTitle('Tema 3')

        self.setFixedSize(self.windowW1*0.2395833333333333, self.windowH1*0.4259259259259259)

        topright1 = QPushButton("Tema 3.1", self)
        topright1.setStyleSheet("background-color: {0}".format(button_color))
        topright1.setGeometry(self.windowW1*0.0104166666666667, self.windowH1*0.0185185185185185, self.windowW1*0.104166666666667, self.windowH1*0.185185185185185)

        topright1.clicked.connect(self.show_tema3_1)

        topright2 = QPushButton("Tema 3.2", self)
        topright2.setStyleSheet("background-color: {0}".format(button_color))
        topright2.setGeometry(self.windowW1*0.125, self.windowH1*0.0185185185185185, self.windowW1*0.104166666666667, self.windowH1*0.185185185185185)

        topright2.clicked.connect(self.show_tema3_2)

        topright3 = QPushButton("Tema 3.3", self)
        topright3.setStyleSheet("background-color: {0}".format(button_color))
        topright3.setGeometry(self.windowW1*0.0104166666666667, self.windowH1*0.2222222222222222, self.windowW1*0.104166666666667, self.windowH1*0.185185185185185)

        topright3.clicked.connect(self.show_tema3_3)

        topright4 = QPushButton("Tema 3.4", self)
        topright4.setStyleSheet("background-color: {0}".format(button_color))
        topright4.setGeometry(self.windowW1*0.125, self.windowH1*0.2222222222222222, self.windowW1*0.104166666666667, self.windowH1*0.185185185185185)

        topright4.clicked.connect(self.show_tema3_4)

    def show_tema3_1(self):
        self.w31 = Tema3_1()
        self.w31.show()

    def show_tema3_2(self):
        self.w32 = Tema3_2()
        self.w32.show()

    def show_tema3_3(self):
        self.w33 = Tema3_3()
        self.w33.show()

    def show_tema3_4(self):
        self.w34 = Tema3_4()
        self.w34.show()


class Tema3_1(QWidget):

    def __init__(self):

        self.homepath = QtCore.QDir.homePath()

        self.windowW1 = Parameters.ParameterSize().ww()
        self.windowH1 = Parameters.ParameterSize().wh()

        super(QWidget, self).__init__()

        self.setFont(QFont('Century Gothic', 10))

        self.setWindowTitle('Tema 3.1')

        self.setFixedSize(self.windowW1*0.15625, self.windowH1*0.2777777777777778)

        self.txt = '3.1'
        answer3_1 = QLabel(self.txt, self)

        btn = SendEmailButton.button(self)
        btn.clicked.connect(self.show_send)

        vbox = QVBoxLayout()
        vbox.addWidget(answer3_1, alignment=QtCore.Qt.AlignHCenter)
        vbox.addWidget(btn, alignment=QtCore.Qt.AlignHCenter)

        self.setLayout(vbox)

    def show_send(self):

        self.send_mail = SendEmailWindow()
        self.send_mail.show()

        with open(self.homepath + "/Desktop/проект/ProgrammFiles/Text.txt", "w") as textfile:

            textfile.write(self.txt)


class Tema3_2(QWidget):

    def __init__(self):

        self.homepath = QtCore.QDir.homePath()

        self.windowW1 = Parameters.ParameterSize().ww()
        self.windowH1 = Parameters.ParameterSize().wh()

        super(QWidget, self).__init__()

        self.setFont(QFont('Century Gothic', 10))

        self.setWindowTitle('Tema 3.2')

        self.setFixedSize(self.windowW1*0.15625, self.windowH1*0.2777777777777778)

        self.txt = '3.2'
        answer3_2 = QLabel(self.txt, self)

        btn = SendEmailButton.button(self)
        btn.clicked.connect(self.show_send)

        vbox = QVBoxLayout()
        vbox.addWidget(answer3_2, alignment=QtCore.Qt.AlignHCenter)
        vbox.addWidget(btn, alignment=QtCore.Qt.AlignHCenter)

        self.setLayout(vbox)

    def show_send(self):

        self.send_mail = SendEmailWindow()
        self.send_mail.show()

        with open(self.homepath + "/Desktop/проект/ProgrammFiles/Text.txt", "w") as textfile:

            textfile.write(self.txt)


class Tema3_3(QWidget):

    def __init__(self):

        self.homepath = QtCore.QDir.homePath()

        self.windowW1 = Parameters.ParameterSize().ww()
        self.windowH1 = Parameters.ParameterSize().wh()

        super(QWidget, self).__init__()

        self.setFont(QFont('Century Gothic', 10))

        self.setWindowTitle('Tema 3.3')

        self.setFixedSize(self.windowW1*0.15625, self.windowH1*0.2777777777777778)

        self.txt = '3.3'
        answer3_3 = QLabel(self.txt, self)

        vbox = QVBoxLayout()
        vbox.addWidget(answer3_3, alignment=QtCore.Qt.AlignHCenter)
        vbox.addWidget(SendEmailButton.button(self), alignment=QtCore.Qt.AlignHCenter)

        self.setLayout(vbox)

    def show_send(self):

        self.send_mail = SendEmailWindow()
        self.send_mail.show()

        with open(self.homepath + "/Desktop/проект/ProgrammFiles/Text.txt", "w") as textfile:

            textfile.write(self.txt)


class Tema3_4(QWidget):

    def __init__(self):

        self.homepath = QtCore.QDir.homePath()

        self.windowW1 = Parameters.ParameterSize().ww()
        self.windowH1 = Parameters.ParameterSize().wh()

        super(QWidget, self).__init__()

        self.setFont(QFont('Century Gothic', 10))

        self.setWindowTitle('Tema 3.4')

        self.setFixedSize(self.windowW1*0.15625, self.windowH1*0.2777777777777778)

        self.txt = '3.4'
        answer3_4 = QLabel(self.txt, self)

        btn = SendEmailButton.button(self)
        btn.clicked.connect(self.show_send)

        vbox = QVBoxLayout()
        vbox.addWidget(answer3_4, alignment=QtCore.Qt.AlignHCenter)
        vbox.addWidget(btn, alignment=QtCore.Qt.AlignHCenter)

        self.setLayout(vbox)

    def show_send(self):

        self.send_mail = SendEmailWindow()
        self.send_mail.show()

        with open(self.homepath + "/Desktop/проект/ProgrammFiles/Text.txt", "w") as textfile:

            textfile.write(self.txt)


class Tema4(QWidget):

    def __init__(self):

        button_color = Parameters.Color().whatcolor()

        self.windowW1 = Parameters.ParameterSize().ww()
        self.windowH1 = Parameters.ParameterSize().wh()

        super(QWidget, self).__init__()

        self.setFont(QFont('Century Gothic', 10))

        self.setWindowTitle('Tema 4')

        self.setFixedSize(self.windowW1*0.2395833333333333, self.windowH1*0.4259259259259259)

        bottomleft1 = QPushButton("Tema 4.1", self)
        bottomleft1.setStyleSheet("background-color: {0}".format(button_color))
        bottomleft1.setGeometry(self.windowW1*0.0104166666666667, self.windowH1*0.0185185185185185, self.windowW1*0.104166666666667, self.windowH1*0.185185185185185)

        bottomleft1.clicked.connect(self.show_tema4_1)

        bottomleft2 = QPushButton("Tema 4.2", self)
        bottomleft2.setStyleSheet("background-color: {0}".format(button_color))
        bottomleft2.setGeometry(self.windowW1*0.125, self.windowH1*0.0185185185185185, self.windowW1*0.104166666666667, self.windowH1*0.185185185185185)

        bottomleft2.clicked.connect(self.show_tema4_2)

        bottomleft3 = QPushButton("Tema 4.3", self)
        bottomleft3.setStyleSheet("background-color: {0}".format(button_color))
        bottomleft3.setGeometry(self.windowW1*0.0104166666666667, self.windowH1*0.2222222222222222, self.windowW1*0.104166666666667, self.windowH1*0.185185185185185)

        bottomleft3.clicked.connect(self.show_tema4_3)

        bottomleft4 = QPushButton("Tema 4.4", self)
        bottomleft4.setStyleSheet("background-color: {0}".format(button_color))
        bottomleft4.setGeometry(self.windowW1*0.125, self.windowH1*0.2222222222222222, self.windowW1*0.104166666666667, self.windowH1*0.185185185185185)

        bottomleft4.clicked.connect(self.show_tema4_4)

    def show_tema4_1(self):
        self.w41 = Tema4_1()
        self.w41.show()

    def show_tema4_2(self):
        self.w42 = Tema4_2()
        self.w42.show()

    def show_tema4_3(self):
        self.w43 = Tema4_3()
        self.w43.show()

    def show_tema4_4(self):
        self.w44 = Tema4_4()
        self.w44.show()


class Tema4_1(QWidget):

    def __init__(self):

        self.homepath = QtCore.QDir.homePath()

        self.windowW1 = Parameters.ParameterSize().ww()
        self.windowH1 = Parameters.ParameterSize().wh()

        super(QWidget, self).__init__()

        self.setFont(QFont('Century Gothic', 10))

        self.setWindowTitle('Tema 4.1')

        self.setFixedSize(self.windowW1*0.15625, self.windowH1*0.2777777777777778)

        self.txt = '4.1'
        answer4_1 = QLabel(self.txt, self)

        btn = SendEmailButton.button(self)
        btn.clicked.connect(self.show_send)

        vbox = QVBoxLayout()
        vbox.addWidget(answer4_1, alignment=QtCore.Qt.AlignHCenter)
        vbox.addWidget(btn, alignment=QtCore.Qt.AlignHCenter)

        self.setLayout(vbox)

    def show_send(self):

        self.send_mail = SendEmailWindow()
        self.send_mail.show()

        with open(self.homepath + "/Desktop/проект/ProgrammFiles/Text.txt", "w") as textfile:

            textfile.write(self.txt)


class Tema4_2(QWidget):

    def __init__(self):

        self.homepath = QtCore.QDir.homePath()

        self.windowW1 = Parameters.ParameterSize().ww()
        self.windowH1 = Parameters.ParameterSize().wh()

        super(QWidget, self).__init__()

        self.setFont(QFont('Century Gothic', 10))

        self.setWindowTitle('Tema 4.2')

        self.setFixedSize(self.windowW1*0.15625, self.windowH1*0.2777777777777778)

        self.txt = '4.2'
        answer4_2 = QLabel(self.txt, self)

        btn = SendEmailButton.button(self)
        btn.clicked.connect(self.show_send)

        vbox = QVBoxLayout()
        vbox.addWidget(answer4_2, alignment=QtCore.Qt.AlignHCenter)
        vbox.addWidget(btn, alignment=QtCore.Qt.AlignHCenter)

        self.setLayout(vbox)

    def show_send(self):

        self.send_mail = SendEmailWindow()
        self.send_mail.show()

        with open(self.homepath + "/Desktop/проект/ProgrammFiles/Text.txt", "w") as textfile:

            textfile.write(self.txt)


class Tema4_3(QWidget):

    def __init__(self):

        self.homepath = QtCore.QDir.homePath()

        self.windowW1 = Parameters.ParameterSize().ww()
        self.windowH1 = Parameters.ParameterSize().wh()

        super(QWidget, self).__init__()

        self.setFont(QFont('Century Gothic', 10))

        self.setWindowTitle('Tema 4.3')

        self.setFixedSize(self.windowW1*0.15625, self.windowH1*0.2777777777777778)

        self.txt = '4.3'
        answer4_3 = QLabel(self.txt, self)

        btn = SendEmailButton.button(self)
        btn.clicked.connect(self.show_send)

        vbox = QVBoxLayout()
        vbox.addWidget(answer4_3, alignment=QtCore.Qt.AlignHCenter)
        vbox.addWidget(btn, alignment=QtCore.Qt.AlignHCenter)

        self.setLayout(vbox)

    def show_send(self):

        self.send_mail = SendEmailWindow()
        self.send_mail.show()

        with open(self.homepath + "/Desktop/проект/ProgrammFiles/Text.txt", "w") as textfile:

            textfile.write(self.txt)


class Tema4_4(QWidget):

    def __init__(self):

        self.homepath = QtCore.QDir.homePath()

        self.windowW1 = Parameters.ParameterSize().ww()
        self.windowH1 = Parameters.ParameterSize().wh()

        super(QWidget, self).__init__()

        self.setFont(QFont('Century Gothic', 10))

        self.setWindowTitle('Tema 4.4')

        self.setFixedSize(self.windowW1*0.15625, self.windowH1*0.2777777777777778)

        self.txt = '4.4'
        answer4_4 = QLabel(self.txt, self)

        btn = SendEmailButton.button(self)
        btn.clicked.connect(self.show_send)

        vbox = QVBoxLayout()
        vbox.addWidget(answer4_4, alignment=QtCore.Qt.AlignHCenter)
        vbox.addWidget(btn, alignment=QtCore.Qt.AlignHCenter)

        self.setLayout(vbox)

    def show_send(self):

        self.send_mail = SendEmailWindow()
        self.send_mail.show()

        with open(self.homepath + "/Desktop/проект/ProgrammFiles/Text.txt", "w") as textfile:

            textfile.write(self.txt)


class Tema5(QWidget):

    def __init__(self):

        button_color = Parameters.Color().whatcolor()
        self.windowW1 = Parameters.ParameterSize().ww()
        self.windowH1 = Parameters.ParameterSize().wh()

        super(QWidget, self).__init__()

        self.setFont(QFont('Century Gothic', 10))

        self.setWindowTitle('Tema 5')

        self.setFixedSize(self.windowW1*0.2395833333333333, self.windowH1*0.4259259259259259)

        bottomcenter1 = QPushButton("Tema 5.1", self)
        bottomcenter1.setStyleSheet("background-color: {0}".format(button_color))
        bottomcenter1.setGeometry(self.windowW1*0.0104166666666667, self.windowH1*0.0185185185185185, self.windowW1*0.104166666666667, self.windowH1*0.185185185185185)

        bottomcenter1.clicked.connect(self.show_tema5_1)

        bottomcenter2 = QPushButton("Tema 5.2", self)
        bottomcenter2.setStyleSheet("background-color: {0}".format(button_color))
        bottomcenter2.setGeometry(self.windowW1*0.125, self.windowH1*0.0185185185185185, self.windowW1*0.104166666666667, self.windowH1*0.185185185185185)

        bottomcenter2.clicked.connect(self.show_tema5_2)

        bottomcenter3 = QPushButton("Tema 5.3", self)
        bottomcenter3.setStyleSheet("background-color: {0}".format(button_color))
        bottomcenter3.setGeometry(self.windowW1*0.0104166666666667, self.windowH1*0.2222222222222222, self.windowW1*0.104166666666667, self.windowH1*0.185185185185185)

        bottomcenter3.clicked.connect(self.show_tema5_3)

        bottomcenter4 = QPushButton("Tema 5.4", self)
        bottomcenter4.setStyleSheet("background-color: {0}".format(button_color))
        bottomcenter4.setGeometry(self.windowW1*0.125, self.windowH1*0.2222222222222222, self.windowW1*0.104166666666667, self.windowH1*0.185185185185185)

        bottomcenter4.clicked.connect(self.show_tema5_4)

    def show_tema5_1(self):
        self.w51 = Tema5_1()
        self.w51.show()

    def show_tema5_2(self):
        self.w52 = Tema5_2()
        self.w52.show()

    def show_tema5_3(self):
        self.w53 = Tema5_3()
        self.w53.show()

    def show_tema5_4(self):
        self.w54 = Tema5_4()
        self.w54.show()


class Tema5_1(QWidget):

    def __init__(self):

        self.homepath = QtCore.QDir.homePath()

        self.windowW1 = Parameters.ParameterSize().ww()
        self.windowH1 = Parameters.ParameterSize().wh()
        super(QWidget, self).__init__()

        self.setFont(QFont('Century Gothic', 10))

        self.setWindowTitle('Tema 5.1')

        self.setFixedSize(self.windowW1*0.15625, self.windowH1*0.2777777777777778)

        self.txt = '5.1'
        answer5_1 = QLabel(self.txt, self)

        btn = SendEmailButton.button(self)
        btn.clicked.connect(self.show_send)

        vbox = QVBoxLayout()
        vbox.addWidget(answer5_1, alignment=QtCore.Qt.AlignHCenter)
        vbox.addWidget(btn, alignment=QtCore.Qt.AlignHCenter)

        self.setLayout(vbox)

    def show_send(self):

        self.send_mail = SendEmailWindow()
        self.send_mail.show()

        with open(self.homepath + "/Desktop/проект/ProgrammFiles/Text.txt", "w") as textfile:

            textfile.write(self.txt)


class Tema5_2(QWidget):

    def __init__(self):

        self.homepath = QtCore.QDir.homePath()

        self.windowW1 = Parameters.ParameterSize().ww()
        self.windowH1 = Parameters.ParameterSize().wh()

        super(QWidget, self).__init__()

        self.setFont(QFont('Century Gothic', 10))

        self.setWindowTitle('Tema 5.2')

        self.setFixedSize(self.windowW1*0.15625, self.windowH1*0.2777777777777778)

        self.txt = '5.2'
        answer5_2 = QLabel(self.txt, self)

        btn = SendEmailButton.button(self)
        btn.clicked.connect(self.show_send)

        vbox = QVBoxLayout()
        vbox.addWidget(answer5_2, alignment=QtCore.Qt.AlignHCenter)
        vbox.addWidget(btn, alignment=QtCore.Qt.AlignHCenter)

        self.setLayout(vbox)

    def show_send(self):

        self.send_mail = SendEmailWindow()
        self.send_mail.show()

        with open(self.homepath + "/Desktop/проект/ProgrammFiles/Text.txt", "w") as textfile:

            textfile.write(self.txt)


class Tema5_3(QWidget):

    def __init__(self):

        self.homepath = QtCore.QDir.homePath()

        self.windowW1 = Parameters.ParameterSize().ww()
        self.windowH1 = Parameters.ParameterSize().wh()

        super(QWidget, self).__init__()

        self.setFont(QFont('Century Gothic', 10))

        self.setWindowTitle('Tema 5.3')

        self.setFixedSize(self.windowW1*0.15625, self.windowH1*0.2777777777777778)

        self.txt = '5.3'
        answer5_3 = QLabel(self.txt, self)

        btn = SendEmailButton.button(self)
        btn.clicked.connect(self.show_send)

        vbox = QVBoxLayout()
        vbox.addWidget(answer5_3, alignment=QtCore.Qt.AlignHCenter)
        vbox.addWidget(btn, alignment=QtCore.Qt.AlignHCenter)

        self.setLayout(vbox)

    def show_send(self):

        self.send_mail = SendEmailWindow()
        self.send_mail.show()

        with open(self.homepath + "/Desktop/проект/ProgrammFiles/Text.txt", "w") as textfile:

            textfile.write(self.txt)


class Tema5_4(QWidget):

    def __init__(self):

        self.homepath = QtCore.QDir.homePath()

        self.windowW1 = Parameters.ParameterSize().ww()
        self.windowH1 = Parameters.ParameterSize().wh()

        super(QWidget, self).__init__()

        self.setFont(QFont('Century Gothic', 10))

        self.setWindowTitle('Tema 5.4')

        self.setFixedSize(self.windowW1*0.15625, self.windowH1*0.2777777777777778)

        self.txt = '5.4'
        answer5_4 = QLabel(self.txt, self)

        btn = SendEmailButton.button(self)
        btn.clicked.connect(self.show_send)

        vbox = QVBoxLayout()
        vbox.addWidget(answer5_4, alignment=QtCore.Qt.AlignHCenter)
        vbox.addWidget(btn, alignment=QtCore.Qt.AlignHCenter)

        self.setLayout(vbox)

    def show_send(self):

        self.send_mail = SendEmailWindow()
        self.send_mail.show()

        with open(self.homepath + "/Desktop/проект/ProgrammFiles/Text.txt", "w") as textfile:

            textfile.write(self.txt)


class Tema6(QWidget):

    def __init__(self):

        self.homepath = QtCore.QDir.homePath()

        button_color = Parameters.Color().whatcolor()

        self.windowW1 = Parameters.ParameterSize().ww()
        self.windowH1 = Parameters.ParameterSize().wh()

        super(QWidget, self).__init__()

        self.setFont(QFont('Century Gothic', 10))

        self.setWindowTitle('Tema 6')

        self.setFixedSize(self.windowW1*0.2395833333333333, self.windowH1*0.4259259259259259)

        bottomright1 = QPushButton("Tema 6.1", self)
        bottomright1.setStyleSheet("background-color: {0}".format(button_color))
        bottomright1.setGeometry(self.windowW1*0.0104166666666667, self.windowH1*0.0185185185185185, self.windowW1*0.104166666666667, self.windowH1*0.185185185185185)

        bottomright1.clicked.connect(self.show_tema6_1)

        bottomright2 = QPushButton("Tema 6.2", self)
        bottomright2.setStyleSheet("background-color: {0}".format(button_color))
        bottomright2.setGeometry(self.windowW1*0.125, self.windowH1*0.0185185185185185, self.windowW1*0.104166666666667, self.windowH1*0.185185185185185)

        bottomright2.clicked.connect(self.show_tema6_2)

        bottomright3 = QPushButton("Tema 6.3", self)
        bottomright3.setStyleSheet("background-color: {0}".format(button_color))
        bottomright3.setGeometry(self.windowW1*0.0104166666666667, self.windowH1*0.2222222222222222, self.windowW1*0.104166666666667, self.windowH1*0.185185185185185)

        bottomright3.clicked.connect(self.show_tema6_3)

        bottomright4 = QPushButton("Tema 6.4", self)
        bottomright4.setStyleSheet("background-color: {0}".format(button_color))
        bottomright4.setGeometry(self.windowW1*0.125, self.windowH1*0.2222222222222222, self.windowW1*0.104166666666667, self.windowH1*0.185185185185185)

        bottomright4.clicked.connect(self.show_tema6_4)

    def show_tema6_1(self):
        self.w61 = Tema6_1()
        self.w61.show()

    def show_tema6_2(self):
        self.w62 = Tema6_2()
        self.w62.show()

    def show_tema6_3(self):
        self.w63 = Tema6_3()
        self.w63.show()

    def show_tema6_4(self):
        self.w64 = Tema6_4()
        self.w64.show()


class Tema6_1(QWidget):

    def __init__(self):

        self.windowW1 = Parameters.ParameterSize().ww()
        self.windowH1 = Parameters.ParameterSize().wh()

        super(QWidget, self).__init__()

        self.setFont(QFont('Century Gothic', 10))

        self.setWindowTitle('Tema 6.1')

        self.setFixedSize(self.windowW1*0.15625, self.windowH1*0.2777777777777778)

        self.txt = '6.1'
        answer6_1 = QLabel(self.txt, self)

        btn = SendEmailButton.button(self)
        btn.clicked.connect(self.show_send)

        vbox = QVBoxLayout()
        vbox.addWidget(answer6_1, alignment=QtCore.Qt.AlignHCenter)
        vbox.addWidget(btn, alignment=QtCore.Qt.AlignHCenter)

        self.setLayout(vbox)

    def show_send(self):

        self.send_mail = SendEmailWindow()
        self.send_mail.show()

        with open(self.homepath + "/Desktop/проект/ProgrammFiles/Text.txt", "w") as textfile:

            textfile.write(self.txt)


class Tema6_2(QWidget):

    def __init__(self):

        self.windowW1 = Parameters.ParameterSize().ww()
        self.windowH1 = Parameters.ParameterSize().wh()

        super(QWidget, self).__init__()

        self.setFont(QFont('Century Gothic', 10))

        self.setWindowTitle('Tema 6.2')

        self.setFixedSize(self.windowW1*0.15625, self.windowH1*0.2777777777777778)

        self.txt = '6.2'
        answer6_2 = QLabel(self.txt, self)

        btn = SendEmailButton.button(self)
        btn.clicked.connect(self.show_send)

        vbox = QVBoxLayout()
        vbox.addWidget(answer6_2, alignment=QtCore.Qt.AlignHCenter)
        vbox.addWidget(btn, alignment=QtCore.Qt.AlignHCenter)

        self.setLayout(vbox)

    def show_send(self):

        self.send_mail = SendEmailWindow()
        self.send_mail.show()

        with open(self.homepath + "/Desktop/проект/ProgrammFiles/Text.txt", "w") as textfile:

            textfile.write(self.txt)


class Tema6_3(QWidget):

    def __init__(self):

        self.windowW1 = Parameters.ParameterSize().ww()
        self.windowH1 = Parameters.ParameterSize().wh()

        super(QWidget, self).__init__()

        self.setFont(QFont('Century Gothic', 10))

        self.setWindowTitle('Tema 6.3')

        self.setFixedSize(self.windowW1*0.15625, self.windowH1*0.2777777777777778)

        self.txt = '6.3'
        answer6_3 = QLabel(self.txt, self)

        btn = SendEmailButton.button(self)
        btn.clicked.connect(self.show_send)

        vbox = QVBoxLayout()
        vbox.addWidget(answer6_3, alignment=QtCore.Qt.AlignHCenter)
        vbox.addWidget(btn, alignment=QtCore.Qt.AlignHCenter)

        self.setLayout(vbox)

    def show_send(self):

        self.send_mail = SendEmailWindow()
        self.send_mail.show()

        with open(self.homepath + "/Desktop/проект/ProgrammFiles/Text.txt", "w") as textfile:

            textfile.write(self.txt)


class Tema6_4(QWidget):

    def __init__(self):

        self.windowW1 = Parameters.ParameterSize().ww()
        self.windowH1 = Parameters.ParameterSize().wh()

        super(QWidget, self).__init__()
        self.setFont(QFont('Century Gothic', 10))
        self.setWindowTitle('Tema 6.4')

        self.setFixedSize(self.windowW1*0.15625, self.windowH1*0.2777777777777778)

        self.txt = '6.4'
        answer6_4 = QLabel(self.txt, self)

        btn = SendEmailButton.button(self)
        btn.clicked.connect(self.show_send)

        vbox = QVBoxLayout()
        vbox.addWidget(answer6_4, alignment=QtCore.Qt.AlignHCenter)
        vbox.addWidget(btn, alignment=QtCore.Qt.AlignHCenter)

        self.setLayout(vbox)

    def show_send(self):

        self.send_mail = SendEmailWindow()
        self.send_mail.show()

        with open(self.homepath + "/Desktop/проект/ProgrammFiles/Text.txt", "w") as textfile:

            textfile.write(self.txt)