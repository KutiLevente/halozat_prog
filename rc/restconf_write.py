import requests, json
url = "https://172.19.255.216:443/restconf/data/ietf-interfaces:interfaces/interface=GigabitEthernet2"
a = ("admin", "admin")
h = {"Accept": "application/yang-data+json"}
d = {
  "ietf-interfaces:interface": {
    "name": "GigabitEthernet2",
    "description": "itt jartam",
    "enabled": True,
    "ietf-ip:ipv4": {
      "address": [
        {
          "ip": "192.168.10.2",
          "netmask": "255.255.255.0"
        }
      ]
    }
   }
}
patch_response = requests.patch(url, auth=a, headers=h, verify=False, data=json.dumps(d))
print(patch_response.status_code)
if patch_response.status_code == 200:
    print(patch_response.json())
else:
    print(patch_response.text)

