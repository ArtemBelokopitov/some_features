#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtCore import *
import smtplib


def send_letter():

    homepath = QDir.homePath()

    with open(homepath + "/Desktop/проект/ProgrammFiles/Mail.txt", "r") as mailfile:
        uremail = mailfile.readline()
        urpassword = mailfile.readline()
        address = mailfile.readline()

    with open(homepath + "/Desktop/проект/ProgrammFiles/Text.txt", "r") as textfile:
        text = textfile.readline()

    mail_lib = smtplib.SMTP_SSL('smtp.mail.ru', 465)
    mail_lib.ehlo()

    mail_lib.login(uremail, urpassword)
    mail_lib.sendmail(uremail, address, text)

    mail_lib.quit()