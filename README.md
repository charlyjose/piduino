# piduino
Arduino Raspberry Pi hacks


## Raspberry Pi not connecting to moniter?
-----------------------------------------
1. Put the your burned SD card to an android mobile/computer
2. Open /boot/config.txt in write mode
3. Uncomment: hdmi_force_hotplug=1
This works most of the time. Still not getting video output? Try altering anything containing `*hdmi*` (at your own risk)


## Enable remote communication
------------------------------
```bash
1. cli method
	1.1. $ sudo raspi-config
	1.2. Select P2 SSH
	1.3. Enable it
	1.4. Then Select Finish

	1.5. Select P3 VNC
	1.6. Enable it
	1.7. Then Select Finish

2. Graphical method
	2.1. Click on the raspberry at the top-left corner of your screen
	2.2. Click "Preferences"
	2.3. Click "Raspberry Pi Configuration"
	2.4. Enable IC2 and Serial
	2.5. Also enable SSH and VNC (it comes handy at times)
	2.6. Reboot the system
```


## Connect to wifi
------------------
### 1. cli method
```bash
	# Scan the wlan0
	1.1. $ sudo iwlist wlan0 scan
	# Kill wifi
	1.2. $ sudo rfkill block wifi
	# Add connection details [SSID, Passphrase]
	1.3. method 1:
		1.3.1 $ nano /etc/wpa_suplicant/wpa_suplicant.conf
		1.3.2. Append this in this file:
						
			network={
				ssid="SSID HERE"
				#psk="CLEAN TEXT PASSPHRASE HERE"
				# UNCOMMENT ANYONE
				psk=6ca015ac306ffe82a5f874ee307f10685bf83ae4f908321ad1defcfeeaa26015
			}

			Generating WPA PSK
				$ wpa_passphrase <ssid> [passphrase]
				Append the generated configuration to the above file
	
	1.4. method 2:
		1.4.1. $ wpa_passphrase <ssid> >> /etc/wpa_suplicant/wpa_suplicant.conf
	
	1.5.  $ sudo rfkill unblock wifi
```

### 2. Graphical method
```bash
	2.1. You know what to do...
```


## Getting around things
---------------------
```bash
1. $ gpio -v
2. $ gpio readall
```

## Setup the environment for Arduino-Pi communication
--------------------------------------------------
### 1. cli method
```bash
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
```

### 2. Graphical method
```bash
	2.1. Click on the raspberry at the top-left corner of your screen
	2.2. Click "Preferences"
	2.3. Click "Raspberry Pi Configuration"
	2.4. Enable IC2 and Serial
	2.5. Also enable SSH and VNC (it comes handy at times)
	2.6. Reboot the system
```


```bash
sudo apt-get install python-serial
sudo pip install pyserial
```
