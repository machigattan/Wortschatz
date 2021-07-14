
import sys
import RPi.GPIO as GPIO

#https://github.com/pimylifeup/MFRC522-python A python library to read/write RFID tags via the budget MFRC522 RFID module.
from mfrc522 import SimpleMFRC522




new_word = sys.argv[1]
reader = SimpleMFRC522()
def send_it():

    print (str(new_word))
    return new_word


# https://pimylifeup.com/raspberry-pi-rfid-rc522/ simple script from pimylifeup that can write on tags

def write_function():
    # print(lines)
    text = new_word
    print("waiting for tag")
    reader.write(text)
  
    id, text = reader.read() 
    print("Written on ", id)
    print(text, "is the new word")
    # GPIO.cleanup()

send_it()
write_function()

