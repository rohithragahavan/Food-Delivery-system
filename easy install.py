import sys
from PyQt5.QtWidgets import (QWidget, QToolTip,
    QPushButton, QApplication, QLabel, QLineEdit, QComboBox)
from PyQt5.QtGui import QFont,QPixmap
from PyQt5.QtCore import QRect



class Admin_login(QWidget):

    def __init__(self):
        super().__init__()
        self.top=100
        self.left=100
        self.width=800
        self.height=500
        self.label1()

    def label1(self):
        self.setWindowTitle("Login")
        self.setGeometry(self.left,self.top,self.width,self.height)

        self.label = QLabel(self)
        self.label.setPixmap(QPixmap("new3.jpg"))

        self.lbl = QLabel(self)
        self.lbl.setFont(QFont('SansSerif', 14))
        self.lbl.setStyleSheet("color: rgb(0,0,255)")
        self.lbl.setStyleSheet("fontName='Times-Italic'")
        self.lbl.setText('Username')
        self.lbl.adjustSize()
        self.lbl.move(50, 50)

        self.line = QLineEdit(self)
        self.line.setFont(QFont('SansSerif', 14))
        self.line.move(200, 50)
        self.line.adjustSize()

        self.lbl = QLabel(self)
        self.lbl.setFont(QFont('Cooper', 14))
        self.lbl.setText('Password')
        self.lbl.adjustSize()
        self.lbl.move(50, 180)

        self.line = QLineEdit(self)
        self.line.setFont(QFont('Cooper', 14))
        self.line.move(200,180)
        self.line.adjustSize()

        self.pushbutton1 = QPushButton("Login", self)
        self.pushbutton1.setFont(QFont('SansSerif', 14))
        self.pushbutton1.resize(self.pushbutton1.sizeHint())
        self.pushbutton1.move(300, 280)
        self.pushbutton1.clicked.connect(self.linked)

        self.show()

    def linked(self):
        from Weladmin import Voption
        self.Vopt=Voption()
        self.close()
        self.Vopt.show()
        print("login button is clicked")






if __name__=="__main__":
    app = QApplication(sys.argv)
    admin =Admin_login()
    sys.exit(app.exec_())