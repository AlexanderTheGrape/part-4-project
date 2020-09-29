import socket
from boltons.socketutils import BufferedSocket
from marytts_helper import generateWav

# CURRENTLY RECEIVES 1024 BYTES AT A TIME.

# MaryTTS startup stuff here

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('localhost', 8089))
serversocket.listen(5) # become a server socket, maximum 5 connections

connection, address = serversocket.accept()

while True:
    

    buffered_socket = BufferedSocket(connection, None)

    # may need to move while loop here
    # buf = connection.recv(1024)
    byte_string = buffered_socket.recv(32786)
    received_str = byte_string.decode("utf-8")

    print("received message: " + received_str)

    # last_buffer_size = 0
    # if len(buf) > 0:
        
    #     while len(buf) > last_buffer_size:
    #         last_buffer_size = len(buf)  
    #     textToSynthesize = buf.decode("utf-8") 
    #     print("received message: " + textToSynthesize)
        
        # now that we have the text for marytts, run it through marytts.
    
    
    
    generateWav(received_str)
        