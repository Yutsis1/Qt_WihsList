import sys
import mysql.connector
from mysql.connector import Error
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QMainWindow, QAction, QLineEdit, QMessageBox, QComboBox, QLabel
from PyQt5.QtCore import QCoreApplication

from DB_halper import DB_halper

class MainWindow(QMainWindow):

    def __init__(self, dbHalper):
        super().__init__()
        self.title = 'WishListQt Test'
        self.left = 300
        self.top = 300
        self.width = 1000
        self.height = 300
        self.initUI()
        self.dbhalper = dbHalper



    def initUI(self):


        # buttons
        addBtn = QPushButton('Add new wish', self)
        addBtn.clicked.connect(self.addToWishes)
        addBtn.resize(addBtn.sizeHint())
        addBtn.move(50, 50)

        showBtn = QPushButton('Show wishes', self)
        showBtn.clicked.connect(self.showWishes)
        showBtn.resize(showBtn.sizeHint())
        showBtn.move(50, 100)

        quitBtn = QPushButton('Quit', self)
        quitBtn.clicked.connect(QCoreApplication.instance().quit)
        quitBtn.resize(quitBtn.sizeHint())
        quitBtn.move(50, 150)



        # editText fields
        self.nameEditText = QLineEdit('name of wish', self)
        self.nameEditText.resize(self.nameEditText.sizeHint())
        self.nameEditText.move(150, 50)

        self.priceEditText = QLineEdit('price', self)
        self.priceEditText.resize(self.priceEditText.sizeHint())
        self.priceEditText.move(300, 50)

        self.commentEditText = QLineEdit('comment', self)
        self.commentEditText.resize(self.commentEditText.sizeHint())
        self.commentEditText.move(450, 50)

        self.linkEditText = QLineEdit('link', self)
        self.linkEditText.resize(self.linkEditText.sizeHint())
        self.linkEditText.move(600, 50)

        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowTitle(self.title)
        self.show()

    def addToWishes(self):
        name = self.nameEditText.text()
        comment = self.commentEditText.text()
        link = self.linkEditText.text()
        try:
            price = int(self.priceEditText.text())
            self.dbhalper.insert_new_to_WishList(name, price, comment, link)
        except ValueError:
            print("write number")


    def showWishes(self):
        self.wishScreen = WishWindow()
        self.wishScreen.show()
    #
    # def initDB(self):
    #
    #
    # def addToDB(self):

class WishWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'WishList'
        self.left = 300
        self.top = 300
        self.width = 1000
        self.height = 300



# custom exceptbook for hooking Qt exceprions (problem found in PyCharm)
def my_exception_hook(exctype, value, traceback):
    # Print the error and traceback
    print(exctype, value, traceback)
    # Call the normal Exception hook after
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)


if __name__ == '__main__':
    # Back up the reference to the exceptionhook
    sys._excepthook = sys.excepthook
    sys.excepthook = my_exception_hook


    dbhalper =  DB_halper()
    app = QApplication(sys.argv)
    ex = MainWindow(dbhalper)
    try:
        sys.exit(app.exec_())
    except:
        print("Exiting")