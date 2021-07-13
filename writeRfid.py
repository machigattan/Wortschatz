import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
# import sys, json

reader = SimpleMFRC522()

#Read data from stdin
def read_in():
    lines = sys.stdin.readlines()

       return json.loads(lines)

# https://pimylifeup.com/raspberry-pi-rfid-rc522/ simple script from pimylifeup that can write on tags

try:
    text = input('New word:')
    print("waiting for tag")
    reader.write(text)
  
    id, text = reader.read() 
     print("Written on ", id)
    print(text, "is the new word")

finally:
    GPIO.cleanup()

