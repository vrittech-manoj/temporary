import socket
#socket
s = socket.socket() 
#bind
s.bind(('', 12345))  
#listen
print("Now server is in listening mood")
s.listen(5) 
#accept
c, addr = s.accept()
print ('Got connection from', addr )
#send
while True:
    input_message = input("#>>>")
    c.send(input_message.encode()) 
    message = c.recv(1024).decode()
    print("client: ",message)
#close
c.close()