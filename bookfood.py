import sys
import mysql.connector
from PyQt5.QtWidgets import (QMainWindow, QApplication, QWidget, QFrame, QPushButton, QGroupBox, QVBoxLayout, QAction,
    QGridLayout, QLineEdit, QLabel, QMessageBox, QPlainTextEdit, QRadioButton , QGridLayout, QTableWidget, QTableWidgetItem,
    QTextEdit)
from PyQt5.QtGui import QIcon, QPixmap, QFont, QTextCursor
from PyQt5.QtCore import pyqtSlot
from subprocess import call

class App(QMainWindow):
    def __init__(self,a):
        super().__init__()
        self.title = 'Book Food'
        self.left = 100
        self.top = 100
        self.width = 600
        self.height = 500
        self.a=a
        self.initUI()
        

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        #database connection        
        conn = mysql.connector.connect(host="localhost", user="root", passwd="", database="mini")
        mycu = conn.cursor()

        self.lh = QLabel(self)
        self.lh.move(0, 0)
        self.lh.resize(600, 200)
        self.head = QPixmap('head.png')
        self.lh.setPixmap(self.head)
        self.lh.resize(self.head.width(), self.head.height())
        
        self.l1=QLabel("Foods",self)
        self.l1.move(10,160)
        
        self.l2=QLabel("Hotels",self)
        self.l2.move(210,160)
        
        self.l3=QLabel("Rupees₹",self)
        self.l3.move(350,160)
        
        self.l1.setFont(QFont('SansSerif', 15))
        self.l2.setFont(QFont('SansSerif', 15))
        self.l3.setFont(QFont('SansSerif', 15))
        
        self.link1 = QPushButton('MAIN PAGE', self)
        self.link1.move(0,70)
        self.link1.resize(200, 60)
        self.link1.clicked.connect(self.on_click1)
        
        self.link2= QPushButton('Book Food', self)
        self.link2.move(200, 70)
        self.link2.resize(200, 60)
        
        self.link2= QPushButton('Settings', self)
        self.link2.move(400, 70)
        self.link2.resize(200, 60)
        self.link2.clicked.connect(self.on_click2)

        self.f=QTextEdit(self)
        self.f.resize(100,200)
        self.f.move(10,200)
        
        self.h=QTextEdit(self)
        self.h.resize(100,200)
        self.h.move(210,200)
        
        self.p=QTextEdit(self)
        self.p.resize(100,200)
        self.p.move(350,200)
        
        self.amn1=QLabel("The Final Amount is :",self)
        self.amn1.resize(150,50)
        self.amn1.move(200,400)
        
        self.amn=QLabel(self)
        self.amn.move(400,410)
        
        self.amn.setFont(QFont('SansSerif', 15))
        self.amn1.setFont(QFont('SansSerif', 10))
        
        mycu.execute("SELECT * FROM "+self.a+"")
        res = mycu.fetchall()
           
        for row in res:
            self.c=QTextCursor(self.f.document())
            self.c.insertText(str(row[0] +"\n"))  
        for row in res:
            self.c=QTextCursor(self.h.document())
            self.c.insertText(str(row[1] +"\n")) 
            
        self.am=0
        for row in res:
            self.c=QTextCursor(self.p.document())
            self.c.insertText((str(row[2]) +"\n"))  
        for row in res:
            self.am=int(self.am)+int(row[2])
            
        self.amn.setText(str(self.am))
        
        
        
         
         # Create a button in the window

        self.reg = QPushButton('Book', self)
        self.reg.move(100, 450)
        self.reg.clicked.connect(self.on_click3)
        
        
        self.show()
        
    def on_click1(self):
        from main import App
        self.m=App(self.a)
        self.m.show()
        self.close()

    def on_click2(self):
        from setting import App
        self.m=App(self.a)
        self.m.show()
        self.close()
    
    def on_click3(self):
        #database connection        
        conn = mysql.connector.connect(host="localhost", user="root", passwd="", database="mini")
        mycu = conn.cursor()
        mycu.execute("TRUNCATE "+self.a+"")
        QMessageBox.question(self, 'Food', 'Foods Booked')
        from main import App
        self.m=App(self.a)
        self.m.show()
        self.close()
        
        
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())