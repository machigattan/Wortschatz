# https://pimylifeup.com/raspberry-pi-rfid-rc522/ simple script from pimylifeup that can read tags

GPIO.setwarnings(False)
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
    id, text = reader.read()
    print('UID:' id)
    print('Vocab:' text)

finally: 
    GPIO.cleanup()
    