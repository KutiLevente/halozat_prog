import requests, json

a=("admin", "admin")
url=("https://172.19.255.216:443/restconf/data/ietf-interfaces:interfaces/interface=GigabitEthernet1")
h={"Accept": "application/yang-data+json"}

#try:
reply = requests.get(url,headers=h,auth=a, verify = False)

#except:
#	print("Hiba")
#	exit

if reply.status_code == 200:
	print(reply.json())
else:
	print(reply.text)

print(reply.status_code)

