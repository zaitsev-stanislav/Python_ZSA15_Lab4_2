#!/usr/bin/env python3
# coding=utf-8

import re
import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi


class Main(QDialog):
    def __init__(self):
        super(Main, self).__init__()
        loadUi('uis/main.ui', self)

        self.setWindowTitle('Работа со строками в Python')
        self.setWindowIcon(QtGui.QIcon('images/logo.png'))

        self.btn_solve.clicked.connect(self.solve)
        self.btn_clear.clicked.connect(self.clear)

    def solve(self):
        self.textEdit_words.clear()
        text = self.textEdit_text.toPlainText().split()  # получаем наш текст
        array = []
        for word in text:
            if word and word[0] == word[-1]:
                array.append(word)
                self.textEdit_words.insertPlainText("[" + word + "]" + "\n")

        self.textEdit_words.insertPlainText("Кол-во слов - " + str(len(array)))

    def clear(self):
        self.textEdit_text.clear()
        self.textEdit_words.clear()


def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()