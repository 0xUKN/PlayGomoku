#!/usr/bin/python3
from . import Plateau
from . import Gomoku
from . import IA
import time

Plateau = Plateau.Plateau
IA = IA.IA

class Game():
	def __init__(self, _player1, _player2):
		self.plateau = Plateau()
		self.player1 = _player1
		self.player2 = _player2

	def Play1V1(self, begin):
		self.plateau.PlayPlayer((7,7), begin)
		i = begin
		last_played = (0,0)
		while self.plateau.isFull() == False and self.plateau.isWin(last_played) == 0:
			Gomoku.ClearScreen()
			if i % 2 == 0:
				current_player = self.player1
				current_value_player = 1
			else:
				current_player = self.player2
				current_value_player = 2
			print("%s's turn !" % current_player)
			self.plateau.Show()
			print("Pick a line and a column (separated with ,)")
			inputList = None
			while inputList is None:
				if i != (begin + 1):
					inputList = self.parseInput(input("%s>" % current_player))
				else:
					inputList = self.specialParseInput(input("%s>" % current_player))
			last_played = inputList
			self.plateau.PlayPlayer(inputList, current_value_player)
			i += 1
		Gomoku.ClearScreen()
		self.plateau.Show()
		print("====== EGALITE ! ======" if self.plateau.isWin(last_played) == 0 else "====== Winner : %s ======" % current_player)

	def Play1VIA(self, max_depth, begin):
		self.plateau.PlayPlayer((7,7), begin)
		ai = IA()
		i = begin
		last_played = (0,0)
		start = 0
		end = 0
		while self.plateau.isFull() == False and self.plateau.isWin(last_played) == 0:
			Gomoku.ClearScreen()
			if i % 2 == 0:
				current_player = self.player1
				print("[!] IA played in %.2f seconds => Played %s \n" % (end - start, str(last_played)) if start != 0 else "")
				print("%s's turn !" % self.player1)
				self.plateau.Show()
				print("Pick a line and a column (separated with ,)")
				inputList = None
				while inputList is None:
					if i != (begin + 1):
						inputList = self.parseInput(input("%s>" % self.player1))
					else:
						inputList = self.specialParseInput(input("%s>" % self.player1))
				self.plateau.PlayPlayer(inputList, 1)
			else:
				self.plateau.Show()
				current_player = "IA"
				start = time.time()
				if i != (begin + 1):
					inputList = ai.Play(self.plateau, max_depth)
				else:
					inputList = (3,0xb)
					self.plateau.PlayPlayer(inputList, 2)
				end = time.time()
			last_played = inputList
				
			i += 1
		Gomoku.ClearScreen()
		self.plateau.Show()
		print("====== EGALITE ! ======" if self.plateau.isWin(last_played) == 0 else "====== Winner : %s ======" % current_player)

	def parseInput(self, inputString):
		inputList = inputString.split(',')
		try:
			inputList[0] = int(inputList[0], 16)
			inputList[1] = int(inputList[1], 16)
		except:
			print('ERROR : You must input valid values !')
			return None
		if len(inputList) != 2 or inputList[0] < 0 or inputList[0] > 14 or inputList[1] < 0 or inputList[1] > 14:
			print('ERROR : Invalid line/column selection...')
			return None
		elif self.plateau.isEmptyCell(inputList) is False:
			print('ERROR : This cell is already occupied !')
			return None
		return inputList

	def specialParseInput(self, inputString):
		inputList = inputString.split(',')
		try:
			inputList[0] = int(inputList[0], 16)
			inputList[1] = int(inputList[1], 16)
		except:
			print('ERROR : You must input valid values !')
			return None
		if len(inputList) != 2 or inputList[0] < 0 or inputList[0] > 14 or inputList[1] < 0 or inputList[1] > 14:
			print('ERROR : Invalid line/column selection...')
			return None
		if ((inputList[0] >= 4 and inputList[0] <= 10) and (inputList[1] >= 4 and inputList[1] <= 10)):
			print('ERROR : You need to pick a cell in a 7*7 square from the middle because you played first !')
			return None
		elif self.plateau.isEmptyCell(inputList) is False:
			print('ERROR : This cell is already occupied !')
			return None
		return inputList
		


