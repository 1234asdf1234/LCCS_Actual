import csv
import serial
import time

ser = serial.Serial()
ser.baudrate = 115200
ser.port = "com26"
ser.open()

header = ['light']
# Open the CSV file for writing
with open('lights.csv', 'w', newline='') as csvfile:
    db = csv.writer(csvfile)
    db.writerow(header)

    while True:
        microbitData = str(ser.readline())
        light = microbitData
        light = microbitData[2:]
        light = light.replace(' ','')
        light = light.replace("'",'')
        light = light.replace('\\r\\n','')
        light =int(light) # Not Necessary Always but can't do calculations without int conversion
        print(light)

        # Write the light to the CSV file
        db.writerow([light, light * 2]) # Square Brackets to create list with single element
        # Data written to .csv must be in a sequence {An iterable object that can be looped through}.
        csvfile.flush()  # Flush the data to ensure that it is written to the file

time.sleep(5)
ser.close()
