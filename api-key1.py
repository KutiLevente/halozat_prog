import requests

h={'x-api-key': 'DEMO_API_KEY'}

try:
	reply=requests.get("https://api.thecatapi.com/v1/breeds", headers=h)

except:
	print("Hiba")
	exit()

print(reply.json())

print(reply.status_code)

