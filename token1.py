import requests
from requests.structures import CaseInsensitiveDict
url = "https://reqbin.com/echo/get/json"
head = CaseInsensitiveDict()
head ["Accept"] = "application/json"
head ["Authorization"] = "Bearor{token}"
r = requests.get(url, headers=head)
print(r.status_code)
print(r.text)
