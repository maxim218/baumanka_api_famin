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

# добавление нескольких человек

jsonAnswer = sendPost("api/database/man/add", createJSONstring({
    "man_fullname": "Maxim Kolotovkin",
	"man_city": 3
}));
objAnswer = parseResult(jsonAnswer)
normal = {
	"man_id": 1,
    "man_fullname": "Maxim Kolotovkin",
	"man_city": 3
}
equalObjects(normal, objAnswer)

jsonAnswer = sendPost("api/database/man/add", createJSONstring({
    "man_fullname": "Petrov Petr",
	"man_city": 3
}));
objAnswer = parseResult(jsonAnswer)
normal = {
	"man_id": 2,
    "man_fullname": "Petrov Petr",
	"man_city": 3
}
equalObjects(normal, objAnswer)

jsonAnswer = sendPost("api/database/man/add", createJSONstring({
    "man_fullname": "Fric August",
	"man_city": 5
}));
objAnswer = parseResult(jsonAnswer)
normal = {
	"man_id": 3,
    "man_fullname": "Fric August",
	"man_city": 5
}
equalObjects(normal, objAnswer)

jsonAnswer = sendPost("api/database/man/add", createJSONstring({
    "man_fullname": "Angela Ferkel",
	"man_city": 5
}));
objAnswer = parseResult(jsonAnswer)
normal = {
	"man_id": 4,
    "man_fullname": "Angela Ferkel",
	"man_city": 5
}
equalObjects(normal, objAnswer)

jsonAnswer = sendPost("api/database/man/add", createJSONstring({
    "man_fullname": "Lord Genry",
	"man_city": 1
}));
objAnswer = parseResult(jsonAnswer)
normal = {
	"man_id": 5,
    "man_fullname": "Lord Genry",
	"man_city": 1
}
equalObjects(normal, objAnswer)

jsonAnswer = sendPost("api/database/man/add", createJSONstring({
    "man_fullname": "Dorian Grey",
	"man_city": 2
}));
objAnswer = parseResult(jsonAnswer)
normal = {
	"man_id": 6,
    "man_fullname": "Dorian Grey",
	"man_city": 2
}
equalObjects(normal, objAnswer)

jsonAnswer = sendPost("api/database/man/add", createJSONstring({
    "man_fullname": "Nina Kolotova",
	"man_city": 2
}));
objAnswer = parseResult(jsonAnswer)
normal = {
	"man_id": 7,
    "man_fullname": "Nina Kolotova",
	"man_city": 2
}
equalObjects(normal, objAnswer)

##########################################################################

# попытка добавить людей из несуществующих городов

jsonAnswer = sendPost("api/database/man/add", createJSONstring({
    "man_fullname": "Jimmy Jobs",
	"man_city": 25
}));
objAnswer = parseResult(jsonAnswer)
normal = {
	"result": "CITY_NOT_FOUND"
}
equalObjects(normal, objAnswer)

jsonAnswer = sendPost("api/database/man/add", createJSONstring({
    "man_fullname": "Kollen Farel",
	"man_city": -5
}));
objAnswer = parseResult(jsonAnswer)
normal = {
	"result": "CITY_NOT_FOUND"
}
equalObjects(normal, objAnswer)

##########################################################################

# бронирование билетов пользователями

jsonAnswer = sendPost("api/database/ticket/add", createJSONstring({
    "ticket_airport_a": 3,
	"ticket_airport_b": 5,
	"ticket_man_id": 4
}));
objAnswer = parseResult(jsonAnswer)
normal = {
	"ticket_id": 1,
	"ticket_airport_a": 3,
	"ticket_airport_b": 5,
	"ticket_man_id": 4,
	"ticket_date": objAnswer["ticket_date"]
}
equalObjects(normal, objAnswer)

jsonAnswer = sendPost("api/database/ticket/add", createJSONstring({
    "ticket_airport_a": 6,
	"ticket_airport_b": 1,
	"ticket_man_id": 5,
}));
objAnswer = parseResult(jsonAnswer)
normal = {
	"ticket_id": 2,
	"ticket_airport_a": 6,
	"ticket_airport_b": 1,
	"ticket_man_id": 5,
	"ticket_date": objAnswer["ticket_date"]
}
equalObjects(normal, objAnswer)

jsonAnswer = sendPost("api/database/ticket/add", createJSONstring({
    "ticket_airport_a": 6,
	"ticket_airport_b": 4,
	"ticket_man_id": 1,
}));
objAnswer = parseResult(jsonAnswer)
normal = {
	"ticket_id": 3,
	"ticket_airport_a": 6,
	"ticket_airport_b": 4,
	"ticket_man_id": 1,
	"ticket_date": objAnswer["ticket_date"]
}
equalObjects(normal, objAnswer)

jsonAnswer = sendPost("api/database/ticket/add", createJSONstring({
    "ticket_airport_a": 5,
	"ticket_airport_b": 2,
	"ticket_man_id": 3,
}));
objAnswer = parseResult(jsonAnswer)
normal = {
	"ticket_id": 4,
	"ticket_airport_a": 5,
	"ticket_airport_b": 2,
	"ticket_man_id": 3,
	"ticket_date": objAnswer["ticket_date"]
}
equalObjects(normal, objAnswer)

jsonAnswer = sendPost("api/database/ticket/add", createJSONstring({
    "ticket_airport_a": 1,
	"ticket_airport_b": 3,
	"ticket_man_id": 2,
}));
objAnswer = parseResult(jsonAnswer)
normal = {
	"ticket_id": 5,
	"ticket_airport_a": 1,
	"ticket_airport_b": 3,
	"ticket_man_id": 2,
	"ticket_date": objAnswer["ticket_date"]
}
equalObjects(normal, objAnswer)

##########################################################################

# попытка добавления билетов с некорректными данными

jsonAnswer = sendPost("api/database/ticket/add", createJSONstring({
    "ticket_airport_a": 100,
	"ticket_airport_b": 2,
	"ticket_man_id": 3,
}));
objAnswer = parseResult(jsonAnswer)
normal = {
	"result": "AIRPORT_OR_MAN_NOT_FOUND"
}
equalObjects(normal, objAnswer)

jsonAnswer = sendPost("api/database/ticket/add", createJSONstring({
    "ticket_airport_a": 2,
	"ticket_airport_b": 200,
	"ticket_man_id": 3,
}));
objAnswer = parseResult(jsonAnswer)
normal = {
	"result": "AIRPORT_OR_MAN_NOT_FOUND"
}
equalObjects(normal, objAnswer)

jsonAnswer = sendPost("api/database/ticket/add", createJSONstring({
    "ticket_airport_a": 3,
	"ticket_airport_b": 2,
	"ticket_man_id": 500,
}));
objAnswer = parseResult(jsonAnswer)
normal = {
	"result": "AIRPORT_OR_MAN_NOT_FOUND"
}
equalObjects(normal, objAnswer)

##########################################################################

# добавление супружеских пар

jsonAnswer = sendPost("api/database/pair/add", createJSONstring({
    "pair_man_a": 3,
	"pair_man_b": 4
}));
objAnswer = parseResult(jsonAnswer)
normal = {
	"pair_id": 1,
	"pair_man_a": 3,
	"pair_man_b": 4
}
equalObjects(normal, objAnswer)

jsonAnswer = sendPost("api/database/pair/add", createJSONstring({
    "pair_man_a": 7,
	"pair_man_b": 1
}));
objAnswer = parseResult(jsonAnswer)
normal = {
	"pair_id": 2,
	"pair_man_a": 7,
	"pair_man_b": 1
}
equalObjects(normal, objAnswer)

jsonAnswer = sendPost("api/database/pair/add", createJSONstring({
    "pair_man_a": 6,
	"pair_man_b": 5
}));
objAnswer = parseResult(jsonAnswer)
normal = {
	"pair_id": 3,
	"pair_man_a": 6,
	"pair_man_b": 5
}
equalObjects(normal, objAnswer)

##########################################################################

# попытка добавить супружеские пары из несуществующих людей

jsonAnswer = sendPost("api/database/pair/add", createJSONstring({
    "pair_man_a": 100,
	"pair_man_b": 4
}));
objAnswer = parseResult(jsonAnswer)
normal = {
	"result": "MAN_NOT_FOUND"
}
equalObjects(normal, objAnswer)

jsonAnswer = sendPost("api/database/pair/add", createJSONstring({
    "pair_man_a": 4,
	"pair_man_b": 100
}));
objAnswer = parseResult(jsonAnswer)
normal = {
	"result": "MAN_NOT_FOUND"
}
equalObjects(normal, objAnswer)

jsonAnswer = sendPost("api/database/pair/add", createJSONstring({
    "pair_man_a": 100,
	"pair_man_b": 100
}));
objAnswer = parseResult(jsonAnswer)
normal = {
	"result": "MAN_NOT_FOUND"
}
equalObjects(normal, objAnswer)

##########################################################################

# получение информации о существующих людях

jsonAnswer = sendGet("api/database/man/3/get")
objAnswer = parseResult(jsonAnswer)
normal = {
	"man_id":3,
	"man_fullname": "Fric August",
	"man_city":5,"city_id": 5,
	"city_name": "Berlin",
	"city_country_id": 2,
	"country_id": 2,
	"country_name": "Germany"
}
equalObjects(normal, objAnswer)

jsonAnswer = sendGet("api/database/man/5/get")
objAnswer = parseResult(jsonAnswer)
normal = {
	"man_id":5,
	"man_fullname":"Lord Genry",
	"man_city":1,"city_id":1,
	"city_name":"London",
	"city_country_id":3,
	"country_id":3,
	"country_name":"England"
}
equalObjects(normal, objAnswer)

##########################################################################

# попытка получить информацию о несуществующем человеке

jsonAnswer = sendGet("api/database/man/17/get")
objAnswer = parseResult(jsonAnswer)
normal = {
	"result":"MAN_NOT_EXISTS"
}
equalObjects(normal, objAnswer)

##########################################################################

# получить информацию о супружеских парах

jsonAnswer = sendGet("api/database/pair/1/get")
objAnswer = parseResult(jsonAnswer)
normal = {
	"pair_id": 1,
	"pair_man_a": 3,
	"pair_man_b": 4,
	"man_1": "Fric August",
	"man_2": "Angela Ferkel"
}
equalObjects(normal, objAnswer)

jsonAnswer = sendGet("api/database/pair/2/get")
objAnswer = parseResult(jsonAnswer)
normal = {
	"pair_id": 2,
	"pair_man_a": 7,
	"pair_man_b": 1,
	"man_1": "Nina Kolotova",
	"man_2": "Maxim Kolotovkin"
}
equalObjects(normal, objAnswer)

jsonAnswer = sendGet("api/database/pair/3/get")
objAnswer = parseResult(jsonAnswer)
normal = {
	"pair_id": 3,
	"pair_man_a": 6,
	"pair_man_b": 5,
	"man_1": "Dorian Grey",
	"man_2": "Lord Genry"
}
equalObjects(normal, objAnswer)

##########################################################################

# попытка получить информацию о несуществующей паре

jsonAnswer = sendGet("api/database/pair/5/get")
objAnswer = parseResult(jsonAnswer)
normal = {
	"result":"PAIR_NOT_FOUND"
}
equalObjects(normal, objAnswer)

##########################################################################

# получить информацию о городе и его стране по имени города

jsonAnswer = sendGet("api/database/get_country_by_city_name?name=Moscow")
objAnswer = parseResult(jsonAnswer)
normal = {
	"city_id": 3,
	"city_name": "Moscow",
	"city_country_id": 1,
	"country_id": 1,
	"country_name": "Russia"
}
equalObjects(normal, objAnswer)

jsonAnswer = sendGet("api/database/get_country_by_city_name?name=Berlin")
objAnswer = parseResult(jsonAnswer)
normal = {
	"city_id": 5,
	"city_name": "Berlin",
	"city_country_id": 2,
	"country_id": 2,
	"country_name": "Germany"
}
equalObjects(normal, objAnswer)

##########################################################################

# попытка получить информацию о несуществующем городе

jsonAnswer = sendGet("api/database/get_country_by_city_name?name=Anadir")
objAnswer = parseResult(jsonAnswer)
normal = {
	"result":"NOT_FOUND"
}
equalObjects(normal, objAnswer)

##########################################################################

# получить все города определённой страны

jsonAnswer = sendGet("api/database/get_all_cities_of_country_by_name?name=Germany")
arrayAns = parseResult(jsonAnswer)
normal = [
	{"city_id":6,"city_name":"Bonn"},
	{"city_id":5,"city_name":"Berlin"}
]
equalArrays(normal, arrayAns)

jsonAnswer = sendGet("api/database/get_all_cities_of_country_by_name?name=Russia")
arrayAns = parseResult(jsonAnswer)
normal = [
	{"city_id":4,"city_name":"Murmansk"},
	{"city_id":3,"city_name":"Moscow"}
]
equalArrays(normal, arrayAns)

##########################################################################

# попытка получить города несуществующей страны

jsonAnswer = sendGet("api/database/get_all_cities_of_country_by_name?name=Meksika")
arrayAns = parseResult(jsonAnswer)
normal = []
equalArrays(normal, arrayAns)

##########################################################################

# получение информации о билетах

jsonAnswer = sendGet("api/database/tickets/all/info/select")
arrayAns = parseResult(jsonAnswer)
normal = [
	{
		"ticket_id": 5,
		"man_fullname": "Petrov Petr",
		"air_1": "AirportBerlin First",
		"air_2": "AirLondon First"
	},{
		"ticket_id": 4,
		"man_fullname": "Fric August",
		"air_1": "MoscowAirport First",
		"air_2": "AirportBerlin Second"
	},{
		"ticket_id": 3,
		"man_fullname": "Maxim Kolotovkin",
		"air_1": "MoscowAirport Second",
		"air_2": "AirLondon Second"
	},{
		"ticket_id": 2,
		"man_fullname": "Lord Genry",
		"air_1": "MoscowAirport Second",
		"air_2": "AirportBerlin First"
	},
	{
		"ticket_id": 1,
		"man_fullname": "Angela Ferkel",
		"air_1": "AirLondon First",
		"air_2": "MoscowAirport First"
	}
]
equalArrays(normal, arrayAns)

##########################################################################

# получить количество городов в странах (в стране должен быть хотя бы 1 город)

jsonAnswer = sendGet("api/database/read/from/view/v1/all")
arrayAns = parseResult(jsonAnswer)
normal = [
	{"city_country_id":3, "count":"2", "country_name":"England"},
	{"city_country_id":2, "count":"2", "country_name":"Germany"},
	{"city_country_id":1, "count":"2", "country_name":"Russia"}
]
equalArrays(normal, arrayAns)

##########################################################################

# добавляем ещё двух пользователей в страну

jsonAnswer = sendPost("api/database/man/add", createJSONstring({
    "man_fullname": "Olegov Oleg",
	"man_city": 3
}));
objAnswer = parseResult(jsonAnswer)
normal = {
	"man_id": 10,
    "man_fullname": "Olegov Oleg",
	"man_city": 3
}
equalObjects(normal, objAnswer)

jsonAnswer = sendPost("api/database/man/add", createJSONstring({
    "man_fullname": "Dmitriev Dmitriy",
	"man_city": 3
}));
objAnswer = parseResult(jsonAnswer)
normal = {
	"man_id": 11,
    "man_fullname": "Dmitriev Dmitriy",
	"man_city": 3
}
equalObjects(normal, objAnswer)

##########################################################################
##########################################################################

end = input()
