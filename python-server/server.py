import socket
import os
from boltons.socketutils import BufferedSocket
from marytts_helper import generateWav

# CURRENTLY RECEIVES 1024 BYTES AT A TIME.

port = 8089
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# ip = serversocket.getsockname()[0]
# print("ip is: " + str(ip))
serversocket.bind(('', port))
serversocket.listen(5) # become a server socket, maximum 5 connections
#print("My name is: " + socket.gethostname() + "\n")

if (os.name == "posix"):
    print("Type 'hostname -I' in console to find host address. Port: " + str(port))
else:
    print("Server hosted on: " + socket.gethostbyname(socket.gethostname()) +":" + str(port))


connection, address = serversocket.accept()
buffered_socket = BufferedSocket(connection, None)
while True:

    # may need to move while loop here
    # buf = connection.recv(1024)
    print("Awaiting Message")
    received_str = ""
    while not('\n' in received_str):
        byte_string = buffered_socket.recv(32786)
        received_str = received_str + byte_string.decode("utf-8")
        
    print("received message: " + received_str)


    

    # last_buffer_size = 0
    # if len(buf) > 0:
        
    #     while len(buf) > last_buffer_size:
    #         last_buffer_size = len(buf)  
    #     textToSynthesize = buf.decode("utf-8") 
    #     print("received message: " + textToSynthesize)
        
        # now that we have the text for marytts, run it through marytts.
    
    
    
    generateWav(received_str)
        