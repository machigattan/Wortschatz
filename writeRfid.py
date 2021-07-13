import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import sys, json

reader = SimpleMFRC522()

#Read data from stdin
def read_in():
    lines = sys.stdin.readlines()

    return json.loads(lines[0])

def main():
    #get our data as an array from read_in()
    lines = read_in()

    #return the sum to the output stream
    print (lines) 
      try:
        text = lines
        print("waiting for tag")
        reader.write(text)
    
        id, text = reader.read() 
        print("Written on ", id)
        print(text, "is the new word")
      finally:
        GPIO.cleanup()


# https://pimylifeup.com/raspberry-pi-rfid-rc522/ simple script from pimylifeup that can write on tags

 



# Start process
if __name__ == '__main__':
    main()