#!/usr/bin/python3

class Plateau():
	def __init__(self):
		self.size = 15
		self.grid = []
		self.advantages = (0, 0)
		for i in range(self.size):
			self.grid.append([3] * self.size)

	def isEmptyCell(self, coords):
		x, y = coords
		if x > (self.size - 1) or x < 0 or y > (self.size - 1) or y < 0:
			raise ValueError
		return self.grid[x][y] == 0 or self.grid[x][y] == 3
	
	def PlayPlayer(self, coords, playerValue):
		x, y = coords
		if x > (self.size - 1) or x < 0 or y > (self.size - 1)  or y < 0:
			raise ValueError
		play_side = []
		real_play_side = []
		for i in range(1, -2, -1):
			for j in range(1, -2, -1):
				play_side.append((x + j, y + i))
		for play in play_side:
			if play[0] < 0 or play[0] > 14 or play[1] < 0 or play[1] > 14 or self.grid[play[0]][play[1]] != 3:
				continue
			real_play_side.append(play)
			self.grid[play[0]][play[1]] = 0
		self.updateAdvantages(coords, playerValue)
		self.grid[x][y] = playerValue
		return real_play_side

	def updateAdvantages(self, last_played, playerValue):
		#Sub old advantages
		advP1 = 0
		advP2 = 0
		seqtab = self.extractSequences(last_played)
		for decouped in self.splitSequences(seqtab):
			if 1 not in decouped:
				advP2 += decouped.count(2) ** 4
			if 2 not in decouped:
				advP1 += decouped.count(1) ** 4
		self.advantages = (self.advantages[0] - advP1, self.advantages[1] - advP2)
		#Add new advantages
		oldval = self.grid[last_played[0]][last_played[1]]
		self.grid[last_played[0]][last_played[1]] = playerValue
		advP1 = 0
		advP2 = 0
		seqtab = self.extractSequences(last_played)
		for decouped in self.splitSequences(seqtab):
			if 1 not in decouped:
				advP2 += decouped.count(2) ** 4
			if 2 not in decouped:
				advP1 += decouped.count(1) ** 4
		self.advantages = (self.advantages[0] + advP1, self.advantages[1] + advP2)
		self.grid[last_played[0]][last_played[1]] = oldval
		
	
	def isFull(self):
		for line in self.grid:
			for case in line:
				if case == 0 or case == 3:
					return False
		return True

	def extractSequences(self, last_played):
		x, y = last_played
		rangetab = []
		line = self.grid[x]
		column = [self.grid[i][y] for i in range(self.size)]
		diagB_base = (x - min(x, y), y - min(x, y))
		diagH_base = (x + min(self.size - 1 - x, y), y - min(self.size - 1 - x, y))
		diagB = [self.grid[diagB_base[0] + i][diagB_base[1] + i] for i in range(self.size - diagB_base[0] - diagB_base[1])]
		diagH = [self.grid[diagH_base[0] - i][diagH_base[1] + i] for i in range(1 + abs(diagH_base[0] - diagH_base[1]))]
		rangetab.append(line)
		rangetab.append(column)
		rangetab.append(diagB)
		rangetab.append(diagH)
		return rangetab

	def splitSequences(self, seqtab):
		for sequence in seqtab:
			if len(sequence) < 5:
				continue
			for i in range(len(sequence) - 4):
				yield sequence[i:i+5]

	def isWin(self, last_played):
		seqtab = self.extractSequences(last_played)
		for decouped in self.splitSequences(seqtab):
			if decouped.count(1) == 5:
				return 1
			elif decouped.count(2) == 5:
				return 2
		return 0

	def Show(self):
		print("=" * (self.size * 2 + 1))
		print(" 0 1 2 3 4 5 6 7 8 9 a b c d e")
		print("=" * (self.size * 2 + 1))
		j = 0
		for line in self.grid:
			for i in line:
				print('| ' if i not in [1,2] else '|%s' % ['O','X'][i - 1], end='')
			print('| %s' % hex(j)[2:])
			j += 1
		print("=" * (self.size * 2 + 1))
			
		
