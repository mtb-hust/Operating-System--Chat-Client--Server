# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chat.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

import socket
import socket
from threading import Thread
from queue import Queue
import random
def encoding(message):
    message = message.encode("utf-8")
    return message
def decoding(message):
    message = message.decode("utf-8")
    return message
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(263, 84)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 241, 61))
        self.groupBox.setStyleSheet("background-color:rgb(233, 210, 255);\n"
"border-radius: 5px")
        self.groupBox.setObjectName("groupBox")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(170, 20, 61, 23))
        self.pushButton.setStyleSheet("background-color:rgb(222, 242, 255);\n"
"border-radius: 5px")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(20, 20, 131, 20))
        self.lineEdit.setStyleSheet("background-color:rgb(222, 242, 255);\n"
"border-radius: 5px")
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.pushButton.clicked.connect(self.returnName)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox.setTitle(_translate("Dialog", "Enter your name:"))
        self.pushButton.setText(_translate("Dialog", "OK"))
        self.lineEdit.setText(_translate("Dialog", "Name..."))
    def returnName(self):
        return self.lineEdit.text()
class NameDialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(263, 84)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 241, 61))
        self.groupBox.setStyleSheet("background-color:rgb(233, 210, 255);\n"
"border-radius: 5px")
        self.groupBox.setObjectName("groupBox")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(170, 20, 61, 23))
        self.pushButton.setStyleSheet("background-color:rgb(222, 242, 255);\n"
"border-radius: 5px")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(20, 20, 131, 20))
        self.lineEdit.setStyleSheet("background-color:rgb(222, 242, 255);\n"
"border-radius: 5px")
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.pushButton.clicked.connect(self.returnName)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox.setTitle(_translate("Dialog", "Enter your name:"))
        self.pushButton.setText(_translate("Dialog", "OK"))
        self.lineEdit.setText(_translate("Dialog", "Name..."))
    def returnName(self):
        return self.lineEdit.text()
class ClientChat:
    def __init__(self, host, port):
        host = socket.gethostbyname(socket.gethostname())
        port = random.randint(6000,10000)
        self.host = host
        self.port = port
        self.name = "Guest"
        self.messageQueue = Queue()
        self.server = (self.host, 1235)
    def createSocket(self):
        try:
            print(f"Creating chat client on host {self.host}, port {self.port}")
            self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.clientSocket.bind((self.host, self.port))
            print(f"Creating chat client on host {self.host}, port {self.port} sucessfully")
        except Exception as e:
            print(e)
            print(f"Creating chat client on host {self.host}, port {self.port} failed")
    def defineUser(self):
        name = input("Enter your name: ")
        if name != "":
            self.name = name
        try:
            self.clientSocket.sendto(encoding(self.name + "join the chat server"), self.server)
        except:
            print("error")
    def messageReciever(self):
        while True:
            try:
                message, address = self.clientSocket.recvfrom(1024)
                print(message)
                self.messageQueue.put((message, address))
            except: 
                pass
    def startThread(self):
        reciever = Thread(target= self.messageReciever)
        reciever.start()

    def run(self):
        while True:
            message = input()
            if (message == 'quit'):
                break
            if message =='':
                continue
            message = self.name +":" + message
            message = encoding(message)
            self.clientSocket.sendto(message,self.server)
        self.clientSocket.sendto(encoding('qqq'), server)
        self.clientSocket.close(
        os._exit(1)
        )

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../ui/chat.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(506, 608)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 461, 71))
        font = QtGui.QFont()
        font.setFamily("Microsoft PhagsPa")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("background-color:rgb(233, 210, 255);\n"
"border-radius: 5px")
        self.groupBox.setObjectName("groupBox")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(86, 20, 131, 20))
        font = QtGui.QFont()
        font.setFamily("Microsoft PhagsPa")
        font.setPointSize(8)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgb(220, 239, 255)")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(256, 20, 91, 20))
        font = QtGui.QFont()
        font.setFamily("Microsoft PhagsPa")
        font.setPointSize(8)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color: rgb(220, 239, 255)")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(366, 20, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Microsoft PhagsPa")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(137, 178, 255);\n"
"border-radius:0px")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(46, 23, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Microsoft PhagsPa")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(134, 74, 255)rgb(255, 48, 238)")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(223, 24, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Microsoft PhagsPa")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(134, 74, 255)rgb(255, 48, 238)")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(33, 43, 391, 20))
        font = QtGui.QFont()
        font.setFamily("Microsoft PhagsPa")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_3.raise_()
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.pushButton.raise_()
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(20, 520, 391, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft PhagsPa")
        font.setPointSize(10)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("border-radius: 10px")
        self.textEdit.setTabChangesFocus(False)
        self.textEdit.setObjectName("textEdit")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 93, 461, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft PhagsPa")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet("background-color:rgb(233, 210, 255);\n"
"border-radius: 5px")
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(50, 11, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Microsoft PhagsPa")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(134, 74, 255)rgb(255, 48, 238)")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(230, 12, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Microsoft PhagsPa")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: rgb(134, 74, 255)rgb(255, 48, 238)")
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(89, 11, 121, 14))
        font = QtGui.QFont()
        font.setFamily("Microsoft PhagsPa")
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color: rgb(134, 74, 255)rgb(255, 48, 238)")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(265, 11, 141, 14))
        font = QtGui.QFont()
        font.setFamily("Microsoft PhagsPa")
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background-color: rgb(134, 74, 255)rgb(255, 48, 238)")
        self.label_8.setObjectName("label_8")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(420, 530, 61, 23))
        font = QtGui.QFont()
        font.setFamily("Microsoft PhagsPa")
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(137, 178, 255);\n"
"border-radius:5px")
        self.pushButton_3.setObjectName("pushButton_3")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 140, 461, 361))
        self.groupBox_3.setStyleSheet("border-radius:  10px;\n"
"background-color:qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0.318182 rgba(180, 100, 171, 169), stop:1 rgba(137, 171, 255, 255))")
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.scrollArea = QtWidgets.QScrollArea(self.groupBox_3)
        self.scrollArea.setGeometry(QtCore.QRect(8, 8, 445, 345))
        self.scrollArea.setStyleSheet("")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 445, 345))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 506, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        #Client
        self.clientHost = socket.gethostbyname(socket.gethostname())
        self.clientPort = random.randint(6000, 10000)

        self.label_7.setText(self.clientHost)
        self.label_8.setText(str(self.clientPort))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Server"))
        self.lineEdit.setText(_translate("MainWindow", "Enter server host"))
        self.lineEdit_2.setText(_translate("MainWindow", "Enter server port"))
        self.pushButton.setText(_translate("MainWindow", "Connect"))
        self.label.setText(_translate("MainWindow", "Host:"))
        self.label_2.setText(_translate("MainWindow", "Port:"))
        self.label_3.setText(_translate("MainWindow", "Please connect!"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Client"))
        self.label_4.setText(_translate("MainWindow", "Host:"))
        self.label_5.setText(_translate("MainWindow", "Port:"))
        self.label_7.setText(_translate("MainWindow", "...."))
        self.label_8.setText(_translate("MainWindow", "...."))
        self.pushButton_3.setText(_translate("MainWindow", "Send"))
    def connectClicked(self):
        Thread(target=self.clientThread).start()
    def clientThread(self):
        host =  self.label.text()
        port = self.label_2.text()
        self.label_3.setText("Connected")
        import sys
        app = QtWidgets.QApplication(sys.argv)
        Dialog = QtWidgets.QDialog()
        ui = Ui_Dialog()
        ui.setupUi(Dialog)
        Dialog.show()
        sys.exit(app.exec_())
    
    def sendMessage(self):
        a=1
    def personalMessage(self):
        print("aa")
    def makeGroupBox(self, text):
        hi = ""
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.pushButton.clicked.connect(lambda: ui.connectClicked())
    MainWindow.show()
    sys.exit(app.exec_())


