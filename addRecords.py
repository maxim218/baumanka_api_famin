## -*- coding: utf-8 -*-

import sys  
import urllib
import urllib2
import json
import time
from random import randint

reload(sys) 
sys.setdefaultencoding('utf-8')

def nl():
	print("  ")

def getUrl(s):
	url = 'http://localhost:5007/' + s
	return url

def sendGet(s):
	url = getUrl(s)
	result = urllib.urlopen(url).read()
	print("GET")
	print("Url: " + url)
	print("Answer: " + result)
	return result

def sendPost(s, body):
	headers = {'User-Agent' : 'python urllib2'}
	data = body
	url = getUrl(s)
	req = urllib2.Request(url, data, headers)
	response = urllib2.urlopen(req)
	result = response.read()
	print("POST")
	print("Url: " + url)
	print("Body: " + data)
	print("Answer: " + result)
	return result

def createJSONstring(obj):
	s = json.dumps(obj)
	return s

def writeHeader(s):
    nl()
    nl()
    print(str(s) + " ...")
    nl()
    time.sleep(3)

##########################################################################

countryNumber = 100
cityNumber = 150
airportNumber = 400
peopleNumber = 700
pairsNumber = 250
ticketsNumber = 3000

##########################################################################

writeHeader("Clear database")

jsonAnswer = sendGet("api/database/clear")

##########################################################################

writeHeader("Add countries")

for i in range(0, countryNumber):
    num = i + 1
    jsonAnswer = sendPost("api/database/country/add", createJSONstring({
        "country_name": "Country_" + str(num)
    }));

##########################################################################

writeHeader("Add cities")

for i in range(0, cityNumber):
    num = i + 1
    jsonAnswer = sendPost("api/database/city/add", createJSONstring({
        "city_name": "City_" + str(num),
        "city_country_id": randint(10, countryNumber - 10)
    }));

##########################################################################

writeHeader("Add airports")

for i in range(0, airportNumber):
    num = i + 1
    jsonAnswer = sendPost("api/database/airport/add", createJSONstring({
        "airport_name": "Airport_" + str(num),
        "airport_city_id": randint(10, cityNumber - 10)
    }));

##########################################################################

writeHeader("Add people")

for i in range(0, peopleNumber):
    num = i + 1
    jsonAnswer = sendPost("api/database/man/add", createJSONstring({
        "man_fullname": "Man_" + str(num),
        "man_city": randint(10, cityNumber - 10)
    }));

##########################################################################

writeHeader("Add pairs")

for i in range(0, pairsNumber):
    num = i + 1
    jsonAnswer = sendPost("api/database/pair/add", createJSONstring({
        "pair_man_a": randint(10, peopleNumber - 10),
        "pair_man_b": randint(10, peopleNumber - 10),
    }));

##########################################################################

writeHeader("Add tickets")

for i in range(0, ticketsNumber):
    num = i + 1
    jsonAnswer = sendPost("api/database/ticket/add", createJSONstring({
        "ticket_airport_a": randint(10, airportNumber - 10),
        "ticket_airport_b": randint(10, airportNumber - 10),
        "ticket_man_id": randint(10, peopleNumber - 10),
    }));

##########################################################################

nl()
nl()
print("Adding all records OK")
nl()
print("Press ENTER")
nl()

try:
	end = input()
except Exception:
	pass

