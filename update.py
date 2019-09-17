import sys
import mysql.connector
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QFrame, QPushButton, QGroupBox, QVBoxLayout, QAction, \
    QGridLayout, QLineEdit, QLabel, QMessageBox, QPlainTextEdit, QRadioButton
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtCore import pyqtSlot
from subprocess import call
#database connection        
conn = mysql.connector.connect(host="localhost", user="root", passwd="", database="mini")
mycu = conn.cursor()


class App(QMainWindow):

    def __init__(self,a):
        super().__init__()
        self.title = 'Update'
        self.left = 100
        self.top = 100
        self.width = 600
        self.height = 500
        self.a=a
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # head image
        self.lh = QLabel(self)
        self.lh.move(0, 0)
        self.lh.resize(600, 200)
        self.head = QPixmap('head.png')
        self.lh.setPixmap(self.head)
        self.lh.resize(self.head.width(), self.head.height())

        self.ladd = QLabel('Address', self)
        self.ladd.move(50, 100)

        self.lpwd = QLabel('Password', self)
        self.lpwd.move(50, 200)

        self.lpwd = QLabel('Re-Enter Password', self)
        self.lpwd.move(50, 250)

        # Create textbox

        self.address = QLineEdit(self)
        self.address.move(150, 100)
        self.address.resize(200, 90)

        self.pwd = QLineEdit(self)
        self.pwd.move(150, 200)
        self.pwd.resize(200, 25)

        self.pwd1 = QLineEdit(self)
        self.pwd1.move(150, 250)
        self.pwd1.resize(200, 30)

        # Create a button in the window

        self.reg = QPushButton('Update', self)
        self.reg.move(50, 300)
        self.reg.clicked.connect(self.on_click)
        self.show()

        self.reg = QPushButton('Back', self)
        self.reg.move(100, 300)
        self.reg.clicked.connect(self.on_click1)
        self.show()


    def on_click(self):
        pwd1=self.pwd1.text()
        add=self.address.text()
        pwd=self.pwd.text()
        user=self.a
        if(add=='' or pwd=='' or pwd1==''):
            QMessageBox.about(self, 'Update', 'Some fields are still incomplete!')
        else:
            if(pwd!=pwd1):
                QMessageBox.about(self, "Password", "Password Doesn't Match")
            else:
                mycu.execute('SELECT password FROM reg WHERE username= "'+user+'"')
                res = mycu.fetchone()
                if(res == pwd):
                    QMessageBox.about(self, 'Update', 'Enter the new Password!', QMessageBox.Yes)
                else:
                    mycu.execute('UPDATE  reg  SET address = "'+add+'", password = "'+pwd+'" WHERE username= "'+user+'"')
                    conn.commit()
                    print('Updated Successfully')
                    self.Reply = QMessageBox.question(self,"Update"," Update successfull", QMessageBox.Yes)
                    if self.Reply == QMessageBox.Yes:
                        from main import App
                        self.m=App(self.a)
                        self.m.show()
                        self.close()
                        
    def on_click1(self):
        from setting import App
        self.m=App(self.a)
        self.m.show()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())