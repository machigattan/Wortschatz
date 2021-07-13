import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

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

