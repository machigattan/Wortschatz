import sys, json
# import writeRfid
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

#Read data from stdin
def read_in():
    lines = sys.stdin.readlines()
    # Since our input would only be having one line, parse our JSON data from that
    return json.loads(lines[0])

def main():
    #get our data as an array from read_in()
    lines = read_in()

    #return the sum to the output stream
    # print (lines)
    
    print("waiting for tag")
    reader.write(lines)
  
    id, text = reader.read() 
    print("Written on ", id)
    print(lines, "is the new word")
    # GPIO.cleanup()

# def write_function():
#     print(lines)
#     text = input('New data:')
#     print("waiting for tag")
#     reader.write(text)
  
#     id, text = reader.read() 
#     print("Written on ", id)
#     print(text, "is the new word")
#     GPIO.cleanup()


# Start process
if __name__ == '__main__':
    main()
    # writeRfid.write_function()