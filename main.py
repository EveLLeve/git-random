import sys

from UI import Ui_MainWindow
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QApplication, QMainWindow

from random import randint


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        self.do = False
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run)

    def paintEvent(self, event):
        if self.do:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()
        self.do = False

    def draw_flag(self, qp):
        for i in range(15):
            qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
            w = randint(0, 100)
            qp.drawEllipse(randint(0 + w, 800 - w), randint(0 + w, 600 - w), w, w)

    def run(self):
        self.do = True
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
