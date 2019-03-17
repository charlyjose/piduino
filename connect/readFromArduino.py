import serial
import RPi.GPIO as GPIO
import time

ser=serial.Serial("/dev/ttyACM0",9600)  #change ACM number as found from ls /dev/tty/ACM*
ser.baudrate=9600

time.sleep(5)

# close/open serial port
ser.close()
ser.open()

while True:
	read_ser=ser.readline()
	print(read_ser)


# release GPIO pins
GPIO.cleanup();
# close serial port
ser.close()
