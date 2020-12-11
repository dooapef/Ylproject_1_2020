import os
import sys
import struct
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import QtCore, QtGui, QtWidgets
import resources
from bibliares import pyaudio
import sqlite3
import wave


class GUI(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(385, 546)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(0, 0, 386, 548))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(20, 30, 361, 191))
        font = QtGui.QFont()
        font.setPointSize(65)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 370, 161, 81))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_11 = QtWidgets.QPushButton(self.widget)
        self.pushButton_11.setGeometry(QtCore.QRect(110, 190, 161, 81))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_14 = QtWidgets.QPushButton(self.widget)
        self.pushButton_14.setGeometry(QtCore.QRect(110, 280, 161, 81))
        self.pushButton_14.setObjectName("pushButton_14")
        self.widget_2 = QtWidgets.QWidget(Form)
        self.widget_2.setGeometry(QtCore.QRect(0, 0, 386, 548))
        self.widget_2.setObjectName("widget_2")
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setGeometry(QtCore.QRect(70, 10, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(self.widget_2)
        self.label_5.setGeometry(QtCore.QRect(10, 270, 331, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.widget_2)
        self.label_6.setGeometry(QtCore.QRect(0, 300, 301, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.widget_2)
        self.label_7.setGeometry(QtCore.QRect(10, 450, 371, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.widget_2)
        self.label_8.setGeometry(QtCore.QRect(10, 470, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.pushButton_12 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_12.setGeometry(QtCore.QRect(10, 10, 51, 51))
        self.pushButton_12.setStyleSheet("background-image: url(:/icons/icon/backup.png);")
        self.pushButton_12.setText("")
        self.pushButton_12.setObjectName("pushButton_12")
        self.label_12 = QtWidgets.QLabel(self.widget_2)
        self.label_12.setGeometry(QtCore.QRect(0, 320, 351, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.widget_2)
        self.label_13.setGeometry(QtCore.QRect(10, 500, 301, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        self.label_3.setGeometry(QtCore.QRect(0, 110, 371, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget_2)
        self.label_4.setGeometry(QtCore.QRect(0, 140, 351, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.widget_3 = QtWidgets.QWidget(Form)
        self.widget_3.setGeometry(QtCore.QRect(0, 0, 386, 151))
        self.widget_3.setObjectName("widget_3")
        self.label_9 = QtWidgets.QLabel(self.widget_3)
        self.label_9.setGeometry(QtCore.QRect(50, 30, 291, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.widget_3)
        self.label_10.setGeometry(QtCore.QRect(140, 60, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.pushButton_3 = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_3.setGeometry(QtCore.QRect(150, 80, 75, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_11 = QtWidgets.QLabel(self.widget_3)
        self.label_11.setGeometry(QtCore.QRect(90, 120, 271, 20))
        self.label_11.setObjectName("label_11")
        self.widget_5 = QtWidgets.QWidget(Form)
        self.widget_5.setGeometry(QtCore.QRect(0, 0, 386, 548))
        self.widget_5.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.widget_5.setObjectName("widget_5")
        self.label_17 = QtWidgets.QLabel(self.widget_5)
        self.label_17.setGeometry(QtCore.QRect(40, 10, 341, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.widget_5)
        self.label_18.setGeometry(QtCore.QRect(20, 180, 341, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.widget_5)
        self.label_19.setGeometry(QtCore.QRect(170, 250, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.pushButton_5 = QtWidgets.QPushButton(self.widget_5)
        self.pushButton_5.setGeometry(QtCore.QRect(140, 320, 101, 61))
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_20 = QtWidgets.QLabel(self.widget_5)
        self.label_20.setGeometry(QtCore.QRect(10, 380, 371, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.pushButton_8 = QtWidgets.QPushButton(self.widget_5)
        self.pushButton_8.setGeometry(QtCore.QRect(120, 450, 141, 71))
        self.pushButton_8.setObjectName("pushButton_8")
        self.label_28 = QtWidgets.QLabel(self.widget_5)
        self.label_28.setGeometry(QtCore.QRect(80, 70, 241, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget_5)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 120, 371, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.widget_6 = QtWidgets.QWidget(Form)
        self.widget_6.setGeometry(QtCore.QRect(0, 0, 386, 361))
        self.widget_6.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.widget_6.setObjectName("widget_6")
        self.label_14 = QtWidgets.QLabel(self.widget_6)
        self.label_14.setGeometry(QtCore.QRect(120, 10, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.widget_6)
        self.label_15.setGeometry(QtCore.QRect(210, 15, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.widget_6)
        self.label_16.setGeometry(QtCore.QRect(60, 60, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.label_25 = QtWidgets.QLabel(self.widget_6)
        self.label_25.setGeometry(QtCore.QRect(80, 150, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.pushButton_4 = QtWidgets.QPushButton(self.widget_6)
        self.pushButton_4.setGeometry(QtCore.QRect(130, 100, 91, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_7 = QtWidgets.QPushButton(self.widget_6)
        self.pushButton_7.setGeometry(QtCore.QRect(130, 190, 91, 41))
        self.pushButton_7.setObjectName("pushButton_7")
        self.label_26 = QtWidgets.QLabel(self.widget_6)
        self.label_26.setGeometry(QtCore.QRect(60, 250, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.pushButton_9 = QtWidgets.QPushButton(self.widget_6)
        self.pushButton_9.setGeometry(QtCore.QRect(130, 300, 91, 41))
        self.pushButton_9.setObjectName("pushButton_9")
        self.widget_7 = QtWidgets.QWidget(Form)
        self.widget_7.setGeometry(QtCore.QRect(0, 0, 386, 371))
        self.widget_7.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.widget_7.setObjectName("widget_7")
        self.label_21 = QtWidgets.QLabel(self.widget_7)
        self.label_21.setGeometry(QtCore.QRect(50, 70, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.widget_7)
        self.label_22.setGeometry(QtCore.QRect(50, 110, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.pushButton_6 = QtWidgets.QPushButton(self.widget_7)
        self.pushButton_6.setGeometry(QtCore.QRect(150, 172, 75, 61))
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_29 = QtWidgets.QLabel(self.widget_7)
        self.label_29.setGeometry(QtCore.QRect(80, 250, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_29.setFont(font)
        self.label_29.setObjectName("label_29")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget_7)
        self.lineEdit_4.setGeometry(QtCore.QRect(10, 290, 371, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton_13 = QtWidgets.QPushButton(self.widget_7)
        self.pushButton_13.setGeometry(QtCore.QRect(150, 320, 75, 23))
        self.pushButton_13.setObjectName("pushButton_13")
        self.widget_4 = QtWidgets.QWidget(Form)
        self.widget_4.setGeometry(QtCore.QRect(0, 0, 386, 201))
        self.widget_4.setObjectName("widget_4")
        self.label_23 = QtWidgets.QLabel(self.widget_4)
        self.label_23.setGeometry(QtCore.QRect(110, 20, 361, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.pushButton = QtWidgets.QPushButton(self.widget_4)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(0, 60, 41, 41))
        self.pushButton.setCheckable(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_15 = QtWidgets.QPushButton(self.widget_4)
        self.pushButton_15.setGeometry(QtCore.QRect(344, 60, 41, 41))
        self.pushButton_15.setObjectName("pushButton_15")
        self.tableWidget = QtWidgets.QTableWidget(self.widget_4)
        self.tableWidget.setGeometry(QtCore.QRect(45, 60, 291, 101))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        self.pushButton_17 = QtWidgets.QPushButton(self.widget_4)
        self.pushButton_17.setGeometry(QtCore.QRect(0, 0, 51, 51))
        self.pushButton_17.setStyleSheet("background-image: url(:/icons/icon/backup.png);")
        self.pushButton_17.setText("")
        self.pushButton_17.setObjectName("pushButton_17")
        self.widget_8 = QtWidgets.QWidget(Form)
        self.widget_8.setGeometry(QtCore.QRect(0, 0, 386, 231))
        self.widget_8.setObjectName("widget_8")
        self.label_24 = QtWidgets.QLabel(self.widget_8)
        self.label_24.setGeometry(QtCore.QRect(80, 10, 241, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.lineEdit = QtWidgets.QLineEdit(self.widget_8)
        self.lineEdit.setGeometry(QtCore.QRect(10, 50, 371, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_27 = QtWidgets.QLabel(self.widget_8)
        self.label_27.setGeometry(QtCore.QRect(110, 80, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget_8)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 120, 371, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_16 = QtWidgets.QPushButton(self.widget_8)
        self.pushButton_16.setGeometry(QtCore.QRect(140, 150, 75, 51))
        self.pushButton_16.setObjectName("pushButton_16")
        self.widget_10 = QtWidgets.QWidget(Form)
        self.widget_10.setGeometry(QtCore.QRect(0, 0, 386, 231))
        self.widget_10.setObjectName("widget_10")
        self.label_30 = QtWidgets.QLabel(self.widget_10)
        self.label_30.setGeometry(QtCore.QRect(30, 30, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_30.setFont(font)
        self.label_30.setObjectName("label_30")
        self.pushButton_10 = QtWidgets.QPushButton(self.widget_10)
        self.pushButton_10.setGeometry(QtCore.QRect(140, 130, 75, 41))
        self.pushButton_10.setObjectName("pushButton_10")
        self.label_31 = QtWidgets.QLabel(self.widget_10)
        self.label_31.setGeometry(QtCore.QRect(150, 30, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_31.setFont(font)
        self.label_31.setObjectName("label_31")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Акызум"))
        self.label.setText(_translate("Form", "АКЫЗУМ"))
        self.pushButton_2.setText(_translate("Form", "ПРАВИЛА"))
        self.pushButton_11.setText(_translate("Form", "ИГРА"))
        self.pushButton_14.setText(_translate("Form", "СТАТИСТИКА"))
        self.label_2.setText(_translate("Form", "Правила АКЫЗУМа"))
        self.label_5.setText(_translate("Form", "2. Второй слушает перевернутую"))
        self.label_6.setText(_translate("Form", " запись и пытыется повторить"))
        self.label_7.setText(_translate("Form", "3. В конце мы соединяем все части, "))
        self.label_8.setText(_translate("Form", "переворачиваем и второй игрок"))
        self.label_12.setText(_translate("Form", " фрагмен за фрагментом"))
        self.label_13.setText(_translate("Form", "пытается угадать песню"))
        self.label_3.setText(_translate("Form", "1. Сначала первый игрок записывает"))
        self.label_4.setText(_translate("Form", " песню втайне от второго игрока"))
        self.label_9.setText(_translate("Form", "Как только будете готовы нажмите на кнопку ниже для записи"))
        self.label_10.setText(_translate("Form", "кнопку ниже"))
        self.pushButton_3.setText(_translate("Form", "СТАРТ!!!"))
        self.label_11.setText(_translate("Form", "ВАРНИНГ!!! У вас есть только 12 секунд!"))
        self.label_17.setText(_translate("Form", "Зовите второго игрока"))
        self.label_18.setText(_translate("Form", "Ниже вы можете прослушать запись первого"))
        self.label_19.setText(_translate("Form", "игрока"))
        self.pushButton_5.setText(_translate("Form", "ПРОСЛУШАТЬ!!!"))
        self.label_20.setText(_translate("Form", "Готов записать песню по частям? Жми на кнопку"))
        self.pushButton_8.setText(_translate("Form", "К ЗАПИСИ!!!"))
        self.label_28.setText(_translate("Form", "Введите свое имя, Игрок 2:"))
        self.lineEdit_3.setText(_translate("Form", "Игрок 2"))
        self.label_14.setText(_translate("Form", "часть:"))
        self.label_15.setText(_translate("Form", "1"))
        self.label_16.setText(_translate("Form", "Прослушать часть"))
        self.label_25.setText(_translate("Form", "Записать часть"))
        self.pushButton_4.setText(_translate("Form", "Прослушать"))
        self.pushButton_7.setText(_translate("Form", "Записать"))
        self.label_26.setText(_translate("Form", "Следующая часть"))
        self.pushButton_9.setText(_translate("Form", "Некст"))
        self.label_21.setText(_translate("Form", "Готовы прослушать результат и попытаться угадать песню?"))
        self.label_22.setText(_translate("Form", " и попытаться угадать песню?"))
        self.pushButton_6.setText(_translate("Form", "СЛУШАТЬ!!!"))
        self.label_29.setText(_translate("Form", "Впишите ответ ниже:"))
        self.lineEdit_4.setText(_translate("Form", "Название песни"))
        self.pushButton_13.setText(_translate("Form", "Готово"))
        self.label_23.setText(_translate("Form", "СТАТИСТИКА"))
        self.pushButton.setText(_translate("Form", "<"))
        self.pushButton_15.setText(_translate("Form", ">"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "1 Игрок"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "2 Игрок"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Победил"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("Form", "п"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("Form", "п"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("Form", "п"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.label_24.setText(_translate("Form", "Введите свое имя, Игрок 1:"))
        self.lineEdit.setText(_translate("Form", "Игрок 1"))
        self.label_27.setText(_translate("Form", "И название песни:"))
        self.lineEdit_2.setText(_translate("Form", "Песня"))
        self.pushButton_16.setText(_translate("Form", "Продолжить"))
        self.label_30.setText(_translate("Form", "Победил"))
        self.pushButton_10.setText(_translate("Form", "Домой"))
        self.label_31.setText(_translate("Form", "Игрок"))


class Main(QWidget, GUI):
    def __init__(self):
        super().__init__()
        self.i = 0
        self.chast = '1'
        self.con = sqlite3.connect("Static.db")
        self.abc = 'йцукенгшщзхъёфывапролджэячсмитьбю '
        self.cur = self.con.cursor()
        self.func = Functional()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.widget.show()
        self.widget_2.hide()
        self.widget_3.hide()
        self.widget_5.hide()
        self.widget_4.hide()
        self.widget_6.hide()
        self.widget_7.hide()
        self.widget_8.hide()
        self.widget_10.hide()
        # Кнопка правила
        self.pushButton_2.clicked.connect(self.rules)
        # Кнопка возвращения назад(стрелочка)
        self.pushButton_12.clicked.connect(self.mainback)
        # Кнопка Готово в конце игры
        self.pushButton_13.clicked.connect(self.end)
        # Кнопка Кнопка игра
        self.pushButton_11.clicked.connect(self.game)
        # Кнопка возвращения начала записи первого игрока
        self.pushButton_3.clicked.connect(self.start)
        # Кнопка прослушивания записи первого игрока
        self.pushButton_5.clicked.connect(self.func.play)
        # Кнопка переход к записи частей
        self.pushButton_8.clicked.connect(self.zapic)
        # Кнопка следующей части
        self.pushButton_9.clicked.connect(self.smena)
        # Кнопка воспроизведение части(1ого игрока)
        self.pushButton_4.clicked.connect(self.func.proig_chasti)
        # Кнопка записи части
        self.pushButton_7.clicked.connect(self.func.zapic_chasti)
        # Кнопка прослушка результата
        self.pushButton_6.clicked.connect(self.func.play_end)
        # Кнопка возвращение домой
        self.pushButton_10.clicked.connect(self.back)
        # Кнопка статистика
        self.pushButton_14.clicked.connect(self.stat)
        # Кнопка возвращения назад(стрелочка)
        self.pushButton_17.clicked.connect(self.mainback)
        # Кнопка назад(в статистике)
        self.pushButton.clicked.connect(self.left)
        # Кнопка вперед(в статистике)
        self.pushButton_15.clicked.connect(self.right)
        # Кнопка перехода к записи песни первым игроком
        self.pushButton_16.clicked.connect(self.cont)

    def rules(self):
        # меняет на экран с правилами
        self.widget.hide()
        self.widget_2.show()

    def back(self):
        # возвращение на главный экран в конце игры
        self.widget_10.hide()
        self.widget.show()
        # занесение статистики в БД
        self.cur.execute("""INSERT INTO players(player_1,player_2) VALUES(?,?)""", (self.player_1, self.player_2))
        self.cur.execute("""INSERT INTO statistic(winner) VALUES(?)""", (self.pobeda, ))
        self.con.commit()
        self.resize(386, 548)

    def end(self):
        # проверка правильности ответа и вывод победителя
        if len(self.lineEdit_4.text()) != 0:
            self.otvet = self.lineEdit_4.text().lower()
            self.otv = ''
            for el in self.otvet:
                if el in self.abc:
                    self.otv += el
            if self.otv == self.song_1:
                self.pobeda = '2'
            else:
                self.pobeda = '1'
            self.widget_7.hide()
            self.widget_10.show()
            self.label_31.setText('Игрок ' + self.pobeda)
            self.resize(386, 231)

    def cont(self):
        # передача переменным имени 1ого мгрока и песни
        if len(self.lineEdit.text()) != 0 and len(self.lineEdit_2.text()) != 0:
            self.player_1 = self.lineEdit.text()
            self.song = self.lineEdit_2.text().lower()
            self.song_1 = ''
            # упрощение названия(без спецсимволов)
            for el in self.song:
                if el in self.abc:
                    self.song_1 += el
            self.widget_8.hide()
            self.widget_3.show()
            self.resize(386, 151)

    def left(self):
        # (в статистике) перемещение на одну игру позже
        self.pushButton_15.setEnabled(True)
        self.i -= 1
        # сбор статистики
        pobed = self.cur.execute("""SELECT winner FROM Statistic
                                                    WHERE ID = ?""", (self.i,)).fetchall()
        players = self.cur.execute("""SELECT player_1, player_2 FROM players
                                                        WHERE ID = ?""", (self.i,)).fetchall()
        # занесение в таблицу
        item = self.tableWidget.item(0, 0)
        item.setText(players[0][0])
        item = self.tableWidget.item(0, 1)
        item.setText(players[0][1])
        item = self.tableWidget.item(0, 2)
        if pobed[0][0] == 1:
            item.setText(str(pobed[0][0]) + '-ый')
        else:
            item.setText(str(pobed[0][0]) + '-ой')
        if self.i == 0:
            self.pushButton.setEnabled(False)

    def right(self):
        # (в статистике) перемещение на одну игру раньше
        self.pushButton.setEnabled(True)
        self.i += 1
        pobed = self.cur.execute("""SELECT winner FROM Statistic
                                            WHERE ID = ?""", (self.i,)).fetchall()
        players = self.cur.execute("""SELECT player_1, player_2 FROM players
                                                WHERE ID = ?""", (self.i,)).fetchall()
        # занесение в таблицу
        item = self.tableWidget.item(0, 0)
        item.setText(players[0][0])
        item = self.tableWidget.item(0, 1)
        item.setText(players[0][1])
        item = self.tableWidget.item(0, 2)
        if pobed[0][0] == 1:
            item.setText(str(pobed[0][0]) + '-ый')
        else:
            item.setText(str(pobed[0][0]) + '-ой')
        res = self.cur.execute("""SELECT * FROM Statistic""").fetchall()
        if len(res) - 1 == self.i:
            self.pushButton_15.setEnabled(False)

    def mainback(self):
        # возвращение на главную стр
        self.widget.show()
        self.widget_2.hide()
        self.widget_3.hide()
        self.widget_4.hide()
        self.widget_5.hide()
        self.widget_6.hide()
        self.widget_7.hide()
        self.widget_8.hide()
        self.widget_10.hide()
        self.resize(386, 548)

    def game(self):
        self.widget.hide()
        self.widget_8.show()
        self.resize(386, 231)

    def zapic(self):
        if len(self.lineEdit_3.text()) != 0:
            self.widget.hide()
            self.widget_2.hide()
            self.widget_3.hide()
            self.widget_5.hide()
            self.widget_6.show()
            self.widget_7.hide()
            self.resize(386, 361)
            self.player_2 = self.lineEdit_3.text()
            self.func.delenie()

    def start(self):
        self.widget_3.hide()
        self.widget_5.show()

        self.func.start_rec()

        self.resize(386, 548)

    def stat(self):
        # вход на стр таблицы
        self.widget.hide()
        self.widget_4.show()
        self.resize(386, 201)
        self.i = 0
        # ее инициализация при:
        res = self.cur.execute("""SELECT * FROM statistic""").fetchall()
        if len(res) == 0:
            # нулевой таблице
            self.pushButton.setEnabled(False)
            self.pushButton_15.setEnabled(False)
            item = self.tableWidget.item(0, 0)
            item.setText('')
            item = self.tableWidget.item(0, 1)
            item.setText('')
            item = self.tableWidget.item(0, 2)
            item.setText('')
        else:
            if len(res) == 1:
                # таблице с одной игрой
                self.pushButton_15.setEnabled(False)
            # с несколькими играми + одной игрой
            self.pushButton.setEnabled(False)
            pobed = self.cur.execute("""SELECT winner FROM statistic
                                    WHERE ID = ?""", (self.i,)).fetchall()
            players = self.cur.execute("""SELECT player_1, player_2 FROM players
                                        WHERE ID = ?""", (self.i,)).fetchall()
            item = self.tableWidget.item(0, 0)
            item.setText(players[0][0])
            item = self.tableWidget.item(0, 1)
            item.setText(players[0][1])
            item = self.tableWidget.item(0, 2)
            if pobed[0][0] == 1:
                item.setText(str(pobed[0][0]) + '-ый')
            else:
                item.setText(str(pobed[0][0]) + '-ой')


    def smena(self):
        # изменение цифр и текста на стр записи частей
        if self.chast != '3' and self.chast != '4':
            self.label_15.setText(str(int(self.chast) + 1))
            self.chast = str(int(self.chast) + 1)
            self.func.get_chast(self.chast)
        elif self.chast == '3':
            self.label_15.setText(str(int(self.chast) + 1))
            self.chast = str(int(self.chast) + 1)
            self.label_26.setText('Конец игры')
            self.pushButton_9.setText('Конец')
            self.func.get_chast(self.chast)
        else:
            self.func.slozh_chastej()
            self.widget_6.hide()
            self.widget_7.show()


class Functional:
    def __init__(self):
        self.chast = '1'

    def get_chast(self, chast):
        self.chast = chast

    def play_end(self):
        chunk = 1024
        # воспроизводит результат записи второго игрока

        # open a wav format music
        f = wave.open("resultat.wav", "rb")
        # instantiate PyAudio
        p = pyaudio.PyAudio()
        # open stream
        stream = p.open(format=p.get_format_from_width(f.getsampwidth()),
                        channels=f.getnchannels(),
                        rate=f.getframerate(),
                        output=True)
        # read data
        data = f.readframes(chunk)

        # play stream
        while data:
            stream.write(data)
            data = f.readframes(chunk)

            # stop stream
        stream.stop_stream()
        stream.close()

        # close PyAudio
        p.terminate()

    def slozh_chastej(self):
        source1 = wave.open("output1.wav", mode="rb")
        source2 = wave.open("output2.wav", mode="rb")
        source3 = wave.open("output3.wav", mode="rb")
        source4 = wave.open("output4.wav", mode="rb")
        dest = wave.open("resultat.wav", mode="wb")

        dest.setparams(source1.getparams())
        dest.setnframes(source1.getnframes() * 4)
        frames_count = source1.getnframes()

        # переворачивает записи
        data = struct.unpack(">" + str(frames_count) + "i", source1.readframes(frames_count))
        newdata1 = data[::-1]
        data = struct.unpack(">" + str(frames_count) + "i", source2.readframes(frames_count))
        newdata2 = data[::-1]
        data = struct.unpack(">" + str(frames_count) + "i", source3.readframes(frames_count))
        newdata3 = data[::-1]
        data = struct.unpack(">" + str(frames_count) + "i", source4.readframes(frames_count))
        newdata4 = data[::-1]
        newdata = newdata4 + newdata3 + newdata2 + newdata1

        # записывает их в resultat.wav
        newframes = struct.pack(">" + str(len(newdata)) + "i", *newdata)
        dest.writeframes(newframes)
        source1.close()
        source2.close()
        source3.close()
        source4.close()
        dest.close()

    def proig_chasti(self):
        chunk = 1024
        # проигрывание одной из частей игрока 1
        # open a wav format music
        f = wave.open("chast" + self.chast + ".wav", "rb")
        # instantiate PyAudio
        p = pyaudio.PyAudio()
        # open stream
        stream = p.open(format=p.get_format_from_width(f.getsampwidth()),
                        channels=f.getnchannels(),
                        rate=f.getframerate(),
                        output=True)
        # read data
        data = f.readframes(chunk)

        # play stream
        while data:
            stream.write(data)
            data = f.readframes(chunk)

            # stop stream
        stream.stop_stream()
        stream.close()

        # close PyAudio
        p.terminate()

    def zapic_chasti(self):
        # игрок 2 записывает одну из частей
        CHUNK = 1024
        FORMAT = pyaudio.paInt16
        CHANNELS = 2
        RATE = 44100
        RECORD_SECONDS = 5
        WAVE_OUTPUT_FILENAME = "output" + self.chast + ".wav"
        p = pyaudio.PyAudio()

        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)

        print("* recording")

        frames = []

        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)

        print("* done recording")

        stream.stop_stream()
        stream.close()
        p.terminate()

        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()

        source = wave.open("output" + self.chast + ".wav", mode="rb")
        dest = wave.open("reversed" + self.chast + ".wav", mode="wb")

        dest.setparams(source.getparams())
        frames_count = source.getnframes()

        data = struct.unpack(">" + str(frames_count) + "i", source.readframes(frames_count))
        newdata = data[::-1]

        newframes = struct.pack(">" + str(len(newdata)) + "i", *newdata)
        dest.writeframes(newframes)
        source.close()
        dest.close()

    def play(self):
        # define stream chunk
        chunk = 1024
        # полное воспроизведение перевернутой версии песни 1ого игрока

        # open a wav format music
        f = wave.open("reversed.wav", "rb")
        # instantiate PyAudio
        p = pyaudio.PyAudio()
        # open stream
        stream = p.open(format=p.get_format_from_width(f.getsampwidth()),
                        channels=f.getnchannels(),
                        rate=f.getframerate(),
                        output=True)
        # read data
        data = f.readframes(chunk)

        # play stream
        while data:
            stream.write(data)
            data = f.readframes(chunk)

            # stop stream
        stream.stop_stream()
        stream.close()

        # close PyAudio
        p.terminate()

    def delenie(self):
        # дробление перевернутой песни 1ого игрока на части
        source = wave.open("reversed.wav", mode="rb")
        dest1 = wave.open("chast1.wav", mode="wb")
        dest2 = wave.open("chast2.wav", mode="wb")
        dest3 = wave.open("chast3.wav", mode="wb")
        dest4 = wave.open("chast4.wav", mode="wb")

        dest1.setparams(source.getparams())
        dest2.setparams(source.getparams())
        dest3.setparams(source.getparams())
        dest4.setparams(source.getparams())
        frames_count = source.getnframes()

        data = struct.unpack(">" + str(frames_count) + "i", source.readframes(frames_count))
        chast1 = data[0:frames_count // 4]
        chast2 = data[frames_count // 4:frames_count // 2]
        chast3 = data[frames_count // 2:((frames_count // 2) + (frames_count // 4))]
        chast4 = data[((frames_count // 2) + (frames_count // 4)):frames_count]

        newframes1 = struct.pack(">" + str(len(chast1)) + "i", *chast1)
        newframes2 = struct.pack(">" + str(len(chast2)) + "i", *chast2)
        newframes3 = struct.pack(">" + str(len(chast3)) + "i", *chast3)
        newframes4 = struct.pack(">" + str(len(chast4)) + "i", *chast4)
        dest1.writeframes(newframes1)
        dest2.writeframes(newframes2)
        dest3.writeframes(newframes3)
        dest4.writeframes(newframes4)
        source.close()
        dest1.close()
        dest2.close()
        dest3.close()
        dest4.close()

    def start_rec(self):
        # запись 1ым игроком песни
        CHUNK = 1024
        FORMAT = pyaudio.paInt16
        CHANNELS = 2
        RATE = 44100
        RECORD_SECONDS = 13
        WAVE_OUTPUT_FILENAME = "output.wav"
        p = pyaudio.PyAudio()
        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)
        print("* recording")
        frames = []
        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)
        print("* done recording")
        stream.stop_stream()
        stream.close()
        p.terminate()
        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()
        source = wave.open("output.wav", mode="rb")
        dest = wave.open("reversed.wav", mode="wb")
        dest.setparams(source.getparams())
        frames_count = source.getnframes()
        data = struct.unpack(">" + str(frames_count) + "i", source.readframes(frames_count))
        newdata = data[::-1]
        newframes = struct.pack(">" + str(len(newdata)) + "i", *newdata)
        dest.writeframes(newframes)
        source.close()
        dest.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec())
