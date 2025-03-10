import requests, json

url="https://172.19.255.216/restconf/data/cisco-IOS-XE-native:native/interface/GigabitEthernet=2"
a=("admin","admin")
h={"Accept":"application/yang-data+json", "Content-Type":"application/yang-data+json"}
d=json.dumps({"Cisco-IOS-XE-native:GigabitEthernet":{"ip":{"address":{"primary":{"address":"10.0.2.1","mask":"255.255.255.0"}}}}})

r=requests.patch(url,auth=a,headers=h,)

