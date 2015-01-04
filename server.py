import socket
import sys
from thread import *
import cv2
import picamera
import numpy as np

HOST =  ''
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


#now keep talking with the client
def clientthread(conn):
  #Sending message to connected client
  conn.send('Welcome to the server. Type something and hit enter\n') #send only takes string
    
    #infinite loop so that function do not terminate and thread do not end.
  while True:
      
      #Receiving from client
      data = conn.recv(1024)
      parse = data.split()
      if parse[0] == 'capture':
        stream = io.BytesIO()
        with picamera.PiCamera() as camera:
            camera.capture(stream, format='jpeg')
        data = np.fromstring(stream.getvalue(), dtype=np.uint8)
        image = cv2.imdecode(data,1)
        conn.sendall(reply)
      if not parse[0]:
        break


  
    #came out of loop
  conn.close()

#now keep talking with the client
while 1:
  #wait to accept a connection - blocking call
  conn, addr = s.accept()
  print 'Connected with ' + addr[0] + ':' + str(addr[1])
    
    #start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
  start_new_thread(clientthread ,(conn,))

s.close()