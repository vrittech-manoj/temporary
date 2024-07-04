import socket
#socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#connect to server
server_ip = '192.168.1.103'
server_port = 12345
print(f"connecting to server {server_ip}...... ")
s.connect((server_ip, server_port))
print(f"connected to server sucessfully to {server_ip} ")
#recv
while True:
 
    print(s.recv(1024).decode())
    message = input('#>>>')
    s.send(message.encode())
 
 
#close
s.close()