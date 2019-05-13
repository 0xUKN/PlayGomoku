#!/usr/bin/python3
import random
from . import Plateau

Plateau = Plateau.Plateau

MAX_VALUE = 99999999
MIN_VALUE = -99999999

class IA():
	def __init__(self, _value = 2):
		self.simulation_plateau = Plateau()
		self.value = _value
		self.opponent_value = 2
		self.last_played = (0, 0)
		if _value == 2:
			self.opponent_value = 1

	def Min(self, alpha, beta, depth):
		if self.simulation_plateau.isWin(self.last_played) != 0 or self.simulation_plateau.isFull() == True or depth <= 0:
			return self.EvalGame(depth)
		min_value = MAX_VALUE
		for x in range(self.simulation_plateau.size):
			for y in range(self.simulation_plateau.size):
				if self.simulation_plateau.grid[x][y] == 0:
					oldplayed = self.last_played
					self.last_played = (x, y)
					modified = self.simulation_plateau.PlayPlayer((x,y), self.opponent_value)
					min_value = min(min_value, self.Max(alpha, beta, depth - 1))
					self.simulation_plateau.PlayPlayer((x,y), 0)
					for case in modified:
						self.simulation_plateau.grid[case[0]][case[1]] = 3
					self.last_played = oldplayed
					if min_value <= alpha:
						return min_value
					beta = min(beta, min_value)
		return min_value

	def Max(self, alpha, beta, depth):
		if self.simulation_plateau.isWin(self.last_played) != 0 or self.simulation_plateau.isFull() == True or depth <= 0:
			return self.EvalGame(depth)
		max_value = MIN_VALUE
		for x in range(self.simulation_plateau.size):
			for y in range(self.simulation_plateau.size):
				if self.simulation_plateau.grid[x][y] == 0:
					oldplayed = self.last_played
					self.last_played = (x, y)
					modified = self.simulation_plateau.PlayPlayer((x,y), self.value)
					max_value = max(max_value, self.Min(alpha, beta, depth - 1))
					self.simulation_plateau.PlayPlayer((x,y), 0)
					for case in modified:
						self.simulation_plateau.grid[case[0]][case[1]] = 3
					self.last_played = oldplayed
					if max_value >= beta:
						return max_value
					alpha = max(alpha, max_value)
		return max_value

	def EvalGame(self, depth):
		base = self.simulation_plateau.isWin(self.last_played)
		advantagesPlayer, advantagesIA = self.simulation_plateau.advantages
		ret = [(advantagesIA - advantagesPlayer) * 10, MIN_VALUE - (depth * 10), MAX_VALUE + (depth * 10)][base]
		return ret
	
	def Play(self, current_plateau, depth = 3):
		self.UpdateCurrentPlateau(current_plateau)

		max_value = MIN_VALUE
		BEST_PLAY = []
		for x in range(self.simulation_plateau.size):
			for y in range(self.simulation_plateau.size):
				if self.simulation_plateau.grid[x][y] == 0:
					oldplayed = self.last_played
					self.last_played = (x, y)
					modified = self.simulation_plateau.PlayPlayer((x,y), self.value)
					max_tmp = self.Min(MIN_VALUE, MAX_VALUE, depth - 1)
					if max_tmp > max_value:
						max_value = max_tmp
						BEST_PLAY = [(x,y)]
					elif max_tmp == max_value:
						BEST_PLAY.append((x,y))
					self.simulation_plateau.PlayPlayer((x,y), 0)
					for case in modified:
						self.simulation_plateau.grid[case[0]][case[1]] = 3
					self.last_played = oldplayed
		choice = random.choice(BEST_PLAY)
		self.simulation_plateau.PlayPlayer(random.choice(BEST_PLAY), self.value)
		return choice
		

	def UpdateCurrentPlateau(self, current_plateau):
		self.simulation_plateau = current_plateau
		
