import sys
import random

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt
from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QWidget, QLabel

class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui.ui', self)
        self.x, self.y = 0, 0
        self.rad = 0
        self.count = ''
        self.pushButton.clicked.connect(self.paintEvent)

    def paintEvent(self, event):
        self.rad = random.randint(4, 80)
        self.x = random.randint(0, 300)
        self.y = random.randint(0, 300)
        qp = QPainter()
        qp.begin(self)
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(self.x - self.rad, self.y - self.rad, 2 * self.rad, 2 * self.rad)
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())