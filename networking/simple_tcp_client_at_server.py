import socket

#black hat python

target_host = "0.0.0.0"
target_port = 9999

#create an object socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect the client
client.connect((target_host, target_port))

#send some data
client.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

#recieve some data
response = client.recv(4096)

print response
