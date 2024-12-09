import requests

car=

try:
	reply=requests.put("http://localhost:3000/cars", json=car)
except:
	print("Hiba")
print(reply.status_code)

