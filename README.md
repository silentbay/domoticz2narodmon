# domoticz2narodmon :snake:

![img](https://github.com/silentbay/domoticz2narodmon/raw/main/img.png)

Simple script to send data from Domoticz to [narodmon.ru](https://narodmon.ru) 

Before run write your MAC, OWNER, NAME (see API Sensors Readings on narodmon.ru)

![api](https://github.com/silentbay/domoticz2narodmon/raw/main/api.png)

# Crontab

Send data every 5 minutes

	*/5 * * * * python3 /home/linuxuser/domoticz2narodmon.py