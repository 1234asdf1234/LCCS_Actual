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

headers = ['temp', 'rh', 'lighting', 'score']
# Open the CSV file for writing
with open('output.csv', 'w', newline='') as csvfile:
    # prepare csv writer
    db = csv.writer(csvfile)
    db.writerow(headers)

    while True:
        # read data
        microbitData = str(ser.readline())
        print(microbitData)
        
        # clean data
        cleaned = microbitData
        cleaned = microbitData[3:]
        cleaned = cleaned.replace("'",'')
        cleaned = cleaned.replace('\\r\\n','')
        cleaned = cleaned.replace('\\n', '')
        print(cleaned)
        

        cleaned = cleaned.split(" ")
    
        temp = cleaned[0]
        rh = cleaned[1]
        lighting = cleaned[2]
        score = cleaned[3]

        # validate data
        # make sure rh and lighting >= 0
        if int(rh) < 0 or int(lighting) < 0:
            print("invalid data")
        else:
            # Write data to the CSV file
            db.writerow([temp, rh, lighting, score])
            csvfile.flush()
        
time.sleep(5)
ser.close()


