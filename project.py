import sys
from PyQt5 import QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.Qt import qSetFieldWidth, QImage
import mysql.connector
import math
from datetime import date
conn = mysql.connector.connect(host="localhost", user="root", passwd="", database="project")
mycu = conn.cursor()
currentuser = ''
currentname = ''
currentbranch = ''
currentsem = ''
currentcriteria = 0
currentsubject=''
#******************HOMEPAGE************#
class HomeWindow(QDialog):
    def __init__(self):
        super(HomeWindow, self).__init__()

        self.header = QLabel('<h1>Attendance Manager</h1>', self)
        self.title = 'Attendance Manager Home'
        self.setWindowTitle(self.title)
        self.header.setAlignment(Qt.AlignCenter)
        self.header.setFont(QtGui.QFont('Times New Roman', 11))
        self.logbut = QPushButton('Login', self)
        self.logbut.setFont(QtGui.QFont('Berlin Sans FB', 12))
        self.logbut.setFixedHeight(40)
        self.logbut.setFixedWidth(100)
        self.logbut.clicked.connect(self.onClickl)
        self.regbut = QPushButton('Register', self)
        self.regbut.setFixedHeight(40)
        self.regbut.setFixedWidth(100)
        self.regbut.setFont(QtGui.QFont('Berlin Sans FB', 12))
        self.regbut.clicked.connect(self.onClickr)
        self.setGeometry(400, 200, 500, 300);
        self.horlayout()

    def onClickl(self):
        self.sw = LoginWindow()
        self.close()
        self.sw.show()

    def onClickr(self):
        self.sw = RegisterWindow()
        self.close()
        self.sw.show()

    def horlayout(self):
        grid = QGridLayout()
        grid.addWidget(self.header, 0, 0, 1, 3)
        grid.addWidget(self.logbut, 1, 0, 1, 1)
        grid.addWidget(self.regbut, 1, 2, 1, 1)
        grid.setAlignment(Qt.AlignHCenter)
        self.setLayout(grid)

#******************LOGINPAGE************#
class LoginWindow(QDialog):
    def __init__(self):
        super(LoginWindow, self).__init__()
        self.title = 'LOGIN PAGE'
        self.setWindowTitle(self.title)
        self.setGeometry(400, 200, 500, 300);
        self.lname = QLabel('USERNAME : ', self)
        self.lpass = QLabel('PASSWORD : ', self)
        self.ename = QLineEdit(self)
        self.epass = QLineEdit(self)
        self.epass.setEchoMode(QLineEdit.Password)
        self.sub = QPushButton('Submit', self)
        self.sub.setFont(QtGui.QFont('Arial', 12))
        self.sub.clicked.connect(self.gotowelcome)
        self.sub.setFixedHeight(30)
        self.ename.setFixedHeight(30)
        self.epass.setFixedHeight(30)
        self.lname.setFont(QtGui.QFont('Times New Roman', 11))
        self.lpass.setFont(QtGui.QFont('Times New Roman', 11))
        self.res = QPushButton('Reset', self)
        self.res.clicked.connect(self.resetform)
        self.res.setFont(QtGui.QFont('Berlin Sans FB', 12))
        self.res.setFixedHeight(30)
        self.can = QPushButton('Cancel', self)
        self.can.setFont(QtGui.QFont('Arial', 12))
        self.can.clicked.connect(self.cancel)
        self.can.setFixedHeight(30)
        self.sub.setFixedWidth(100)
        self.res.setFixedWidth(100)
        self.can.setFixedWidth(100)
        self.horlayout()

    def gotowelcome(self):
        username = self.ename.text()
        passw = self.epass.text()
        mycu.execute('SELECT * FROM studdetails WHERE username = "'+username+'" AND password = "'+passw+'"')
        res = mycu.fetchone()
        if(not res):
            QMessageBox.about(self, 'Login', 'Invalid Details!!')
            self.resetform()
        else:
            self.sw = WelcomeWindow()
            self.close()
            self.sw.show()
            mycu.execute('SELECT *  FROM studdetails where username = "'+username+'"')
            res = mycu.fetchall()
            for x in res:
                global currentuser
                currentuser = x[1]
                global currentname
                currentname = x[3]
                global currentbranch
                currentbranch = x[4]
                global currentsem
                currentsem = x[5]
                global currentcriteria
                currentcriteria = x[6]
            self.sw.l1.setText("<h2>Welcome %s</h2>" % currentname)

    def resetform(self):
        self.ename.setText('')
        self.epass.setText('')

    def cancel(self):
        self.sw = HomeWindow()
        self.close()
        self.sw.show()

    def horlayout(self):
        grid = QGridLayout()
        grid.addWidget(self.lname, 0, 0, 1, 1)
        grid.addWidget(self.lpass, 1, 0, 1, 1)
        grid.addWidget(self.ename, 0, 1, 1, 2)
        grid.addWidget(self.epass, 1, 1, 1, 2)
        grid.addWidget(self.sub, 2, 0, 1, 1)
        grid.addWidget(self.res, 2, 1, 1, 1)
        grid.addWidget(self.can, 2, 2, 1, 1)
        self.setLayout(grid)

#******************REGISTERPAGE************#

class RegisterWindow(QDialog):
    def __init__(self):
        super(RegisterWindow, self).__init__()
        self.l1=QLabel("Full Name               :",self)

        self.l2=QLabel("Username                 :",self)

        self.l3=QLabel("Password                 :",self)

        self.l4=QLabel("Retype Password     :",self)

        self.l6=QLabel("Branch                       :",self)

        self.l7=QLabel("Sem                           :",self)

        self.setGeometry(400, 200, 500, 300);
        self.l1.setFont(QtGui.QFont('Times New Roman', 11))
        self.l2.setFont(QtGui.QFont('Times New Roman', 11))
        self.l3.setFont(QtGui.QFont('Times New Roman', 11))
        self.l4.setFont(QtGui.QFont('Times New Roman', 11))
        self.l6.setFont(QtGui.QFont('Times New Roman', 11))
        self.l7.setFont(QtGui.QFont('Times New Roman', 11))
        self.nametext=QLineEdit(self)
        self.nametext.setFixedHeight(30)
        self.usertext=QLineEdit(self)
        self.usertext.setFixedHeight(30)
        self.pwdtext=QLineEdit(self)
        self.pwdtext.setFixedHeight(30)
        self.rpwdtext=QLineEdit(self)
        self.rpwdtext.setFixedHeight(30)
        self.reg=QPushButton("Submit",self)
        self.reg.setFixedWidth(130)
        self.reg.clicked.connect(self.gotologin)
        self.reg.setFont(QtGui.QFont('Arial', 10))
        self.clear=QPushButton("Clear",self)
        self.clear.setFixedWidth(130)
        self.clear.clicked.connect(self.clearall)
        self.clear.setFont(QtGui.QFont('Arial', 10))
        self.back=QPushButton("Back",self)
        self.back.setFixedWidth(130)
        self.back.clicked.connect(self.gotohome)
        self.back.setFont(QtGui.QFont('Arial', 10))

        self.combo = QComboBox(self)
        self.combo.addItem("IT")
        self.combo.addItem("CS")
        self.combo.addItem("EXTC")
        self.combo.activated[str].connect(self.onActivated)

        self.combo1 = QComboBox(self)
        self.combo1.addItem("I")
        self.combo1.addItem("II")
        self.combo1.addItem("III")
        self.combo1.addItem("IV")
        self.combo1.addItem("V")
        self.combo1.addItem("VI")
        self.combo1.addItem("VII")
        self.combo1.addItem("VIII")
        self.combo1.activated[str].connect(self.onActivated2)

        self.hl()
    def gotologin(self):
        self.checkblank()
    def checkblank(self):
        nt = self.nametext.text()
        ut = self.usertext.text()
        pt = self.pwdtext.text()
        rt = self.rpwdtext.text()
        bran = self.combo.currentText()
        seme = self.combo1.currentText()
        if(nt=='' or ut=='' or pt=='' or rt==''):
            QMessageBox.about(self, 'Register', 'Some fields are still incomplete!')
        else:
            if(pt != rt):
                QMessageBox.about(self, 'Register', 'Password fields do not match')
            else:
                mycu.execute("SELECT username FROM studdetails")
                res = mycu.fetchall()
                if(ut in str(res)):
                    QMessageBox.about(self, 'Register', 'Account already Exists!')
                else:
                    print(ut)
                    mycu.execute( "CREATE TABLE "+ut+" (id INTEGER PRIMARY KEY, subject VARCHAR(40), date DATE, present INTEGER, absent INTEGER)")
                    conn.commit()
                    que = "INSERT INTO studdetails (username, password, fname, branch, sem, criteria) VALUES (%s, %s, %s, %s, %s, 75)"
                    vala = (ut, pt, nt, bran, seme)
                    mycu.execute(que, vala)
                    conn.commit()
                    QMessageBox.information(self, 'Register', 'Registeration Successful!!')
                    self.sw = HomeWindow()
                    self.close()
                    self.sw.show()


    def hl(self):
        hbl=QGridLayout()
        hbl.addWidget(self.l1,0,0)
        hbl.addWidget(self.l2,1,0)
        hbl.addWidget(self.l3,2,0)
        hbl.addWidget(self.l4,3,0)
        hbl.addWidget(self.l6,4,0)
        hbl.addWidget(self.l7,5,0)

        hbl.addWidget(self.nametext,0,1,1,2)
        hbl.addWidget(self.usertext,1,1,1,2)
        hbl.addWidget(self.pwdtext,2,1,1,2)
        hbl.addWidget(self.rpwdtext,3,1,1,2)

        hbl.addWidget(self.combo,4,1)
        hbl.addWidget(self.combo1,5,1)

        hbl.addWidget(self.reg,6,2)
        hbl.addWidget(self.clear,6,1)
        hbl.addWidget(self.back, 6, 0)
        self.setLayout(hbl)

    def onActivated(self, text):
        self.branch = text

    def onActivated2(self,text2):
        self.sem = text2

    def clearall(self):
        self.nametext.setText('')
        self.usertext.setText('')
        self.pwdtext.setText('')
        self.rpwdtext.setText('')

    def gotohome(self):
        self.sw = HomeWindow()
        self.close()
        self.sw.show()

     #   ---------------------------WELCOME-----------------------

class WelcomeWindow(QDialog):
    def __init__(self):
        super(WelcomeWindow, self).__init__()
        self.setGeometry(400, 200,500,300)
        self.l1=QLabel(self)
        self.l1.setFixedHeight(30)
        self.lout=QPushButton("Logout",self)
        self.lout.setFixedHeight(30)
        self.sa=QPushButton("Submit Daily Attendance",self)
        self.sa.clicked.connect(self.gotosubmit)
        self.sa.setFixedHeight(30)
        self.see=QPushButton("See your attendance",self)
        self.see.clicked.connect(self.gotosee)
        self.see.setFixedHeight(30)
        self.cri=QPushButton("Criteria",self)
        self.cri.clicked.connect(self.gotocri)
        self.cri.setFixedHeight(30)
        self.reset=QPushButton("Reset",self)
        self.reset.setFixedHeight(30)
        self.reset.clicked.connect(self.resetdata)
        self.log=QPushButton("Log",self)
        self.log.setFixedHeight(30)
        self.lout.clicked.connect(self.gotohome)
        self.log.clicked.connect(self.gotolog)
        self.lout.setFont(QtGui.QFont('Arial', 10))
        self.sa.setFont(QtGui.QFont('Arial', 10))
        self.see.setFont(QtGui.QFont('Arial', 10))
        self.cri.setFont(QtGui.QFont('Arial', 10))
        self.log.setFont(QtGui.QFont('Arial', 10))
        self.reset.setFont(QtGui.QFont('Arial', 10))
        self.hl()
    def gotohome(self):
        self.sw = HomeWindow()
        self.close()
        self.sw.show()

    def resetdata(self):
        butrep = QMessageBox.question(self, 'Reset', 'This will reset all your data.\n Are you sure you want to continue', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if(butrep == QMessageBox.Yes):
            mycu.execute("TRUNCATE TABLE "+currentuser+"")
            conn.commit()
            print('done')
        else:
            pass

    def gotosubmit(self):
        self.sw = SubmitWindow()
        self.close()
        self.sw.show()
        mycu.execute("SELECT subject FROM branchwise WHERE branch = %s AND sem = %s", (currentbranch, currentsem))
        res = mycu.fetchall()
        for x in res:
            self.sw.combo.addItem(x[0])

    def gotocri(self):
        self.sw = CriteriaWindow()
        self.close()
        self.sw.show()

    def gotosee(self):
        self.sw = SeeattendanceWindow()
        self.close()
        self.sw.show()
        mycu.execute("SELECT subject FROM branchwise WHERE branch = %s AND sem = %s", (currentbranch, currentsem))
        res = mycu.fetchall()
        j = 1
        for x in res:
            self.sw.ltable.setItem( j, 0, QTableWidgetItem(x[0]))
            cuval = x[0]
            mycu.execute("SELECT * FROM {} WHERE subject = '{}'".format(currentuser, cuval))
            res = mycu.fetchall()
            self.sw.ltable.setItem( j, 3, QTableWidgetItem(str(mycu.rowcount)))
            to = mycu.rowcount
            mycu.execute("SELECT present FROM {} WHERE subject = '{}' AND present = 1".format(currentuser, cuval))
            res = mycu.fetchall()
            self.sw.ltable.setItem( j, 1, QTableWidgetItem(str(mycu.rowcount)))
            po = mycu.rowcount
            ao = to-po
            self.sw.ltable.setItem( j, 2, QTableWidgetItem(str(ao)))
            per = round(float(po/to)*100, 2)
            self.sw.ltable.setItem( j, 4, QTableWidgetItem(str(per)))
            j = j+1

    def gotolog(self):
        self.sw = LogWindow()
        self.close()
        self.sw.show()

    def hl(self):
        hbl=QGridLayout()
        hbl.addWidget(self.l1,0,0,1,2)
        hbl.addWidget(self.lout,0,2,1,1)
        hbl.addWidget(self.sa,2,0,1,3)
        hbl.addWidget(self.see,3,0,1,3)
        hbl.addWidget(self.cri,1,0,1,2)
        hbl.addWidget(self.reset,4,0,1,1)
        hbl.addWidget(self.log,4,2,1,1)
        self.setLayout(hbl)

#-----------------------criteria----------------------------
class CriteriaWindow(QDialog):
    def __init__(self):
        super(CriteriaWindow, self).__init__()
        self.setGeometry(400, 200,500,300)
        self.l1=QLabel("<h2>SELECT LOWER LIMIT        :</h2>",self)
        self.l1.setFixedHeight(30)
        self.l1.setFont(QtGui.QFont('Times New Roman', 10))
        self.slider=QSlider(Qt.Horizontal)
        self.slider.setFixedHeight(30)
        self.slider.setFocusPolicy(Qt.StrongFocus)
        self.slider.setTickPosition(QSlider.TicksAbove)
        self.slider.setTickInterval(10)
        self.slider.setSingleStep(5)
        self.slider.setRange(0,100)
        self.spin=QSpinBox(self)
        self.spin.setRange(0,100)
        self.spin.valueChanged.connect(self.valchange)
        self.back=QPushButton("Back",self)
        self.back.setFixedHeight(30)
        self.back.setFixedWidth(75)
        self.back.setFont(QtGui.QFont('Arial', 10))
        self.back.clicked.connect(self.gotoback)
        self.slider.valueChanged.connect(self.change)
        self.subbut = QPushButton('Submit', self)
        self.subbut.setFixedHeight(30)
        self.subbut.setFixedWidth(75)
        self.subbut.setFont(QtGui.QFont('Arial', 10))
        self.subbut.clicked.connect(self.submitvalue)
        self.hl()
    def gotoback(self):
        self.sw = WelcomeWindow()
        self.close()
        self.sw.show()
        self.sw.l1.setText("<h2>Welcome %s</h2>" % currentname)

    def hl(self):
        hbl=QGridLayout()
        hbl.addWidget(self.back,0,0,1,1)
        hbl.addWidget(self.subbut,0,1,1,1)
        hbl.addWidget(self.l1,1,0,1,1)
        hbl.addWidget(self.slider,2,0,1,2)
        hbl.addWidget(self.spin,1,1,1,1)
        self.setLayout(hbl)

    def change(self):
        val=int(self.slider.value())
        self.spin.setValue(val)

    def valchange(self):
        val = int(self.spin.value())
        self.slider.setValue(val)

    def submitvalue(self):
        subval = self.spin.value()
        mycu.execute("UPDATE studdetails SET criteria = %s WHERE username = %s", (subval, currentuser))
        conn.commit()
        QMessageBox.about(self, 'Criteria', 'Criteria updated!')

#--------------------------SUBMIT----------------------------------------------
class SubmitWindow(QDialog):
    def __init__(self):
        super(SubmitWindow, self).__init__()
        self.setGeometry(400, 200,500,300)
        self.sub=QLabel("               SUBJECT       : ",self)
        self.sub.setFont(QtGui.QFont('Times New Roman', 13))
        self.attend=QPushButton("ATTEND",self)
        self.attend.setFixedHeight(30)
        self.attend.setFixedWidth(230)
        self.attend.clicked.connect(self.addattendance)
        self.missed=QPushButton("MISSED",self)
        self.missed.setFixedHeight(30)
        self.missed.clicked.connect(self.addabsent)
        self.group = QGroupBox('Lectures', self)
        self.group.setFont(QtGui.QFont('Times New Roman', 10))
        self.total=QLabel("Total",self)
        self.totalval=QLabel("-",self)
        self.atten=QLabel("Attended",self)
        self.attenval=QLabel("-",self)
        self.miss=QLabel("Missed",self)
        self.missval=QLabel("-",self)
        self.back=QPushButton("Back",self)
        self.back.setFixedWidth(75)
        self.back.clicked.connect(self.gotowel)
        self.attend.setFont(QtGui.QFont('Arial', 10))
        self.missed.setFont(QtGui.QFont('Arial', 10))
        self.back.setFont(QtGui.QFont('Arial', 10))

        self.ad=QLabel("<h4>ATTENDANCE</h4>",self)
        self.bl=QLabel(self)
        self.bl.setFont(QtGui.QFont('Arial', 16))
        self.bel=QLabel(self)

        self.combo = QComboBox(self)
        self.combo.setFixedHeight(30)
        self.combo.currentTextChanged.connect(self.checksubject)

        self.hl()
    def gotowel(self):
        self.sw = WelcomeWindow()
        self.close()
        self.sw.show()
        self.sw.l1.setText('<h2>Welcome %s</h2>' % currentname)

    def addattendance(self):
        que = "INSERT INTO "+currentuser+" (subject, date, present, absent) VALUES (%s, %s, %s, %s)"
        now = QDate.currentDate().toPyDate()
        print(now)
        vala = (currentsubject, now, 1, 0)
        mycu.execute(que, vala)
        conn.commit()
        self.checksubject()

    def addabsent(self):
        que = "INSERT INTO "+currentuser+" (subject, date, present, absent) VALUES (%s, %s, %s, %s)"
        now = QDate.currentDate().toPyDate()
        print(now)
        vala = (currentsubject, now, 0, 1)
        mycu.execute(que, vala)
        conn.commit()
        self.checksubject()

    def checksubject(self):
        global currentsubject
        currentsubject = self.combo.currentText()
        print(currentuser)
        mycu.execute("SELECT criteria FROM studdetails WHERE username = '"+currentuser+"'")
        res = mycu.fetchall()
        for x in res:
            currentcriteria = x[0]
        mycu.execute("SELECT * FROM "+currentuser+" WHERE subject = '"+currentsubject+"'")
        res = mycu.fetchall()
        tot = mycu.rowcount
        c = 0
        for x in res:
            if(x[3] == 1):
                c = c+1
        abs = tot-c
        self.totalval.setText(str(tot))
        self.attenval.setText(str(c))
        self.missval.setText(str(abs))
        if(tot!=0):
            percent = float(c/tot)*100
        else:
            percent = 0
        if(percent < float(currentcriteria)):
            tempc = c
            if(tot == 0):
                tempc = 0
            else:
                temptot = tot
                while(100*(float(tempc/temptot))<float(currentcriteria)):
                    tempc = tempc + 1
                    temptot = temptot + 1
            self.bel.setText('NOTE : Your attendance is below {} % \n You need to sit {} more lectures to coverup'.format(currentcriteria, math.ceil(tempc-c)))
        else:
            self.bel.setText('')
        self.bl.setText(str(round(percent, 2))+'%')

    def hl(self):
        hbox = QGridLayout()
        hbox.addWidget(self.total, 0, 0, 1, 1)
        hbox.addWidget(self.totalval, 1, 0, 1, 1)
        hbox.addWidget(self.atten, 0, 1, 1, 1)
        hbox.addWidget(self.attenval, 1, 1, 1, 1)
        hbox.addWidget(self.miss, 0, 2, 1, 1)
        hbox.addWidget(self.missval, 1, 2, 1, 1)
        hbox.addWidget(self.ad, 2, 0, 1, 1)
        hbox.addWidget(self.bl, 3, 0, 1, 1)
        hbox.addWidget(self.bel, 4, 0, 1, 1)
        self.group.setLayout(hbox)
        hbl=QGridLayout()
        hbl.addWidget(self.sub,0,0,1,1)
        hbl.addWidget(self.attend,1,0,1,1)
        hbl.addWidget(self.missed,1,1,1,1)
        hbl.addWidget(self.group,2,0,3,2)
        hbl.addWidget(self.combo,0,1,1,1)
        hbl.addWidget(self.back, 5, 0, 1, 1)


        self.setLayout(hbl)

   # ------------------------------SA-----------------------------------------
class SeeattendanceWindow(QDialog):
    def __init__(self):
        super(SeeattendanceWindow, self).__init__()
        self.setGeometry(400, 200, 540, 300)
        self.button = QPushButton('back', self)
        self.button.setFont(QtGui.QFont('Arial', 10))
        self.horlayout()
        self.show()
    def horlayout(self):
        self.ltable = QTableWidget()
        self.ltable.setRowCount(7)
        self.ltable.setColumnCount(5)
        self.ltable.setItem( 0, 0, QTableWidgetItem("Subject"))
        self.ltable.setItem( 0, 1, QTableWidgetItem("Attended Lectures"))
        self.ltable.setItem( 0, 2, QTableWidgetItem("Missed Lectures"))
        self.ltable.setItem( 0, 3, QTableWidgetItem("Total"))
        self.ltable.setItem( 0, 4, QTableWidgetItem("Percentage"))

        self.button.clicked.connect(self.gotoback)

        self.hl()

    def gotoback(self):
        self.sw = WelcomeWindow()
        self.close()
        self.sw.show()
        self.sw.l1.setText('<h2>Welcome %s</h2>' % currentname)

    def hl(self):
        grid = QGridLayout()
        grid.addWidget(self.ltable, 0, 0, 5, 5)
        grid.addWidget(self.button, 6, 0, 1, 1)
        self.setLayout(grid)

#---------------------------log---------------------------
class DateWindow(QDialog):
    def __init__(self):
        super(DateWindow, self).__init__()
        self.setGeometry(400, 200,430,230)
        self.cal=QCalendarWidget(self)
        self.enter=QPushButton("ENTER",self)
        self.enter.setFixedHeight(50)
        self.enter.setFont(QtGui.QFont('Arial', 10))
        self.group = QGroupBox('Date', self)
        self.enter.clicked.connect(self.gotolog)
        self.hl()

    def gotolog(self):
        self.sw = LogWindow()
        self.close()
        self.sw.show()
        date1 = self.cal.selectedDate().toPyDate()
        self.sw.datelabel.setText(str(date1))
        mycu.execute("SELECT * FROM shrey86 WHERE date = '{}'".format(date1))
        res = mycu.fetchall()
        self.sw.ltable.setColumnCount(mycu.rowcount)
        i = 0
        for x in res:
            self.sw.ltable.setItem(0, i, QTableWidgetItem(x[1]))
            if(x[3] == 1):
                self.sw.ltable.setItem(1, i, QTableWidgetItem('Present'))
            else:
                self.sw.ltable.setItem(1, i, QTableWidgetItem('Absent'))
            i = i+1

    def hl(self):
        hbox = QGridLayout()
        hbox.addWidget(self.cal, 0, 0, 1, 1)
        hbox.addWidget(self.enter, 0, 1, 1, 1)

        self.group.setLayout(hbox)

#---------------------------------------logwindow-------------------------------
class LogWindow(QDialog):
    def __init__(self):
        super(LogWindow, self).__init__()
        self.setGeometry(400,200,550,300)
        self.date=QPushButton("Select Date",self)
        self.back=QPushButton(" back",self)
        self.datelabel = QLabel(self)
        self.date.setFont(QtGui.QFont('Arial', 10))
        self.back.setFont(QtGui.QFont('Arial', 10))
        self.date.setFixedWidth(150)
        self.horlayout()
    def horlayout(self):
        self.ltable = QTableWidget()
        self.ltable.setRowCount(2)
        self.back.clicked.connect(self.gotoback)

        self.hl()
        self.date.clicked.connect(self.gotodate)

    def gotodate(self):
        self.sw = DateWindow()
        self.close()
        self.sw.show()

    def gotoback(self):
        self.sw = WelcomeWindow()
        self.close()
        self.sw.show()
        self.sw.l1.setText('<h2>Welcome %s</h2>' % currentname)

    def hl(self):
        grid = QGridLayout()
        grid.addWidget(self.ltable, 1, 0, 5, 5)
        grid.addWidget(self.datelabel, 0, 2, 1, 1)
        grid.addWidget(self.date, 0, 0, 1, 1)
        grid.addWidget(self.back, 0, 4, 1, 1)
        self.setLayout(grid)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MW = LoginWindow()
    MW.show()
    sys.exit(app.exec_())
