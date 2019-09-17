import sys
import mysql.connector
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QFrame, QPushButton, QGroupBox, QVBoxLayout, QAction, \
    QGridLayout, QLineEdit, QLabel, QMessageBox, QPlainTextEdit, QRadioButton
from PyQt5.QtGui import QIcon, QPixmap , QFont
from PyQt5.QtCore import pyqtSlot
from subprocess import call
#database connection        
conn = mysql.connector.connect(host="localhost", user="root", passwd="", database="mini")
mycu = conn.cursor()


class App(QMainWindow):
    def __init__(self,a):

        super().__init__()
        self.title = 'Settings'
        self.left = 100
        self.top = 100
        self.width = 500
        self.height = 600
        self.a=a
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
        
        #create label
        self.lname = QLabel('Name', self)
        self.lname.move(50,100)
        
        self.lgen= QLabel('Gender', self)
        self.lgen.move(50,150)
        
        self.ladd= QLabel('Address', self)
        self.ladd.move(50,230)
        
        self.luser= QLabel('Username', self)
        self.luser.move(50,350)
        
        
        username=self.a
        mycu.execute('SELECT *  FROM reg where username = "'+username+'"')
        res = mycu.fetchall()
        for x in res:
            global n
            n = x[0]
            global ge
            ge = x[1]
            global ad
            ad = x[2]
            global un
            un = x[3]
        

        
        # Create textbox
        self.name = QLabel(self)
        self.name.move(150, 100)
        self.name.resize(200,25)
        self.name.setText(n)
        
        self.gender = QLabel(self)
        self.gender.move(150, 150)
        self.gender.setText(ge)
        
        self.address = QLabel(self)
        self.address.move(150, 200)
        self.address.resize(200,90)
        self.address.setText(ad)

        self.user = QLabel(self)
        self.user.move(150, 350)
        self.user.resize(200,25)
        self.user.setText(un)
        
        
        self.lname.setFont(QFont('SansSerif', 15))
        self.lgen.setFont(QFont('SansSerif', 15))
        self.ladd.setFont(QFont('SansSerif', 15))
        self.luser.setFont(QFont('SansSerif', 15))
        self.name.setFont(QFont('SansSerif', 15))
        self.gender.setFont(QFont('SansSerif', 15))
        self.address.setFont(QFont('SansSerif', 15))
        self.user.setFont(QFont('SansSerif', 15))
        

         
        # Create a button in the window
        
        self.reg = QPushButton('Update', self)
        self.reg.move(50, 400)
        self.reg.clicked.connect(self.on_click1)

        
        self.lo=QPushButton("Main page",self)
        self.lo.move(250,400)
        self.lo.clicked.connect(self.log)
        self.show()
        


    def on_click1(self):
        self.Reply = QMessageBox.question(self,"Update","Address and password can be updated",  QMessageBox.Yes)
        if self.Reply == QMessageBox.Yes:
            from update import App
            self.m= App(self.a)
            self.m.show()
            self.close()

    def log(self):
        from main import App
        self.m=App(self.a)
        self.m.show()
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
