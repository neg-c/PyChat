from PyQt6.QtWidgets import (
    QApplication,
    QButtonGroup,
    QFrame,
    QLabel,
    QLayout,
    QLineEdit,
    QListView,
    QListWidgetItem,
    QMainWindow,
    QPushButton,
    QStackedLayout,
    QTextEdit,
    QVBoxLayout,
    QWidget,
    QHBoxLayout,
    QListWidget,
)


import sys


from PyQt6 import QtCore, QtGui, QtWidgets
import os

class PyClientChat(object):
    # this method creates all the widgets and updates their styles
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(742, 629)

        script_dir = os.path.dirname(os.path.abspath(__file__))
        STYLE_PATH = os.path.join(script_dir,"..\\", "res", "chat_styles.qss")

        with open( STYLE_PATH, "r") as fh:
            MainWindow.setStyleSheet(fh.read())

        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.ChatWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.ChatWidget.setGeometry(QtCore.QRect(30, 20, 451, 491))
        self.ChatWidget.setStyleSheet("background-color: rgb(195, 195, 195);")
        self.ChatWidget.setObjectName("ChatWidget")
        self.chatBox = QtWidgets.QListWidget(parent=self.ChatWidget)
        self.chatBox.setGeometry(QtCore.QRect(10, 10, 431, 471))
        self.chatBox.setStyleSheet("background-color: rgb(147, 147, 147);")
        self.chatBox.setObjectName("chatBox")

        self.OnlineListWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.OnlineListWidget.setGeometry(QtCore.QRect(510, 20, 201, 491))
        self.OnlineListWidget.setStyleSheet("background-color: rgb(195, 195, 195);")
        self.OnlineListWidget.setObjectName("OnlineListWidget")
        self.OnlineList = QtWidgets.QListWidget(parent=self.OnlineListWidget)
        self.OnlineList.setGeometry(QtCore.QRect(10, 10, 181, 471))
        self.OnlineList.setStyleSheet("background-color: rgb(147, 147, 147);")
        self.OnlineList.setObjectName("OnlineList")

        self.InputWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.InputWidget.setGeometry(QtCore.QRect(30, 530, 681, 81))
        self.InputWidget.setStyleSheet("background-color: rgb(195, 195, 195);")
        self.InputWidget.setObjectName("InputWidget")

        self.pushButton = QtWidgets.QPushButton(parent=self.InputWidget)
        self.pushButton.setGeometry(QtCore.QRect(500, 20, 141, 41))
        self.pushButton.setStyleSheet("background-color: rgb(115, 115, 115);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.sendButtonClick)

        self.lineEdit = QtWidgets.QLineEdit(parent=self.InputWidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 20, 431, 41))
        self.lineEdit.setStyleSheet(
            "background-color: rgb(234, 234, 234);color: rgb(0,0,0);"
        )
        self.lineEdit.setReadOnly(False)
        self.lineEdit.setObjectName("lineEdit")

        MainWindow.setCentralWidget(self.centralwidget)

        self.uiLoop(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def uiLoop(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Send"))

    def sendButtonClick(self):
        msg = self.lineEdit.text()
        if msg:
            self.chatBox.addItem(msg)
            self.lineEdit.setText("")


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)

        self.ui = PyClientChat()
        self.ui.setupUi(self)

        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
