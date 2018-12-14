## -*- coding: utf-8 -*-

import sys  
import urllib
import urllib2
import json
import time

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

def parseResult(jsonString):
	obj = json.loads(jsonString)
	return obj
	
def createJSONstring(obj):
	s = json.dumps(obj)
	return s
	
testNumber = 0

def equalObjects(aObj, bObj):
	global testNumber
	testNumber += 1
	print("Test: " + str(testNumber))
	n1 = len(aObj)
	n2 = len(bObj)
	# сравнение количества полей у объектов
	if (n1 != n2):
		message = "Error of test: Not equal length: " + str(n1) + " && " + str(n2)
		raise Exception(message)
	# перебор полей и сравнение их значений
	for key in aObj:
		v1 = str(aObj[key])
		v2 = str(bObj[key])
		if (v1 != v2):
			message = "Error of test: Not equal fields: " + str(v1) + " && " + str(v2)
			raise Exception(message)
	print("Objects equal OK")
	nl()

def equalObjectsForControlArrayElements(aObj, bObj):
	n1 = len(aObj)
	n2 = len(bObj)
	# сравнение количества полей у объектов
	if (n1 != n2):
		message = "Error of test: Not equal length: " + str(n1) + " && " + str(n2)
		raise Exception(message)
	# перебор полей и сравнение их значений
	for key in aObj:
		v1 = str(aObj[key])
		v2 = str(bObj[key])
		if (v1 != v2):
			message = "Error of test: Not equal fields: " + str(v1) + " && " + str(v2)
			raise Exception(message)
	print("Objects equal OK")

def equalArrays(arrA, arrB):
	global testNumber
	testNumber += 1
	print("Test: " + str(testNumber))
	a = len(arrA)
	b = len(arrB)
	# сравниваем длины массивов
	if(a != b):
		message = "Error of test: Not equal length of arrays: " + str(a) + " && " + str(b)
		raise Exception(message)
	# сравнение элементов в массиве
	for i in range(0, a):
		equalObjectsForControlArrayElements(arrA[i], arrB[i])
	print("Array equal OK")
	nl()

##########################################################################

# очистка базы данных

jsonAnswer = sendGet("api/database/clear")
objAnswer = parseResult(jsonAnswer)
normal = {"result": "INIT_DATABASE_OK"}
equalObjects(normal, objAnswer)

##########################################################################

# добавление нескольких стран

jsonAnswer = sendPost("api/database/country/add", createJSONstring({
	"country_name": "Russia"
}));
objAnswer = parseResult(jsonAnswer)
normal = {
    "country_id": 1,
    "country_name": "Russia"
}
equalObjects(normal, objAnswer)

jsonAnswer = sendPost("api/database/country/add", createJSONstring({
	"country_name": "Germany"
}));
objAnswer = parseResult(jsonAnswer)
normal = {
    "country_id": 2,
    "country_name": "Germany"
}
equalObjects(normal, objAnswer)

jsonAnswer = sendPost("api/database/country/add", createJSONstring({
	"country_name": "England"
}));
objAnswer = parseResult(jsonAnswer)
normal = {
    "country_id": 3,
    "country_name": "England"
}
equalObjects(normal, objAnswer)

##########################################################################

# попытка добавить уже существующие страны

jsonAnswer = sendPost("api/database/country/add", createJSONstring({
	"country_name": "Russia"
}));
objAnswer = parseResult(jsonAnswer)
normal = {
    "result": "COUNTRY_ALREADY_EXISTS"
}
equalObjects(normal, objAnswer)

jsonAnswer = sendPost("api/database/country/add", createJSONstring({
	"country_name": "Germany"
}));
objAnswer = parseResult(jsonAnswer)
normal = {
    "result": "COUNTRY_ALREADY_EXISTS"
}
equalObjects(normal, objAnswer)

##########################################################################

# добавить несколько городов

jsonAnswer = sendPost("api/database/city/add", createJSONstring({
	"city_name": "London",
    "city_country_id": 3
}));
objAnswer = parseResult(jsonAnswer)
normal = {
    "city_id": 1,
    "city_name": "London",
    "city_country_id": 3
}
equalObjects(normal, objAnswer)

jsonAnswer = sendPost("api/database/city/add", createJSONstring({
	"city_name": "Liverpool",
    "city_country_id": 3
}));
objAnswer = parseResult(jsonAnswer)
normal = {
    "city_id": 2,
    "city_name": "Liverpool",
    "city_country_id": 3
}
equalObjects(normal, objAnswer)

jsonAnswer = sendPost("api/database/city/add", createJSONstring({
	"city_name": "Moscow",
    "city_country_id": 1
}));
objAnswer = parseResult(jsonAnswer)
normal = {
    "city_id": 3,
    "city_name": "Moscow",
    "city_country_id": 1
}
equalObjects(normal, objAnswer)

jsonAnswer = sendPost("api/database/city/add", createJSONstring({
	"city_name": "Murmansk",
    "city_country_id": 1
}));
objAnswer = parseResult(jsonAnswer)
normal = {
    "city_id": 4,
    "city_name": "Murmansk",
    "city_country_id": 1
}
equalObjects(normal, objAnswer)

jsonAnswer = sendPost("api/database/city/add", createJSONstring({
	"city_name": "Berlin",
    "city_country_id": 2
}));
objAnswer = parseResult(jsonAnswer)
normal = {
    "city_id": 5,
    "city_name": "Berlin",
    "city_country_id": 2
}
equalObjects(normal, objAnswer)

jsonAnswer = sendPost("api/database/city/add", createJSONstring({
	"city_name": "Bonn",
    "city_country_id": 2
}));
objAnswer = parseResult(jsonAnswer)
normal = {
    "city_id": 6,
    "city_name": "Bonn",
    "city_country_id": 2
}
equalObjects(normal, objAnswer)

##########################################################################

# попытка добавить города в несуществующие страны

jsonAnswer = sendPost("api/database/city/add", createJSONstring({
	"city_name": "Ekaterinburg",
    "city_country_id": 25
}));
objAnswer = parseResult(jsonAnswer)
normal = {
    "result": "COUNTRY_NOT_FOUND"
}
equalObjects(normal, objAnswer)

jsonAnswer = sendPost("api/database/city/add", createJSONstring({
	"city_name": "Samara",
    "city_country_id": 82
}));
objAnswer = parseResult(jsonAnswer)
normal = {
    "result": "COUNTRY_NOT_FOUND"
}
equalObjects(normal, objAnswer)

##########################################################################

# добавить несколько аэропортов

jsonAnswer = sendPost("api/database/airport/add", createJSONstring({
    "airport_name": "AirportBerlin First",
	"airport_city_id": 5
}));
objAnswer = parseResult(jsonAnswer)
normal = {
    "airport_id": 1,
    "airport_name": "AirportBerlin First",
	"airport_city_id": 5
}
equalObjects(normal, objAnswer)

jsonAnswer = sendPost("api/database/airport/add", createJSONstring({
    "airport_name": "AirportBerlin Second",
	"airport_city_id": 5
}));
objAnswer = parseResult(jsonAnswer)
normal = {
    "airport_id": 2,
    "airport_name": "AirportBerlin Second",
	"airport_city_id": 5
}
equalObjects(normal, objAnswer)

jsonAnswer = sendPost("api/database/airport/add", createJSONstring({
    "airport_name": "AirLondon First",
	"airport_city_id": 1
}));
objAnswer = parseResult(jsonAnswer)
normal = {
    "airport_id": 3,
    "airport_name": "AirLondon First",
	"airport_city_id": 1
}
equalObjects(normal, objAnswer)

jsonAnswer = sendPost("api/database/airport/add", createJSONstring({
    "airport_name": "AirLondon Second",
	"airport_city_id": 1
}));
objAnswer = parseResult(jsonAnswer)
normal = {
    "airport_id": 4,
    "airport_name": "AirLondon Second",
	"airport_city_id": 1
}
equalObjects(normal, objAnswer)

jsonAnswer = sendPost("api/database/airport/add", createJSONstring({
    "airport_name": "MoscowAirport First",
	"airport_city_id": 3,
}));
objAnswer = parseResult(jsonAnswer)
normal = {
    "airport_id": 5,
    "airport_name": "MoscowAirport First",
	"airport_city_id": 3,
}
equalObjects(normal, objAnswer)

jsonAnswer = sendPost("api/database/airport/add", createJSONstring({
    "airport_name": "MoscowAirport Second",
	"airport_city_id": 3,
}));
objAnswer = parseResult(jsonAnswer)
normal = {
    "airport_id": 6,
    "airport_name": "MoscowAirport Second",
	"airport_city_id": 3,
}
equalObjects(normal, objAnswer)

##########################################################################

# попытка добавить аэропорты в несуществующие города

jsonAnswer = sendPost("api/database/airport/add", createJSONstring({
    "airport_name": "NoNameAirport Single",
	"airport_city_id": 57,
}));
objAnswer = parseResult(jsonAnswer)
normal = {
    "result": "CITY_NOT_FOUND",
}
equalObjects(normal, objAnswer)

jsonAnswer = sendPost("api/database/airport/add", createJSONstring({
    "airport_name": "NoNameAirport Single",
	"airport_city_id": 124,
}));
objAnswer = parseResult(jsonAnswer)
normal = {
    "result": "CITY_NOT_FOUND",
}
equalObjects(normal, objAnswer)

##########################################################################



