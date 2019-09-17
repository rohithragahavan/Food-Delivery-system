import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QFrame, QPushButton, QGroupBox, QVBoxLayout, QAction, \
    QGridLayout, QLineEdit, QLabel, QMessageBox, QPlainTextEdit, QRadioButton
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtCore import pyqtSlot
from subprocess import call


class App(QMainWindow):
    def __init__(self):

        super().__init__()
        self.title = 'Book'
        self.left = 10
        self.top = 10
        self.width = 500
        self.height = 500
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.lh = QLabel(self)
        self.lh.move(0, 0)
        self.lh.resize(600, 200)
        self.head = QPixmap('head.png')
        self.lh.setPixmap(self.head)
        self.lh.resize(self.head.width(), self.head.height())

        # create label
        self.lname = QLabel('Amount', self)
        self.lname.move(150, 100)

        self.name = QLabel(self)
        self.name.move(100, 120)
        self.name.resize(180, 20)
        self.show()

    def on_click1(self):

        self.Reply = QMessageBox.question(self, QMessageBox.Yes)
        if self.Reply == QMessageBox.Yes:
            print('Yes clicked.')
            self.close()
            call(["python", "main.py"])

    def on_click(self):

        self.Reply = QMessageBox.question(self, QMessageBox.Yes)
        if self.Reply == QMessageBox.Yes:
            print('Yes clicked.')
            self.close()
            call(["python", "book food.py"])\
            

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())