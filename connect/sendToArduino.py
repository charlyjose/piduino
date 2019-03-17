import serial
import RPi.GPIO as GPIO
import time

ser=serial.Serial("/dev/ttyACM0",9600)  #change ACM number as found from ls /dev/tty/ACM*
ser.baudrate=9600


time.sleep(5);

ser.close()
ser.open()

for i in range(1, 1000):
	ser.write(b'1')
	print("Send")
	time.sleep(1)

# release GPIO pins
GPIO.cleanup();
ser.close();
