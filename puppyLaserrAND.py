import serial
from random import randint
import time
global pan,tilt,ser
pan=4160/4
tilt=1500
ser=serial.Serial("/dev/ttyACM0")
print ser.portstr


def send_command(axis,value):

    bin_value=bin(value*4)
    bin_low='0b'+bin_value[-7:]
    bin_high=bin_value[:-7]
    ser.write(chr(0xAA))
    ser.write(chr(0x84))
    ser.write(chr(axis))
    ser.write(chr(int(bin_low,2)))
    ser.write(chr(int(bin_high,2)))
 
send_command(5,1000)

while(1):
    pan=randint(1000,1400)
    tilt=randint(1200,1700)
    send_command(1,tilt)
    send_command(0,pan)
    time.sleep(1.6)

# pythoncom.PumpMessages()
