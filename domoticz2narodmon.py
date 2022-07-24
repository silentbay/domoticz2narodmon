import json
import requests
import urllib
import urllib.request

# URL to Domoticz device
# https://www.domoticz.com/wiki/Domoticz_API/JSON_URL's#Retrieve_status_of_specific_device for example http://127.0.0.1:8080/json.htm?type=devices&rid=1
URL = "###"
# MAC - unique identifier of the device in the narodmon.ru
DEVICE_MAC = "###"
# OWNER - device owner in the narodmon.ru
OWNER ="###"
# NAME - name of monitoring device
NAME = "###"

# Get data from domoticz
response = requests.get(URL)
data_raw = json.loads(response.text)
WSDCGQ11LM_temperature = (data_raw["result"][0]["Temp"])
WSDCGQ11LM_humidity = (data_raw["result"][0]["Humidity"])
WSDCGQ11LM_pressure = (data_raw["result"][0]["Barometer"])
#print (WSDCGQ11LM_temperature, WSDCGQ11LM_humidity, WSDCGQ11LM_pressure)

# Request formation
data = urllib.parse.urlencode({
'ID': DEVICE_MAC,
'OWNER': OWNER,
'NAME': NAME,
'TEMP': WSDCGQ11LM_temperature,
'HUMID': WSDCGQ11LM_humidity,
'PRESS': WSDCGQ11LM_pressure,
})
#print (data)

# Header
headers = {
'Content-Length': str(len(data)),
'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'narodmon.ru'
}

# Request
request = requests.post('http://narodmon.ru/post.php', data, headers)
#print (request)