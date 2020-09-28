import socket
from marytts_helper import generateWav

# CURRENTLY RECEIVES 1024 BYTES AT A TIME.

# MaryTTS startup stuff here

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('localhost', 8080))
serversocket.listen(5) # become a server socket, maximum 5 connections

def main():
    while True:

        # last_buffer_size = 0
        # if len(buf) > 0:
            
        #     while len(buf) > last_buffer_size:
        #         last_buffer_size = len(buf)
            buffer = receiveText()

            textToSynthesize = buffer.decode("utf-8")
            print("received message: " + textToSynthesize)
            
            # now that we have the text for marytts, run it through marytts.
            # generateWav(textToSynthesize)
            
def receiveText():
    connection, address = serversocket.accept()
    # may need to move while loop here
    buffer = connection.recv(1024)
    decoded_buffer = buffer.decode()

    buffering = True
    while buffering:
        if "\n" in buffer:
            (line, buffer) = buffer.split("\n", 1)
            return line + "\n"
        else:
            more = connection.recv(1024)
            if not more:
                buffering = False
            else:
                buffer += more
    if buffer:
        return buffer

main()