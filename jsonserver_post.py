import requests

car= {
	"id": "7",
	"brand": "Porsche",
	"model": "911",
	"production_year": 2000,
	"convertible": False
	}

try:
	reply=requests.post("http://localhost:3000:/cars", json=car)
except:
	print("Hiba")
	exit
print(reply.status_code)

