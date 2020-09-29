#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# HTTP + URL packages
import httplib2
from urllib.parse import urlencode, quote # For URL creation

# To play wave files
import pygame
import math # For ceiling

import time

# Mary server informations
mary_host = "localhost"
mary_port = "59125"

# Input text
# filename = 'testfiles/test' + str(i)
# with open(filename, 'r') as file:
#     input_text = file.read().replace('\n',' ')

def generateWav(input_text):

    # Build the query
    query_hash = {"INPUT_TEXT":input_text,
                "INPUT_TYPE":"TEXT", # Input text
                "LOCALE":"en_US",
                "VOICE":"cmu-slt-hsmm", # Voice informations  (need to be compatible)
                "OUTPUT_TYPE":"AUDIO",
                "AUDIO":"WAVE", # Audio informations (need both)
                }
    query = urlencode(query_hash)
    print("query = \"http://%s:%s/process?%s\"" % (mary_host, mary_port, query))

    # Run the query to mary http server
    h_mary = httplib2.Http()
    start = time.time()
    resp, content = h_mary.request("http://%s:%s/process?" % (mary_host, mary_port), "POST", query)

    #  Decode the wav file or raise an exception if no wav files
    if (resp["content-type"] == "audio/x-wav"):

        # Write the wav file
        wfilename = "results/mary_test.wav"
        f = open(wfilename, "wb")
        f.write(content)
        f.close()
        end = time.time()
        print(end - start)
        # Play the wav file
        # pygame.mixer.init(frequency=16000) # Initialise the mixer
        # s = pygame.mixer.Sound("/tmp/output_wav.wav")
        # s.play()
        # pygame.time.wait(int(math.ceil(s.get_length() * 1000)))

    else:
        raise Exception(content)

