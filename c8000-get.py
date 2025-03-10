import requests, json

a=("admin", "admin")
url=("https://172.19.255.216:443/restconf/data/ietf-interfaces:interfaces/interface=GigabitEthernet1")
h={"Accept": "application/yang-data+json"}

reply = requests.get(url,headers=h,auth=a,verify = False)

if reply.status_code == 200:
	print(reply.json())

print(reply.status_code)

