import socket
import sys
import cv2
import numpy as np
try:
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
  print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
  sys.exit()

print 'Socket Created'

host = '10.120.122.231'
port = 8888

s.connect((host,port))
message = sys.stdin.readline()
s.sendall(message)
height = s.recv(1024)
print'HEIGHT received'
s.sendall('ok')
width = s.recv(1024)
print'WIDTH received'
s.sendall('ok')
Bstring = s.recv(1024)
print'Bstring received'
s.sendall('ok')
Gstring = s.recv(1024)
print'Gstring received'
s.sendall('ok')
Rstring = s.recv(1024)
print'Rstring received'