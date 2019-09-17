import sys
import mysql.connector
from subprocess import call
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QLabel, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
 
class App(QMainWindow):
 
    def __init__(self):
        super().__init__()
        self.title = 'Log in'
        self.left = 100
        self.top = 100
        self.width = 400
        self.height = 200
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        #create label
        self.lbl1 = QLabel('Username', self)
        self.lbl1.move(50,50)
        
        self.lbl2 = QLabel('Password', self)
        self.lbl2.move(50,100)
        
        # Create textbox
        self.username = QLineEdit(self)
        self.username.move(120, 50)
        self.username.resize(200,30)
        
        self.pwd = QLineEdit(self)
        self.pwd.move(120, 100)
        self.pwd.resize(200,30)
         
        # Create a button in the window
        
        self.reg = QPushButton('Register', self)
        self.reg.move(200,150)
        #self.reg.clicked.connect(self.on_click1)
        
        self.log= QPushButton('Log in', self)
        self.log.move(50,150)
        #self.log.clicked.connect(self.on_click)
 
        self.show()
        
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())