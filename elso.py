import socket as so

d = input("Adj meg egy doamint! ")

s = so.socket(so.AF_INET, so.SOCK_STREAM)

s.connect((d, 80))

s.send("GET / HTTP1.1\r\n
