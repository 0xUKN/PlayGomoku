#!/usr/bin/python3
from Gomoku import Gomoku

if __name__ == '__main__':
	try:
		Gomoku.Run()
	except KeyboardInterrupt:
		print("\n[!] Emergency exit ...")
