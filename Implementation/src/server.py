import socket;
import string;
import re;
from socket import *;
server_socket = socket(AF_INET, SOCK_STREAM);
server_socket.bind(("127.0.0.1",9999));
server_socket.listen(20000);
print("Waiting for Connection...");
connection, addr = server_socket.accept();
data=connection.recv(1024);
data = data.decode();

print("Message is : \n",data);
server_socket.close();