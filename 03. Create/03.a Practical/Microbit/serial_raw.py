# test script to investigate the sensor outputs

'''
temperature: done
light sensor: differs on microbit chips, found working one (done)
humidity: pending
'''


import serial

ser = serial.Serial()
ser.baudrate = 115200
# run "mode" in cmd to get this
ser.port = "com3"
# run ls /dev/cu.*  to get path below
ser.port = "/dev/cu.usbmodem14102" # MacBook Only 
ser.open()

while True:
    microbitData = str(ser.readline())
    print(microbitData)