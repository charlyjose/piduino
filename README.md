# piduino
Arduino Raspberry Pi hacks


Rasberry Pi not connecting to moniter?
-----------------------------------------
1. Put the your burned SD card to an android mobile/computer
2. Open /boot/config.txt in write mode
3. Uncomment: hdmi_force_hotplug=1
This works most of the time. Still not getting video output? Try altering anything containing *hdmi* (at your own risk)


Getting around things
---------------------
$ gpio -v
$ gpio readall


Setup the environment for arduino-Pi communocation
--------------------------------------------------
1. cli method
	1.1. $ sudo raspi-config
	1.2. Select P5 IC2
	1.3. Enable it
	1.4. Then Select Finish

	1.5. Open /boot/config.txt
	1.6. Check if this lines are not commented: 
		dtparam=spi=on
		dtparam=i2c_arm=on

	1.7. $ sudo apt-get install -y i2c-tools
	
	1.8. Reboot the system
		$ sudo reboot

2. Graphical method
	2.1. Click on the raspberry at the top-left corner of your screen
	2.2. Click "Preferences"
	2.3. Click "Raspberry Pi Configuration"
	2.4. Enable IC2 and Serial
	2.5. Also enable SSH and VNC (it comes handy at times)
	2.6. Reboot the system
 
sudo apt-get install python-serial
sudo pip install pyserial
