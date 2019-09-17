import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QMainWindow
from PyQt5.QtGui import QIcon, QPixmap, QPainter
from PyQt5.QtCore import Qt
 
class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Log_in '
        self.left = 100
        self.top = 100
        self.width = 640
        self.height = 480
        self.initUI()
     
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        
        # Set window background color
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.green)
        self.setPalette(p)



     
        label = QLabel('Python', self)
        label.move(50,50)

        label2 = QLabel('PyQt5', self)
        label2.move(50,100)

        label3 = QLabel('Examples', self)
        label3.move(50,150)

        label4 = QLabel('pytonspot.com', self)
        label4.move(50,200)



        
        self.show()   
     
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
