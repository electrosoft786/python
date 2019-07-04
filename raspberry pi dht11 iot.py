import time
import board
import I2C_LCD_driver
import adafruit_dht
import sys
import requests


#initial  the dht device, with data pin connected to:
dhtDevice = adafruit_dht.DHT11(board.D4)

#initial the lcd
mylcd = I2C_LCD_driver.lcd()


#Enter Your API Code Here
myAPI = 'KCDSWNQ9ELK6XEWR'

# URL where we will send the data, Don't change it
baseURL = 'https://api.thingspeak.com/update'

mylcd.lcd_display_string("Temp & Humidity", 1)
mylcd.lcd_display_string("  Monitoring Sys", 2)
time.sleep(3.0)



while True:
	try:
		#print the values to the serial port
		temperature_c = dhtDevice.temperature
		temperature_f = temperature_c * (9 / 5) + 32
		humidity = dhtDevice.humidity
		print("Temp: {:.1f} F / {:.1f} C   Humidity: {}%"
			.format(temperature_f, temperature_c, humidity))

		mylcd.lcd_clear()
		mylcd.lcd_display_string("Temp: %d%s C" % (temperature_c, chr(223)),1)
		mylcd.lcd_display_string("Humidity: %d %%" % humidity,2)
		
		data = {'api_key': myAPI, 'field1':temperature_c, 'field2':humidity};
		result = requests.post(baseURL, params=data)
		print (result.status_code)
                #if result.status_code == 200:
                #    print ("Success!! Thingspeak")
                #else
                #    print ("Fail!! Thingspeak")       
		
                
                           
	except RuntimeError as error:
		#Errors happen fairly often, DHT's are hard to read, just keep going
		print(error.args[0])
        
		
	
	

	time.sleep(2.0)

