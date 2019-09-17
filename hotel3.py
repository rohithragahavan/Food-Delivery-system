import sys
import mysql.connector
from subprocess import call
from PyQt5.QtWidgets import QMainWindow, QFrame, QApplication, QWidget, QPushButton, QAction, QLineEdit, QLabel, QMessageBox
from PyQt5.QtGui import QIcon, QPixmap , QFont
from PyQt5.QtCore import pyqtSlot, Qt , QDate
import datetime
#database connection        
conn = mysql.connector.connect(host="localhost", user="root", passwd="", database="mini")
mycu = conn.cursor()

class App(QMainWindow):
 
    def __init__(self,a):
        super().__init__()
        self.title = 'Dominos'
        self.left = 100
        self.top = 100
        self.width = 600
        self.height = 300
        self.a =a 
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.green)
        self.setPalette(p)
        
        #head image      
        self.lh=QLabel(self)
        self.lh.move(0, 0)
        self.lh.resize(600, 200)
        self.head = QPixmap('head.png')
        self.lh.setPixmap(self.head)
        self.lh.resize(self.head.width(),self.head.height())
        
        self.back=QPushButton("Back",self)
        self.back.move(550,20)
        self.back.resize(40, 20)
        self.back.clicked.connect(self.backclick)    
        
        #main page
        #h1
        self.frame1 = QFrame(self)
        self.frame1.setStyleSheet("color: rgb(0,0,255)")
        self.frame1.move(0,75 )
        self.frame1.resize(299, 110)
        self.frame1.setAutoFillBackground(True)
        self.frame1.setStyleSheet("QWidget {background-color: Qcolor(0,0,255) } ") 
        
        self.i1=QLabel(self.frame1)
        self.i1.move(0,0)
        self.i1.resize(299, 110)
        self.i1.setPixmap(QPixmap('p1.jpg'))
        self.i1.resize(self.i1.width(),self.i1.height())
        
        self.h1=QLabel("Small Pizza    ₹99",self.frame1)
        self.h1.setFont(QFont('SansSerif', 20))
        self.h1.setStyleSheet("QLabel {background-color: rgba(255, 255, 255, 10); color :yellow ;}")
        self.h1.move(15, 65)
        self.h1.resize(300, 50)
        
        self.s1=QPushButton("Select",self.frame1)
        self.s1.move(260, 5)
        self.s1.resize(38, 16)
        self.s1.setFont(QFont('SansSerif', 10))
        self.s1.setStyleSheet("border:1px solid lightblue; ")
        self.s1.clicked.connect(self.hotel1)
        
        #h2
        self.frame2 = QFrame(self)
        self.frame2.setStyleSheet("color: rgb(0,0,255)")
        self.frame2.move(300,75 )
        self.frame2.resize(300, 110)
        self.frame2.setAutoFillBackground(True)
        self.frame2.setStyleSheet("QWidget {background-color: Qcolor(0,0,255)}")
         
        self.i2=QLabel(self.frame2)
        self.i2.move(0,0)
        self.i2.resize(300, 110)
        self.i2.setPixmap(QPixmap('p2.jpg'))
        self.i2.resize(self.i1.width(),self.i1.height())
        
        self.h2=QLabel("Medium Pizza    ₹190",self.frame2)
        self.h2.setFont(QFont('SansSerif', 20))
        self.h2.setStyleSheet("QLabel {background-color: rgba(255, 255, 255, 10); color :yellow ;}")
        self.h2.move(15, 65)
        self.h2.resize(300, 50)
        
        self.s2=QPushButton("Select",self.frame2)
        self.s2.move(260, 5)
        self.s2.resize(38, 16)
        self.s2.setFont(QFont('SansSerif', 10))
        self.s2.setStyleSheet("border:1px solid lightblue; ")
        self.s2.clicked.connect(self.hotel2)
        
        #h3
        self.frame3 = QFrame(self)
        self.frame3.setStyleSheet("color: rgb(0,0,255)")
        self.frame3.move(0,186 )
        self.frame3.resize(299, 110)
        self.frame3.setAutoFillBackground(True)
        self.frame3.setStyleSheet("QWidget {background-color: Qcolor(0,0,255)}") 
        
        self.i3=QLabel(self.frame3)
        self.i3.move(0,0)
        self.i3.resize(300, 110)
        self.i3.setPixmap(QPixmap('p3.jpg'))
        self.i3.resize(self.i1.width(),self.i1.height())
        
        self.h3=QLabel("Large Pizza    ₹300",self.frame3)
        self.h3.setFont(QFont('SansSerif', 20))
        self.h3.setStyleSheet("QLabel {background-color: rgba(255, 255, 255, 10); color :yellow ;}")
        self.h3.move(15, 65)
        self.h3.resize(300, 50)
        
        self.s3=QPushButton("Select",self.frame3)
        self.s3.move(260, 5)
        self.s3.resize(38, 16)
        self.s3.setFont(QFont('SansSerif', 10))
        self.s3.setStyleSheet("border:1px solid lightblue; ")
        self.s3.clicked.connect(self.hotel3)
        
        #h4
        self.frame4 = QFrame(self)
        self.frame4.setStyleSheet("color: rgb(0,0,255)")
        self.frame4.move(300,186 )
        self.frame4.resize(299, 110)
        self.frame4.setAutoFillBackground(True)
        self.frame4.setStyleSheet("QWidget {background-color: Qcolor(0,0,255)}") 
        
        self.i4=QLabel(self.frame4)
        self.i4.move(0,0)
        self.i4.resize(300, 110)
        self.i4.setPixmap(QPixmap('p4.jpg'))
        self.i4.resize(self.i1.width(),self.i1.height())
        
        self.h4=QLabel("Cold Drinks    ₹50",self.frame4)
        self.h4.setFont(QFont('SansSerif', 20))
        self.h4.setStyleSheet("QLabel {background-color: rgba(255, 255, 255, 10); color :yellow ;}")
        self.h4.move(15, 65)
        self.h4.resize(300, 50)
        
        self.s4=QPushButton("Select",self.frame4)
        self.s4.move(260, 5)
        self.s4.resize(38, 16)
        self.s4.setFont(QFont('SansSerif', 10))
        self.s4.setStyleSheet("border:1px solid lightblue; ")
        self.s4.clicked.connect(self.hotel4)
        
        self.show()
          
    def hotel1(self):
        c=self.a
        que = "INSERT INTO "+c+" (food, hotel, rupees, date) VALUES (%s, %s, %s, %s)"
        now = QDate.currentDate().toPyDate()
        print(now)
        vala = ('Small Pizza','Dominos','99',now)
        mycu.execute(que, vala)
        conn.commit()
        QMessageBox.question(self,'Dominos', "Food added to list")
        
    def hotel2(self):
        c=self.a
        que = "INSERT INTO "+c+" (food, hotel, rupees, date) VALUES (%s, %s, %s, %s)"
        now = QDate.currentDate().toPyDate()
        print(now)
        vala = ('Regular Pizza','Dominos','190',now)
        mycu.execute(que, vala)
        conn.commit()
        QMessageBox.question(self,'Dominos', "Food added to list")
    def hotel3(self):
        c=self.a
        que = "INSERT INTO "+c+" (food, hotel, rupees, date) VALUES (%s, %s, %s, %s)"
        now = QDate.currentDate().toPyDate()
        print(now)
        vala = ('Large Pizza','Dominos','300',now)
        mycu.execute(que, vala)
        conn.commit()
        QMessageBox.question(self,'Shivsagar hotel', "Food added to list")
    def hotel4(self):
        c=self.a
        que = "INSERT INTO "+c+" (food, hotel, rupees, date) VALUES (%s, %s, %s, %s)"
        now = QDate.currentDate().toPyDate()
        print(now)
        vala = ('Cold Drinks','Dominos','50',now)
        mycu.execute(que, vala)
        conn.commit()
        QMessageBox.question(self,'Dominos', "Food added to list") 
    def backclick(self):
        from main import App
        self.m=App(self.a)
        self.m.show()
        self.close()   

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
