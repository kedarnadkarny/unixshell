import sys
import os
import psutil
import time

builtins = ['cd','exit']

def main():
	while (True):
		args = raw_input("> ").split(" ")
		if args[0] in builtins:
			builtins_exe(args)
		else:
			create_proc(args)

def builtins_exe(args):
	if args[0]=='exit':
		os._exit(0)
	elif args[0]=='cd':
		os.chdir(args[1])
		

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
