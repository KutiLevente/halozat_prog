from netmiko import ConnectHandler
from getpass import getpass

kapcs={
	"device_type":"cisco_ios",
	"host":"172.19.255.216",
	"username":"admin",
	"password":"admin"
}

cmd="show ip int brief"

with ConnectHandler(**kapcs) as k:
	out=k.send_command(cmd)
print(out)

