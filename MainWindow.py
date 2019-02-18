#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import Parameters as Parameters
import Settings as Settings
import Information as Information
import ProgramBody as ProgramBody


class MainWindow(QMainWindow):

    def __init__(self, parent=None):

        super(MainWindow, self).__init__(parent)
        self.setFont(QFont('Century Gothic', 10))
        self.setWindowTitle("Книга бизнес-процессов")

        self.windowW = Parameters.ParameterSize().ww()
        self.windowH = Parameters.ParameterSize().wh()

        self.setFixedSize(self.windowW * 0.63, self.windowH * 0.769)

        self.homepath = QDir.homePath()

        self.initUI()

    def initUI(self):

        self.button_color = Parameters.Color().whatcolor()

        self.statusBar().showMessage('Готово к работе')

        # MenuBar

        menubar = self.menuBar()

        settingAction = QAction(QIcon(self.homepath+'/Desktop/проект/ProgrammFiles/setting.png'), '&Настройки', self)
        settingAction.setStatusTip('Открыть настройки')
        settingAction.triggered.connect(self.show_setting)
        settingAction.setShortcut('Ctrl+N')

        infoAction = QAction(QIcon(self.homepath+'/Desktop/проект/ProgrammFiles/info.png'), '&Информация', self)
        infoAction.setStatusTip('Информация о программе')
        infoAction.triggered.connect(self.show_info)
        infoAction.setShortcut('Ctrl+I')

        exitAction = QAction(QIcon(self.homepath+'/Desktop/проект/ProgrammFiles/quit.png'), '&Выход', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Выход из программы')
        exitAction.triggered.connect(qApp.quit)

        programMenu = menubar.addMenu('&Программа')
        programMenu.addAction(settingAction)
        programMenu.addAction(infoAction)
        programMenu.addAction(exitAction)

        # Search

        self.line = QLineEdit(self)
        self.line.move(self.windowW * 0.46785, self.windowH * 0.04)
        self.line.resize(self.windowW * 0.10416666667, self.windowH * 0.0259259259)

        srcbut = QPushButton(self)
        srcbut.setGeometry(self.windowW * 0.5755208333333333, self.windowH * 0.0349, self.windowW * 0.0182291666666667,
                           self.windowH * 0.033)
        srcbut.setIcon(QIcon(self.homepath+"/Desktop/проект/ProgrammFiles/search.png"))
        srcbut.setIconSize(QSize(self.windowW * 0.0182291666666667,
                           self.windowH * 0.033))
        srcbut.setStatusTip('Начать поиск')

        # Main Button

        topleft = QPushButton("Tema 1", self)
        topleft.setStyleSheet("background-color: {0}".format(self.button_color))
        topleft.setGeometry(self.windowW * 0.015625, self.windowH * 0.0925925925925926, self.windowW * 0.1927083333333333,
                            self.windowH * 0.3055555555555556)
        topleft.setToolTip('Здесь будет что-то интересное, но всему свое время...')
        topleft.setStatusTip("Возможность перейти в раздел Темы 1")
        topleft.clicked.connect(self.show_tema1)

        topcenter = QPushButton("Tema 2", self)
        topcenter.setStyleSheet("background-color: {0}".format(self.button_color))
        topcenter.setGeometry(self.windowW * 0.2161458333333333, self.windowH * 0.0925925925925926,
                              self.windowW * 0.1927083333333333,
                              self.windowH * 0.3055555555555556)
        topcenter.setToolTip('Здесь тоже ничего нет, но спасибо, что потратил время на проверку.')
        topcenter.setStatusTip("Возможность перейти в раздел Темы 2")
        topcenter.clicked.connect(self.show_tema2)

        topright = QPushButton("Tema 3", self)
        topright.setStyleSheet("background-color: {0}".format(self.button_color))
        topright.setToolTip('А ты настойчивый, как я погляжу.')
        topright.setGeometry(self.windowW * 0.4166666666666667, self.windowH * 0.0925925925925926,
                             self.windowW * 0.1927083333333333,
                             self.windowH * 0.3055555555555556)
        topright.setStatusTip("Возможность перейти в раздел Темы 3")
        topright.clicked.connect(self.show_tema3)

        bottomleft = QPushButton("Tema 4", self)
        bottomleft.setToolTip('Программное поле плоское или это лишь зрительная иллюзия?')
        bottomleft.setStyleSheet("background-color: {0}".format(self.button_color))
        bottomleft.setGeometry(self.windowW * 0.015625, self.windowH * 0.4166666666666667, self.windowW * 0.1927083333333333,
                               self.windowH * 0.3055555555555556)
        bottomleft.setStatusTip("Возможность перейти в раздел Темы 4")
        bottomleft.clicked.connect(self.show_tema4)

        bottomcenter = QPushButton("Tema 5", self)
        bottomcenter.setStyleSheet("background-color: {0}".format(self.button_color))
        bottomcenter.setGeometry(self.windowW * 0.2161458333333333, self.windowH * 0.4166666666666667,
                                 self.windowW* 0.1927083333333333, self.windowH * 0.3055555555555556)
        bottomcenter.setToolTip('Я устал и хочу спать. Давай закругляйся.')
        bottomcenter.setStatusTip("Возможность перейти в раздел Темы 5")
        bottomcenter.clicked.connect(self.show_tema5)

        bottomright = QPushButton("Tema 6", self)
        bottomright.setStyleSheet("background-color: {0}".format(self.button_color))
        bottomright.setGeometry(self.windowW * 0.4166666666666667, self.windowH * 0.4166666666666667,
                                self.windowW * 0.1927083333333333,
                                self.windowH * 0.3055555555555556)
        bottomright.setToolTip('Кто и зачем я? Окно, которое создано для пустоты. У Создателя точно не все дома.')
        bottomright.setStatusTip("Возможность перейти в раздел Темы 6")
        bottomright.clicked.connect(self.show_tema6)

    def show_info(self):

            self.info = Information.Info()
            self.info.show()

    def show_setting(self):

            self.setting = Settings.Setting()
            self.setting.show()

    def show_tema1(self):

        self.w1 = ProgramBody.Tema1()
        self.w1.show()

    def show_tema2(self):

        self.w2 = ProgramBody.Tema2()
        self.w2.show()

    def show_tema3(self):

        self.w3 = ProgramBody.Tema3()
        self.w3.show()

    def show_tema4(self):

        self.w4 = ProgramBody.Tema4()
        self.w4.show()

    def show_tema5(self):

        self.w5 = ProgramBody.Tema5()
        self.w5.show()

    def show_tema6(self):

        self.w6 = ProgramBody.Tema6()
        self.w6.show()




if __name__ == '__main__':

        app = QApplication(sys.argv)
        ex = MainWindow()
        ex.show()
        sys.exit(app.exec_())