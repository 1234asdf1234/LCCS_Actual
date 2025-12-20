import csv
import serial
import time

ser = serial.Serial()
ser.baudrate = 115200
ser.port = "com3"
ser.port = "/dev/cu.usbmodem14102" # MacBook Only 
ser.open()

header = ['Temperature']
# Open the CSV file for writing
with open('temperatures.csv', 'w', newline='') as csvfile:
    db = csv.writer(csvfile)
    db.writerow(header)

    while True:
        microbitData = str(ser.readline())
        temperature = microbitData
        temperature = microbitData[2:]
        temperature = temperature.replace(' ','')
        temperature = temperature.replace("'",'')
        temperature = temperature.replace('\\r\\n','')
        temperature =int(temperature) # Not Necessary Always but can't do calculations without int conversion
        print(temperature)

        # Write the temperature to the CSV file
        db.writerow([temperature, temperature * 2]) # Square Brackets to create list with single element
        # Data written to .csv must be in a sequence {An iterable object that can be looped through}.
        csvfile.flush()  # Flush the data to ensure that it is written to the file

time.sleep(5)
ser.close()


