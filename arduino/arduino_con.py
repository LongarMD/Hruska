import serial
import time

ser = serial.Serial("/dev/ttyUSB0", 9600)
ser.baudrate = 9600

while True:
    print("On")
    ser.write("1 1 1 1\n".encode('ascii'))
    time.sleep(1)
    
    print("Off")
    ser.write("0 0 0 0\n".encode('ascii'))
    time.sleep(1)
