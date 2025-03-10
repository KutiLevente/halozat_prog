import requests
try:
	reply=requests.get("http://localhost:3000/cars/2")
except:
	print("Hiba")
	exit
#print(reply.json())
print(reply.status_code)

