import sys
import mysql.connector
from mysql.connector import Error
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QAction, QLineEdit, QMessageBox, QComboBox, QLabel
from PyQt5.QtCore import QCoreApplication

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'WishListQt Test'
        self.left = 300
        self.top = 300
        self.width = 1000
        self.height = 300
        self.initUI()


    def initUI(self):


        # buttons
        addBtn = QPushButton('Add new wish', self)
        addBtn.clicked.connect(QCoreApplication.instance().quit)
        addBtn.resize(addBtn.sizeHint())
        addBtn.move(50, 50)

        showBtn = QPushButton('Show wishes', self)
        showBtn.clicked.connect(QCoreApplication.instance().quit)
        showBtn.resize(showBtn.sizeHint())
        showBtn.move(50, 100)

        quitBtn = QPushButton('Quit', self)
        quitBtn.clicked.connect(QCoreApplication.instance().quit)
        quitBtn.resize(quitBtn.sizeHint())
        quitBtn.move(50, 150)



        # editText fields
        nameEditText = QLineEdit('name of wish', self)
        nameEditText.resize(nameEditText.sizeHint())
        nameEditText.move(150, 50)

        priceEditText = QLineEdit('price', self)
        priceEditText.resize(priceEditText.sizeHint())
        priceEditText.move(300, 50)

        commentEditText = QLineEdit('comment', self)
        commentEditText.resize(commentEditText.sizeHint())
        commentEditText.move(450, 50)

        linkEditText = QLineEdit('link', self)
        linkEditText.resize(linkEditText.sizeHint())
        linkEditText.move(600, 50)

        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowTitle(self.title)
        self.show()
    #
    # def initDB(self):
    #
    #
    # def addToDB(self):


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())