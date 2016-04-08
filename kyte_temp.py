#!/usr/bin/env python


import urllib2,json
import requests
import time
import RPi.GPIO as GPIO
import time
import sys


#sys.stdout = open('kyte_temp.log', 'a')
kell = time.ctime()

print "------------------------ TEMPERATUURI JA KYTTE REGULEERIMISE SKRIPT -------------------------"
print ""
print time.ctime(),"skript k2ivitub"
time.sleep(10)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# init list with pin numbers
print time.ctime(),"m22ran relee pin'id"

pinList = [17,27,22,5,6,13,19,26]
l_tuba = (13,19)
s_tuba = (22,5,6)
m_tuba = (26)



# loop through pins and set mode and state to 'low'

for i in pinList: 
    GPIO.setup(i, GPIO.OUT) 
    GPIO.output(i, GPIO.HIGH)
 
 # Reset GPIO settings
 # GPIO.cleanup()



while True:
# 28-0315a3fa6bff  28-031600196fff  28-0316001a5aff  28-0316002c5dff  28-0316002f89ff  28-031600ac11ff  28-031600ac35ff  28-031600dca7ff
# 28-0316001a53ff  28-0316002ee4ff 
# Open the file that we viewed earlier so that python can see what is in it. Replace the serial number as before.
	print time.ctime()," while tsykkel algab"
	t1file = open("/sys/bus/w1/devices/28-0315a3fa6bff/w1_slave")
	t2file = open("/sys/bus/w1/devices/28-031600196fff/w1_slave")
	t3file = open("/sys/bus/w1/devices/28-0316001a5aff/w1_slave")
	t4file = open("/sys/bus/w1/devices/28-0316002c5dff/w1_slave")
	t5file = open("/sys/bus/w1/devices/28-0316002f89ff/w1_slave")
	t6file = open("/sys/bus/w1/devices/28-031600ac11ff/w1_slave")
	t7file = open("/sys/bus/w1/devices/28-031600ac35ff/w1_slave")
	t8file = open("/sys/bus/w1/devices/28-031600dca7ff/w1_slave")
        t9file = open("/sys/bus/w1/devices/28-0316001a53ff/w1_slave")
        t10file = open("/sys/bus/w1/devices/28-0316002ee4ff/w1_slave")
	print time.ctime()," one wire loetud failidesse"
# Read all of the text in the file.
	text1 = t1file.read()
	text2 = t2file.read()
        text3 = t3file.read()
        text4 = t4file.read()
        text5 = t5file.read()
        text6 = t6file.read()
        text7 = t7file.read()
        text8 = t8file.read()
        text9 = t9file.read()
        text10 = t10file.read()
	print time.ctime()," k6ik text lotud failidest"
# Close the file now that the text has been read.
	t1file.close()
	t2file.close()
        t3file.close()
        t4file.close()
        t5file.close()
        t6file.close()
        t7file.close()
        t8file.close()
        t9file.close()
        t10file.close()
	print time.ctime()," failid sulgetud"
# Split the text with new lines (\n) and select the second line.
	secondline1 = text1.split("\n")[1]
	secondline2 = text2.split("\n")[1]
        secondline3 = text3.split("\n")[1]
        secondline4 = text4.split("\n")[1]
        secondline5 = text5.split("\n")[1]
        secondline6 = text6.split("\n")[1]
        secondline7 = text7.split("\n")[1]
        secondline8 = text8.split("\n")[1]
        secondline9 = text9.split("\n")[1]
        secondline10 = text10.split("\n")[1]
	print time.ctime()," modin ridu sobivaks"
# Split the line into words, referring to the spaces, and select the 10th word (counting from 0).
	temperaturedata1 = secondline1.split(" ")[9]
	temperaturedata2 = secondline2.split(" ")[9]
        temperaturedata3 = secondline3.split(" ")[9]
        temperaturedata4 = secondline4.split(" ")[9]
        temperaturedata5 = secondline5.split(" ")[9]
        temperaturedata6 = secondline6.split(" ")[9]
        temperaturedata7 = secondline7.split(" ")[9]
        temperaturedata8 = secondline8.split(" ")[9]
        temperaturedata9 = secondline9.split(" ")[9]
        temperaturedata10 = secondline10.split(" ")[9]

# The first two characters are "t=", so get rid of those and convert the temperature from a string to a number.
	temperature1 = float(temperaturedata1[2:])
	temperature2 = float(temperaturedata2[2:])
        temperature3 = float(temperaturedata3[2:])
        temperature4 = float(temperaturedata4[2:])
        temperature5 = float(temperaturedata5[2:])
        temperature6 = float(temperaturedata6[2:])
        temperature7 = float(temperaturedata7[2:])
        temperature8 = float(temperaturedata8[2:])
        temperature9 = float(temperaturedata9[2:])
        temperature10 = float(temperaturedata10[2:])

# Put the decimal point in the right place and display it.
	temperature1 = temperature1 / 1000
	temperature2 = temperature2 / 1000
        temperature3 = temperature3 / 1000
        temperature4 = temperature4 / 1000
        temperature5 = temperature5 / 1000
        temperature6 = temperature6 / 1000
        temperature7 = temperature7 / 1000
        temperature8 = temperature8 / 1000
        temperature9 = temperature9 / 1000
        temperature10 = temperature10 / 1000

# Naita temperatuuri
#	print temperature1 
#	print temperature2
#       print temperature3 
        print time.ctime()," Elutuba kollektor tagasi: ",temperature4 
#       print temperature5 
#       print temperature6
#       print temperature7 
        print time.ctime()," Magamistuba kollektor tagasi: ",temperature8 
#	print("-------")
	loe_temp1 = requests.get('http://192.168.1.251/feed/value.json?id=13&apikey=47ecd3901bec2ceed3d2f4ec8def40d4')
	temperature_tubadata = loe_temp1.text
	temperature_tuba = float(temperature_tubadata[1:-1])
#	print temperature_tuba

        loe_temp_el = requests.get('http://192.168.1.251/feed/value.json?id=92&apikey=47ecd3901bec2ceed3d2f4ec8def40d4')
        temperature_etubadata = loe_temp_el.text
        temperature_etuba = float(temperature_etubadata[1:-1])

        loe_temp_ma = requests.get('http://192.168.1.251/feed/value.json?id=93&apikey=47ecd3901bec2ceed3d2f4ec8def40d4')
        temperature_matubadata = loe_temp_ma.text
        temperature_matuba = float(temperature_matubadata[1:-1])

        loe_temp_la = requests.get('http://192.168.1.251/feed/value.json?id=94&apikey=47ecd3901bec2ceed3d2f4ec8def40d4')
        temperature_latubadata = loe_temp_la.text
        temperature_latuba = float(temperature_latubadata[1:-1])

#	magamistoa temperatuuri seadistus
	if temperature10 < temperature_matuba:
		GPIO.output(m_tuba, GPIO.LOW)
	elif temperature8 < 26:
		GPIO.output(m_tuba, GPIO.LOW)
	else:
		GPIO.output(m_tuba, GPIO.HIGH)

#	lastetoa temperatuuri seadistus
        if temperature9 < temperature_latuba:
                GPIO.output(l_tuba, GPIO.LOW)
        else:
                GPIO.output(l_tuba, GPIO.HIGH)

#	Elutoa temperatuuri seadistus
        if temperature_tuba < temperature_etuba:
                GPIO.output(s_tuba, GPIO.LOW)
        elif temperature4 < 28:
		GPIO.output(s_tuba, GPIO.LOW)
	else:
                GPIO.output(s_tuba, GPIO.HIGH)

	print time.ctime(),"Saadan andmed serverile..."

	r = requests.get('http://192.168.1.251/input/post.json?node=100&json={t1:'+str(temperature1)+'}&apikey=da060a9bca73b01fd7b00318049455af')
	r = requests.get('http://192.168.1.251/input/post.json?node=100&json={t2:'+str(temperature2)+'}&apikey=da060a9bca73b01fd7b00318049455af')
        r = requests.get('http://192.168.1.251/input/post.json?node=100&json={t3:'+str(temperature3)+'}&apikey=da060a9bca73b01fd7b00318049455af')
        r = requests.get('http://192.168.1.251/input/post.json?node=100&json={t4:'+str(temperature4)+'}&apikey=da060a9bca73b01fd7b00318049455af')
        r = requests.get('http://192.168.1.251/input/post.json?node=100&json={t5:'+str(temperature5)+'}&apikey=da060a9bca73b01fd7b00318049455af')
        r = requests.get('http://192.168.1.251/input/post.json?node=100&json={t6:'+str(temperature6)+'}&apikey=da060a9bca73b01fd7b00318049455af')
        r = requests.get('http://192.168.1.251/input/post.json?node=100&json={t7:'+str(temperature7)+'}&apikey=da060a9bca73b01fd7b00318049455af')
        r = requests.get('http://192.168.1.251/input/post.json?node=100&json={t8:'+str(temperature8)+'}&apikey=da060a9bca73b01fd7b00318049455af')
        r = requests.get('http://192.168.1.251/input/post.json?node=100&json={t9:'+str(temperature9)+'}&apikey=da060a9bca73b01fd7b00318049455af')
        r = requests.get('http://192.168.1.251/input/post.json?node=100&json={t10:'+str(temperature10)+'}&apikey=da060a9bca73b01fd7b00318049455af')

#	print ""
	print time.ctime(),"Andmed saadetud, ootan 60 sekundit..."
	print "" 
 	time.sleep(60)