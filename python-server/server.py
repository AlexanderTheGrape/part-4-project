import socket
import marytts-helper

# CURRENTLY RECEIVES 1024 BYTES AT A TIME.

# MaryTTS startup stuff here

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('localhost', 8089))
serversocket.listen(5) # become a server socket, maximum 5 connections

while True:
    connection, address = serversocket.accept()
    buf = connection.recv(1024)
    
    if len(buf) > 0:
        textToSynthesize = buf.decode("utf-8") 
        
        # now that we have the text for marytts, run it through marytts.
        generateWav(textToSynthesize)
        