import sys
import mysql.connector
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget,QFrame, QPushButton, QGroupBox, QVBoxLayout, QAction,QGridLayout, QLineEdit, QLabel, QMessageBox, QPlainTextEdit, QRadioButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from subprocess import call
from datetime import date

#database connection
conn = mysql.connector.connect(host="localhost", user="root", passwd="", database="mini")
mycu = conn.cursor()

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Registration'
        self.left = 100
        self.top = 100
        self.width = 500
        self.height = 500
        self.gender=""
        self.initUI()
 
    def initUI(self):
        
        
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        #create label
        self.lname = QLabel('Name', self)
        self.lname.move(50,50)
        
        self.lgen= QLabel('Gender', self)
        self.lgen.move(50,100)
        
        self.ladd= QLabel('Address', self)
        self.ladd.move(50,150)
        
        self.luser= QLabel('Username', self)
        self.luser.move(50,250)
        
        self.lpwd= QLabel('Password', self)
        self.lpwd.move(50,300)
        
        self.lpwd= QLabel('Re-Enter Password', self)
        self.lpwd.move(50,350)
        
        # Create textbox
        self.name = QLineEdit(self)
        self.name.move(150, 50)
        self.name.resize(200,25)
        

        self.frame1 = QFrame(self)
        self.frame1.move(150, 100)
        self.radioBtn1 = QRadioButton("Male", self.frame1)
        self.radioBtn1.setChecked(True)
        self.radioBtn1.move(0, 0)
        self.radioBtn2 = QRadioButton("Female",self.frame1)
        self.radioBtn2.move(0, 15)
        
            
        self.address = QLineEdit(self)
        self.address.move(150, 150)
        self.address.resize(200,90)

        self.user = QLineEdit(self)
        self.user.move(150, 250)
        self.user.resize(200,25)
        
        self.pwd= QLineEdit(self)
        self.pwd.move(150, 300)
        self.pwd.resize(200,25)
        
        self.pwd1 = QLineEdit(self)
        self.pwd1.move(150, 350)
        self.pwd1.resize(200,30)
        
        
        
         
        # Create a button in the window
        
        self.reg = QPushButton('Register', self)
        self.reg.move(50,400)
        self.reg.clicked.connect(self.on_click)
        
        self.log= QPushButton("Login page",self)
        self.log.move(200,400)
        self.log.clicked.connect(self.on_click1)
        
        self.reset = QPushButton("Reset",self)
        self.reset.move(350,400)
        self.reset.clicked.connect(self.on_click2)
        
        self.show()
        
  
    def on_click(self):
        if(self.radioBtn1.isChecked()):
            self.gender="Male"
        else:
            if(self.radioBtn2.isChecked()):
                self.gender="Female"
        name=self.name.text()
        gender=self.gender
        pwd=self.pwd.text()
        pwd1=self.pwd1.text()
        address=self.address.text()
        user=self.user.text()
        if(name=='' or address=='' or user=='' or pwd=='' or pwd1==''):
            QMessageBox.about(self, 'Register', 'Some fields are still incomplete!')
        else:
            if(pwd!=pwd1):
                QMessageBox.about(self, "Password", "Password Doesn't Match")
            else:
                mycu.execute("SELECT username FROM reg")
                res = mycu.fetchall()
                if(user in str(res)):
                    QMessageBox.about(self, 'Register', 'Account already Exists or change username !')
                else:
                    print(user)
                    mycu.execute("CREATE TABLE "+user+" (food VARCHAR(100),hotel VARCHAR(50) ,rupees INTEGER, date DATE)")
                    conn.commit()
                    que = "INSERT INTO reg (name, gender, address, username, password) VALUES (%s, %s, %s, %s, %s)"
                    vala = (name, gender, address, user,pwd )
                    mycu.execute(que, vala)
                    conn.commit()
                print('Registered Successfully')
                self.Reply = QMessageBox.question(self, 'Registartion', "Registration successfull", QMessageBox.Yes)
                if self.Reply == QMessageBox.Yes:
                    print('Yes clicked.')
                    from login import App
                    self.sw=App()
                    self.sw.show()
                    self.close()

            
    def on_click1(self):
        from login import App
        self.a= App()
        self.a.show()
        self.close()
        
    def on_click2(self):
        self.name.setText("")
        self.address.setText("")
        self.pwd.setText("")
        self.pwd1.setText("")
        self.user.setText("")
        self.radioBtn1.setChecked(True)
        
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
