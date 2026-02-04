# Basic requirement 2

import csv
import serial

ser = serial.Serial()
ser.baudrate = 115200
# run "mode" in cmd to get this
ser.port = "com3"
# run ls /dev/cu.*  to get path below
ser.port = "/dev/cu.usbmodem14102" # MacBook Only 
ser.open()

header = ['temp', 'rh', 'lighting', 'score']
# Open the CSV file for writing
with open('output.csv', 'w', newline='') as csvfile:
    db = csv.writer(csvfile)
    db.writerow(header)

    while True:
        microbitData = str(ser.readline())
        print(microbitData)
        
        cleaned = microbitData
        # removes prefix junk characters
        cleaned = microbitData[3:]
        cleaned = cleaned.replace("'",'')
        cleaned = cleaned.replace('\\r\\n','')
        # may occur on specific platforms, take into account
        cleaned = cleaned.replace('\\n', '')
        print(cleaned)
        
        # splitting works due to spaces are preserved
        cleaned = cleaned.split(" ")
    
        # assign elements into variables
        temp = cleaned[0]
        rh = cleaned[1]
        lighting = cleaned[2]
        score = cleaned[3]

        # Write data to the CSV file
        db.writerow([temp, rh, lighting, score]) # Square Brackets to create list with single element
        # Data written to .csv must be in a sequence {An iterable object that can be looped through}.
        csvfile.flush()  # Flush the data to ensure that it is written to the file
        
time.sleep(5)
ser.close()


