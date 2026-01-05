# Basic requirement 2

import csv
import serial
import time

ser = serial.Serial()
ser.baudrate = 115200
ser.port = "com3"
# run ls /dev/cu.*  to get path below
ser.port = "/dev/cu.usbmodem14102" # MacBook Only 
ser.open()

header = ['temp, rh, wind, score']
# Open the CSV file for writing
with open('output.csv', 'w', newline='') as csvfile:
    db = csv.writer(csvfile)
    db.writerow(header)

    while True:
        microbitData = str(ser.readline())
        
        cleaned = microbitData
        cleaned = microbitData[2:]
        cleaned = cleaned.replace(' ','')
        cleaned = cleaned.replace("'",'')
        cleaned = cleaned.replace('\\r\\n','')
        cleaned =int(cleaned) # Not Necessary Always but can't do calculations without int conversion
        print(cleaned)
        

        microbitData = cleaned.split(" ")
        temp = cleaned[0]
        rh = cleaned[1]
        wind = cleaned[2]
        score = cleaned[3]

        # Write data to the CSV file
        db.writerow([temp, rh, wind, score]) # Square Brackets to create list with single element
        # Data written to .csv must be in a sequence {An iterable object that can be looped through}.
        csvfile.flush()  # Flush the data to ensure that it is written to the file

time.sleep(5)
ser.close()


