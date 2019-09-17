import sys
import mysql.connector
from subprocess import call
from PyQt5.QtWidgets import QMainWindow, QFrame, QApplication, QWidget, QPushButton, QAction, QLineEdit, QLabel, QMessageBox
from PyQt5.QtGui import QIcon, QPixmap , QFont
from PyQt5.QtCore import pyqtSlot, Qt
f=[]
p=[]
h=[]
class App(QMainWindow):
 
    def __init__(self,a):
        super().__init__()
        self.title = 'Raa'
        self.left = 100
        self.top = 100
        self.width = 600
        self.height = 500
        self.a=a
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
        
        self.l1= QLabel(self)
        self.l1.move(450,10)
        self.l1.resize(200,30)
        
        # Create a link in the window
        
        self.link1 = QPushButton('MAIN PAGE', self)
        self.link1.move(0,70)
        self.link1.resize(200, 60)      
        
        self.link2= QPushButton('Book Food', self)
        self.link2.move(200, 70)
        self.link2.resize(200, 60)
        self.link2.clicked.connect(self.on_click2)
        
        self.link2= QPushButton('Settings', self)
        self.link2.move(400, 70)
        self.link2.resize(200, 60)
        self.link2.clicked.connect(self.on_click3)
        
        #main page
        #h1
        self.frame1 = QFrame(self)
        self.frame1.setStyleSheet("color: rgb(0,0,255)")
        self.frame1.move(0,130 )
        self.frame1.resize(600, 110)
        self.frame1.setAutoFillBackground(True)
        self.frame1.setStyleSheet("QWidget {background-color: Qcolor(0,0,255)}") 
        
        self.h1=QLabel("Shivsagar hotel",self.frame1)
        self.h1.setFont(QFont('SansSerif', 30))
        self.h1.move(10, 10)
        self.h1.resize(300, 50)
        
        self.s1=QPushButton("Select Food",self.frame1)
        self.s1.move(400, 20)
        self.s1.resize(180, 50)
        self.s1.setFont(QFont('SansSerif', 15))
        self.s1.setStyleSheet("border:5px solid lightblue")
        self.s1.clicked.connect(self.hotel1)
        
        #h2
        self.frame2 = QFrame(self)
        self.frame2.setStyleSheet("color: rgb(0,0,255)")
        self.frame2.move(0,250 )
        self.frame2.resize(600, 110)
        self.frame2.setAutoFillBackground(True)
        self.frame2.setStyleSheet("QWidget {background-color: Qcolor(0,0,255)}") 
        
        self.h2=QLabel("Ram Hotel",self.frame2)
        self.h2.setFont(QFont('SansSerif', 30))
        self.h2.move(10, 10)
        self.h2.resize(300, 50)
        
        self.s2=QPushButton("Select Food",self.frame2)
        self.s2.move(400, 20)
        self.s2.resize(180, 50)
        self.s2.setFont(QFont('SansSerif', 15))
        self.s2.setStyleSheet("border:5px solid lightblue")
        self.s2.clicked.connect(self.hotel2)
        
        #h3
        self.frame3 = QFrame(self)
        self.frame3.setStyleSheet("color: rgb(0,0,255)")
        self.frame3.move(0,370 )
        self.frame3.resize(600, 110)
        self.frame3.setAutoFillBackground(True)
        self.frame3.setStyleSheet("QWidget {background-color: Qcolor(0,0,255)}") 
        
        self.h3=QLabel("Dominos",self.frame3)
        self.h3.setFont(QFont('SansSerif', 30))
        self.h3.move(10, 10)
        self.h3.resize(300, 50)
        
        self.s3=QPushButton("Select Food",self.frame3)
        self.s3.move(400, 20)
        self.s3.resize(180, 50)
        self.s3.setFont(QFont('SansSerif', 15))
        self.s3.setStyleSheet("border:5px solid lightblue")
        self.s3.clicked.connect(self.hotel3)
        
        self.lo=QPushButton("Logout",self)
        self.lo.move(460,35)
        self.lo.clicked.connect(self.log)
        self.show()
        
        
              
    def on_click2(self):
        from bookfood import App
        self.m= App(self.a)
        self.m.show()
        self.close()
         
    def on_click3(self):
        from setting import App
        self.s=App(self.a)
        self.s.show()
        self.close()
            
    def hotel1(self):
        from hotel1 import App
        self.m=App(self.a)
        self.m.show()
        self.close()
    def hotel2(self):
        from hotel2 import App
        self.m=App(self.a)
        self.m.show()
        self.close()
        
    def hotel3(self):
        from hotel3 import App
        self.m=App(self.a)
        self.m.show()
        self.close()      
        
    def log(self):
        from login import App
        self.m= App()
        self.m.show()
        self.close()  

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
