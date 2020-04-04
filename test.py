import sys  # sys нужен для передачи argv в QApplication
import os  # Отсюда нам понадобятся методы для отображения содержимого директорий

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *

import design  # Это наш конвертированный файл дизайна

class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        # self.btnBrowse.clicked.connect(self.browse_folder)  # Выполнить функцию browse_folder
        #                                                     # при нажатии кнопки

        self.btn_0.clicked.connect(lambda: self.add_number("0"))
        self.btn_1.clicked.connect(lambda: self.add_number("1"))
        self.btn_2.clicked.connect(lambda: self.add_number("2"))
        self.btn_3.clicked.connect(lambda: self.add_number("3"))
        self.btn_4.clicked.connect(lambda: self.add_number("4"))
        self.btn_5.clicked.connect(lambda: self.add_number("5"))
        self.btn_6.clicked.connect(lambda: self.add_number("6"))
        self.btn_7.clicked.connect(lambda: self.add_number("7"))
        self.btn_8.clicked.connect(lambda: self.add_number("8"))
        self.btn_9.clicked.connect(lambda: self.add_number("9"))
        self.btn_point.clicked.connect(lambda: self.add_number("."))

        self.btn_plus.clicked.connect(lambda: self.add_number("+"))
        self.btn_minus.clicked.connect(lambda: self.add_number("-"))
        self.btn_mlt.clicked.connect(lambda: self.add_number("*"))
        self.btn_div.clicked.connect(lambda: self.add_number("/"))
        self.btn_left.clicked.connect(lambda: self.add_number("("))
        self.btn_right.clicked.connect(lambda: self.add_number(")"))

        self.btn_eq.clicked.connect(lambda: self.calculate())
        self.btn_clear.clicked.connect(lambda: self.clear())


    def add_number(self, value):
    	if value == ".":
    		if value not in self.result.text():
    			line = self.result.text()
    			line += value
    			self.result.setText(line)
    	else:
    		line = self.result.text()
    		line += value
    		self.result.setText(line)

    def add_operation(self, value):
    	line = self.result.text()
    	line += value
    	self.result.setText(line)

    def calculate(self):
    	try:
    		answer = eval(self.result.text())
    		self.result.setText(str(answer))
    	except ZeroDivisionError:
    		print("ZeroDivisionError")
    		
    def clear(self):
    	self.result.setText("")

    # def browse_folder(self):
    #     self.listWidget.clear()  # На случай, если в списке уже есть элементы
    #     directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Выберите папку")
    #     # открыть диалог выбора директории и установить значение переменной
    #     # равной пути к выбранной директории

    #     if directory:  # не продолжать выполнение, если пользователь не выбрал директорию
    #         for file_name in os.listdir(directory):  # для каждого файла в директории
    #             self.listWidget.addItem(file_name)   # добавить файл в listWidget

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.setWindowTitle('Calculator App')
    window.setGeometry(400, 100, 300, 400)
    window.setFixedSize(300, 400)
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()