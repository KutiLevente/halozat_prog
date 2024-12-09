import requests
id=input("Melyiket szertend torolni? ")
try:
	reply.delete("http://localhost:3000/cars" +id)
except:
	print("Hiba")
	exit
print(reply.status_code)
