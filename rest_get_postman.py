import requests
try:
	reply=requests.get("https://postman-echo.com/basic-auth/", auth=("postman","password"))
except:
	print("Hiba")
	exit()
if reply.status_code == 200:
	print(reply.json())
print(reply.status_code)
