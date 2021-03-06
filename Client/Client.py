import socket
from threading import Thread
from queue import Queue
import random
import os
import time

def encoding(message):
    message = message.encode("utf-8")
    return message

def decoding(message):
    message = message.decode("utf-8")
    return message

class ClientChat:
    def __init__(self, host, port):
        self.hostC = socket.gethostbyname(socket.gethostname()) #host, port client
        self.portC = random.randint(6000,10000) #init random + localhost
        self.host = host #host port server
        self.port = int(port) #cast string -> int
        self.name = "Guest" #ten khoi tao nguoi dung la guest(khach vang lai)
        self.messageQueue = Queue() #hang doi tin nhan
        self.server = (self.host, self.port) #tuple chua dia chi cua server
    def createSocket(self):
        try:
            print(f"Creating chat client on host {self.host}, port {self.port}")
            self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.clientSocket.bind((self.hostC, self.portC))
            print(f"Creating chat client on host {self.host}, port {self.port} sucessfully")
            return 1
        except Exception as e:
            print(e)
            print(f"Creating chat client on host {self.host}, port {self.port} failed")
            return 0
    def defineUser(self, name): #interface gui name
        # name = input("Enter your name: ")
        if name != "":
            self.name = name
        #Thoi gian gui va nhan toi da de xac nhan truy cap la 5 giay
        try:
            self.clientSocket.sendto(encoding(self.name + ": join the chat server"), self.server)
        except Exception as e:
            print(e)

    def messageReciever(self): #luong nhan tin
        while True:
            try:
                message, address = self.clientSocket.recvfrom(1024)
                message = decoding(message)
                self.messageQueue.put((message, address))
                print(message)
            except: 
                pass
    def startThread(self):
        #khoi tao luong
        reciever = Thread(target= self.messageReciever)

        reciever.start()

    def sendMessage(self, message): #ham nay dang interface hoan thanh
        if (message == 'qqq'):
                self.clientSocket.close()
                os._exit(1)
        if message =='':
            return

        message = self.name + ":" + message
        message = encoding(message) #encoding-> utf8 truoc khi gui
        self.clientSocket.sendto(message, self.server)
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
if __name__ == "__main__":
    host = "192.168.1.3"
    port = 1236
    client =  ClientChat(host, port)
    client.createSocket()
    client.startThread()
    client.defineUser(input("Name:"))
    client.run()