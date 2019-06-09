#-*-coding:utf8;-*-
#qpy:3
#qpy:console

##import androidhelper
import time

##droid = androidhelper.Android()
#droid.ttsSpeak(time.strftime("%I %M %p on %A, %B %e, %Y"))

print("---hash.py---")

import hashlib
h1 = hashlib.sha256(b"hello world")
print(h1)

h1hex = hashlib.sha256(b"hello world").hexdigest()
print(h1hex)

scale = 16
h1bin = bin(int(h1hex, scale))[2:].zfill(255)


#h1bin = (h1.hexdigest())
print(h1bin)
#droid.ttsSpeak(h1bin)

import binascii 
h1bin = binascii.unhexlify(int(h1hex))
print(h1bin)


import pybitcoin
