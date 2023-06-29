import socket

# IP-Address and Port
HOST = '169.254.173.4'
PORT = 502

# Read data from Logger
def readData():
    with socket.socket(socket.AF_Inet, socket.SOCK_Stream) as s:
        s.connect(HOST, PORT)
        data = s.recv(1024).decode('utf-8')
        return data

def getTestData():
    data = 1
    return data
    