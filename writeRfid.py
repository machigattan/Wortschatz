import sys
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
# from __main__ import *

reader = SimpleMFRC522()

# https://pimylifeup.com/raspberry-pi-rfid-rc522/ simple script from pimylifeup that can write on tags

def write_function():
    # print(lines)
    word = sys.argv[1]
    text = input(word)
    print("waiting for tag")
    reader.write(text)
  
    id, text = reader.read() 
    print("Written on ", id)
    print(text, "is the new word")
    # GPIO.cleanup()

write_function()
# try:
#     print(lines)
#     text = lines
#     print("waiting for tag")
#     reader.write(text)
  
#     id, text = reader.read() 
#      print("Written on ", id)
#     print(text, "is the new word")

# finally:
#     GPIO.cleanup()

