import sys
from PyQt5.QtWidgets import (QWidget, QToolTip,
    QPushButton, QApplication, QLabel, QLineEdit, QComboBox)
from PyQt5.QtGui import QFont,QPixmap
from PyQt5.QtCore import QRect

class Voption(QWidget):

    def __init__(self):
        super().__init__()
        self.top=100
        self.left=100
        self.width=800
        self.height=500
        self.Rozokar()

    def Rozokar(self):
        self.setWindowTitle("Welcome Admin")
        self.setGeometry(self.left,self.top,self.width,self.height)

        self.label = QLabel(self)
        self.label.setPixmap(QPixmap("new3.jpg"))

        self.pushbutton1=QPushButton("Add Employee",self)
        self.pushbutton1.setFont(QFont('SansSerif', 14))
        self.pushbutton1.resize(self.pushbutton1.sizeHint())
        self.pushbutton1.move(300, 100)
        self.pushbutton1.clicked.connect(self.linked_to_addemp)


        self.pushbutton2 = QPushButton("Edit Employee Details", self)
        self.pushbutton2.setFont(QFont('SansSerif', 14))
        self.pushbutton2.resize(self.pushbutton2.sizeHint())
        self.pushbutton2.move(300, 200)
        self.pushbutton2.clicked.connect(self.linked_to_editemp)

        self.pushbutton3 = QPushButton("Remove Employee", self)
        self.pushbutton3.setFont(QFont('SansSerif', 14))
        self.pushbutton3.resize(self.pushbutton3.sizeHint())
        self.pushbutton3.move(300, 300)

        self.pushbutton4 = QPushButton("Prepare Monthly Salary", self)
        self.pushbutton4.setFont(QFont('SansSerif', 14))
        self.pushbutton4.resize(self.pushbutton4.sizeHint())
        self.pushbutton4.move(300, 400)

        self.show()

    def linked_to_addemp(self):
        from addemp import Addemp
        self.Add_emp=Addemp()
        self.Add_emp.show()
        self.close()

    def linked_to_editemp(self):
        from editemp import Editemp
        self.Edit_emp=Editemp()
        self.Edit_emp.show()
        self.close()











if __name__=="__main__":
    app=QApplication(sys.argv)
    Vopt=Voption()
    sys.exit(app.exec())