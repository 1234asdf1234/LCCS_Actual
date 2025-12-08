import serial   # Serial Library
import time     # Time Library

ser = serial.Serial() # We use the serial library to create a serial connection
ser.baudrate = 115200 # Set the baud rate to the same as that on the Microbit
ser.port = "com3"  # This virtual port changes. Use Cmd prompt and type: mode to get correct one
#ser.port = "/dev/cu.usbmodem102" # MacBook Only 
ser.open() # Open the port for communication.

while True:
    
    microbitData = str(ser.readline())  # Incoming data is a 'byte' object. Coverted to 'string' for easy manipulation
    temperature = microbitData
    
    temperature = microbitData[2:]  # Gets rid of first 2 characters
    temperature = temperature.replace(' ','') # Gets rid blank of spaces
    temperature = temperature.replace("'",'') # Two "" with a ' in middle gets rid of the ' at the end

    temperature = temperature.replace('\\r\\n','') # Gets rid of the \r\n but has to use \\r\\n
    
    temperature =int(temperature) # int if you want to do calculations with this data. Could be str.
    
    print(temperature)

#time.sleep(5)
ser.close() # Good Practice but actually doesn't do anything.
    

    
    
    