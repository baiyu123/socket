import numpy as np
import cv2
import socket
import sys

HOST = ''
PORT = 8888
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'

try:
  s.bind((HOST,PORT))
except socket.error, msg:
  print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
  sys.exit()
print 'Socket bind complete'

s.listen(10)
print 'Socket now listensing'
conn, addr = s.accept()
print 'Connected with ' + addr[0] + ':' + str(addr[1])
while True:
  data = conn.recv(1024)
  parse = data.split()
  if parse[0] == 'c':
    img = cv2.imread('pussies.jpg',3)
    height, width, channel = img.shape
    B = img[:,:,0]
    G = img[:,:,1]
    R = img[:,:,2]
    Bstring = ''.join([chr(n) for n in R.reshape(1, height*width)[0,:]])
    Gstring = ''.join([chr(n) for n in R.reshape(1, height*width)[0,:]])
    Rstring = ''.join([chr(n) for n in R.reshape(1, height*width)[0,:]])
    conn.sendall(str(height))
    reply = conn.recv(1024)
    parse = reply.split()
    if parse[0] == 'ok':
      conn.sendall(str(width))
      reply = conn.recv(1024)
      parse = reply.split()
      if parse[0] == 'ok':
        conn.sendall(Bstring)
        reply = conn.recv(1024)
        parse = reply.split()
        if parse[0] == 'ok':
          conn.sendall(Gstring)
          print Gstring
          reply = conn.recv(1024)
          parse = reply.split()
          if parse[0] == 'ok':
            conn.sendall(Rstring)
            break
          else:
            print'G NOT RECEIVED'
            break
        else:
          print 'B NOT RECEIVED'
          break
      else:
        print'WIDTH NOT RECEIVED'
        break
    else:
      print'HEIGHT NOT RECEIVED'
      break
  else:
    break
s.close()