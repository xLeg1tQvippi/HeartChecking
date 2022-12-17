from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit
from instr.py import *

# app = QApplication([]) # !Конструктор, создаёт объяект - Приложение.
# app.exec_() #*Оставляет приложение открытым, untill Не нажата кнопка выхода
# mw = QWdiget() # !Конструктор создаёт объект - Окно
# mw.show()  #Сделать окно видимым
# mw.setWindowTitle('Определить победитея') # TODO Заголовок окна. (название)
# mw.move(900, 70) #*Появление окна в указанной точке (А не по центру экрана)
# mw.resize(400,500) #*Изменение размеров окна
# mw.hide() #Скрыть окно
# mwtext = QLabel('Победитель') # !Конструктор, создающий объект "Надпись" с указанным текстом.
# mwtext.setText('34') # TODO Метод который изменяет надпись
# mwtext.text() #Позволяет получить текст надписи
# button = QPushButton('Сгенерировать') # !Конструктор, создающий объект - Кнопка с Надписью.
# button.setText('Новый текст') # TODO Метод изменяющий текст на кнопке.
# button.text() #Метод позволяющий получить текст, надписи на кнопке.
# v_line = QVBoxLayout() # !Конструктор, создающий объект - Вертикальная линия
# v_line.addWidget(tittle, alignment=Qt.AlignCenter) # TODO Метод добавляющий виджет к линии и располагающий его по центру
# mw.setLayout(v_line) #TODO Добавить получившуюся линию и расположенные на ней виджеты в окно приложения


# name.QLineEdit("") #TODO Добавление текста виджета (Способ работы "input" с текстом и рамкой)

class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def initUI(self):
        self.h_line = QHBoxLayout()
        self.r_line = QVBoxLayout()
        self.l_line = QVBoxLayout()
        self.l_line.addWidget(self.pass) #
        self.r_line.addWidget(self.pass) #
        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        self.setLayout(self.h_line)

    def connects(self):
        self.bnt_next.clicked.connect(self.next_click)

    def next_click(self):
        self.hide()
        self.fw = final_win()