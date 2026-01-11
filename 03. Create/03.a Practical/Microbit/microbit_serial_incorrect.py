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
        
        # apparently junk characters come in different forms
        cleaned = microbitData
        cleaned = cleaned.replace("'",'')
        cleaned = cleaned.replace('\\r\\n','')

        # forgot that spaces are needed for separation of data
        cleaned = cleaned.replace(" ", "")

        print(cleaned)

        # then the code below would not be valid due to absence of spaces
        

        cleaned = cleaned.split(" ")
    
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


