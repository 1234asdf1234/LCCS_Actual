import serial   # Serial Library
import time     # Time Library

ser = serial.Serial() # We use the serial library to create a serial connection
ser.baudrate = 115200 # Set the baud rate to the same as that on the Microbit
#ser.port = "/dev/cu.usbmodem102"  # MacBook Only
ser.port = "com16"  # This virtual port changes. Use Cmd prompt and type: mode to get correct one
ser.open() # Open the port for communication.

while True:
    microbitData = str(ser.readline())  # Incoming data is a 'byte' object. Coverted to 'string' for easy manipulation
    temperature = microbitData
    temperature =str(temperature) # Converts temperature to an integer
    
    print(temperature)

#time.sleep(5)
ser.close() # Good Practice but actually doesn't do anything.
    
    
    
