
import sys
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
# from testscript import send_it



new_word = sys.argv[1]
reader = SimpleMFRC522()
def send_it():

    print (str(new_word))
    return new_word
# https://pimylifeup.com/raspberry-pi-rfid-rc522/ simple script from pimylifeup that can write on tags

def write_function():
    # print(lines)
    text = input(new_word)
    print("waiting for tag")
    reader.write(text)
  
    id, text = reader.read() 
    print("Written on ", id)
    print(text, "is the new word")
    # GPIO.cleanup()

send_it()
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

