import sys
import os
import psutil
import time

def main():
	while (True):
		#time.sleep(5)
		args = raw_input("> ").split(" ")
		if "exit" in args:
			break
		else:
			create_proc(args)

def create_proc(args):
	newpid = os.fork()
	if newpid==0:
		try:
			os.execvp(args[0], args)
		except Exception, e:
			print e.args
	elif newpid < 0:
		print "Error"
	else:
		os.waitpid(newpid, 0)

if __name__ == "__main__":
	main()
