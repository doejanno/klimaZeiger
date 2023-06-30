import socket
import log

# Read data from Logger
def readData(HOST, PORT):
    try:
        with socket.socket(socket.AF_Inet, socket.SOCK_Stream) as s:
            s.connect(HOST, PORT)
            data = s.recv(1024).decode('utf-8')
            return data
    except:
        log.logText('Could not establish connection')

# Test as long as there is no logger
def getTestData():
    data = 1
    return data
