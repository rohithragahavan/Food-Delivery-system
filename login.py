import sys
import mysql.connector
from subprocess import call
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QLabel, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
#database connection        
conn = mysql.connector.connect(host="localhost", user="root", passwd="", database="mini")
mycu = conn.cursor()
 
class App(QMainWindow):
 
    def __init__(self):
        super().__init__()
        self.title = 'Log in'
        self.left = 100
        self.top = 100
        self.width = 500
        self.height = 300
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
        self.pwd.setEchoMode(QLineEdit.Password)
        self.pwd.move(120, 100)
        self.pwd.resize(200,30)
         
        # Create a button in the window
        
        self.reg = QPushButton('Register', self)
        self.reg.move(200,150)
        self.reg.clicked.connect(self.on_click1)
        
        self.log= QPushButton('Log in', self)
        self.log.move(50,150)
        self.log.clicked.connect(self.on_click)
 
        self.show()
        
    def on_click(self):
        username = self.username.text()
        passw = self.pwd.text()
        mycu.execute('SELECT * FROM reg WHERE username = "'+username+'" AND password = "'+passw+'"')
        res = mycu.fetchone()
        if(not res):
            QMessageBox.about(self, 'Login', 'Invalid Details!!')
            self.resetform()
        else:
            print('Logged in Successfully')
            self.Reply = QMessageBox.question(self, 'Login', "Logged in successfull", QMessageBox.Yes)
            if self.Reply == QMessageBox.Yes:
                print('Yes clicked.')
            from main import App
            self.m=App(username)
            self.m.show()
            self.close()
            
            mycu.execute('SELECT *  FROM reg where username = "'+username+'"')
            res = mycu.fetchall()
            for x in res:
                global currentuser
                currentuser = x[0]
                global currentname
                currentname = x[3]
            self.m.l1.setText("<h2>Welcome %s</h2>" % currentuser)
            
            
    def on_click1(self):
        print('clicked Regsiter.')
        from register import App
        self.m=App()
        self.m.show()
        self.close()
        
    def resetform(self):
        self.username.setText('')
        self.pwd.setText('')
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
