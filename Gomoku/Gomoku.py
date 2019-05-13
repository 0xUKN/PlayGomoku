#!/usr/bin/python3
from . import Game
import os

BANNIERE = """
============== Gomoku v2.0 ====================
"""

def ClearScreen():
	os.system('cls' if os.name == 'nt' else 'clear')

def ShowIntro():
	print(BANNIERE)
	print("[1] Play 1 vs 1\n[2] Play 1 vs IA")
	depth = 0
	begin = 0
	gamemode = 0
	while gamemode == 0:
		print("Choose gamemode (1 or 2)")
		try:
			gamemode = int(input(">"))
			if gamemode < 1 or gamemode > 2:
				gamemode = 0
				raise ValueError
		except ValueError:
			print("You must enter an integer between 1 and 2")
	print("Choose nickname for player 1")
	p1 = input(">")
	if gamemode == 1:
		print("Choose nickname for player 2")
		p2 = input(">")
	else:
		p2 = "IA"
		while depth == 0:
			print("Choose difficulty for AI (1-3)")
			try:
				depth = int(input(">"))
				if depth < 1 or depth > 3:
					depth = 0
					raise ValueError
			except ValueError:
				print("You must enter an integer between 1 and 3")
	while begin == 0:
		try:
			print("Choose who begins (1 for %s and 2 for %s)" % (p1, p2))
			begin = int(input(">"))
			if begin < 1 or begin > 2:
				begin = 0
				raise ValueError
		except ValueError:
			print("You must enter an integer between 1 and 2")
	return int(gamemode), p1, p2, depth, begin

def Run():
	game, joueur1, joueur2, max_depth, begin = ShowIntro()
	ClearScreen()
	myGame = Game.Game(joueur1, joueur2)
	if game == 1:
		myGame.Play1V1(begin)
	else:
		myGame.Play1VIA(max_depth, begin)




