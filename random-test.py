#!/usr/bin/python -u
import random
import game
import sys
import time

if (len(sys.argv) < 3):
	print "Invalid no. of arguments"
	print "Usage: %s <difficulty> <rounds> [size]"%sys.argv[0]
	print " - difficulty: 1-6 (warning: 6 takes forever!)"
	print " - rounds: number, for ex. 100"
	print " - size: board size, default: 3x6"
	sys.exit(1)
#
difficulty = int(sys.argv[1])
rounds = int(sys.argv[2])
try:
	size = sys.argv[3]
except:
	size = '3x6'

rand_won = 0
comp_won = 0
ties = 0
symbols = ['X','O']

def symbol_to_n(symbol):
	n = 0
	for symbol in symbols:
		if symbol == symbols[n]:
			return n
		n += 1

	return -1

(height, width) = [int(val) for val in size.split("x")]

for r in range(0,rounds):
	game_over = 0
	board = game.board(size, 3) # 3-in-a-row !
	computer = game.computer(board,difficulty)
	if (r % 10 == 0):
		print "Round %d/%d"%(r+1,rounds)
	computer_player = random.randrange(2) # which player is the computer?
	while (not game_over):
		board.draw()
		print "Computer should play: " + str(symbols[computer_player])
		# we are the random dude?
		for player in [0, 1]:
			if (board.fourinarow is not None or board.freespaces == 0):
				#print "Player %s is playing, but the game is over, or no free spaces"%player
				break
			if player == computer_player:
				computer.play(symbols[player])
			else:
				while (board.play(symbols[player], random.randrange(width)) != True):
					next

		if (board.fourinarow is not None):
			if board.fourinarow == symbols[computer_player]:
				#print "Woohoo, COMPUTER (%s) won"%board.fourinarow
				comp_won += 1
			else:
				#print "Boohoo, RANDOM (%s) won"%board.fourinarow
				rand_won += 1
			game_over = 1
		if (board.freespaces == 0):
			#print "WHAAA? IT'S A TIE!"
			ties += 1
			game_over = 1
	board.draw()

print "Ran %d rounds, computer wins: %d, random wins: %d, ties: %d"%(rounds, comp_won, rand_won, ties)
