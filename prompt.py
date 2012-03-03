#!/usr/bin/python -u
import sys,game

def parse_input(inp):
	return

def startgame(board, has_computer):
	rounds = 0
	board.draw()
	if (has_computer):
		computer = game.computer(board)
	while (1):
		rounds += 1
		print 'Round: ' + str(rounds)
		for i in range(0,len(players)):
			player = players[i]
			symbol = player_symbols[i]
			if player == 'Computer':
				print "computer plays: " + symbol
				computer.play(symbol)
			else:        
				print player + " make your move (enter column number!)"
				while (1):
					try:
						play = raw_input(prompt)
						if not board.play(symbol, int(play)):
							raise Exception("Invalid play")
						break
					except Exception as e:
						print e
						print "Oops! Please try again, " + player
			board.draw()
			if (board.fourinarow is not None):
				# SOMEONE HAS SOMETHING IN A ROW!
				if (board.fourinarow == symbol):
					print "WOO HOO! CONGRATULATIONS " + player + " YOU WON, IN " + str(rounds) + " ROUNDS !"
					return


player_symbols = ['X', 'O', 'Y', 'Z']
players = []
n_players = 0

prompt = '>> '

print "Welcome to Disconnect!"
print "The game that will blow your mind!"
n_players = 0
print "Enter the number of human players (1-4)"
computer = 0 # default we do not expect a computer player
while (not n_players):
	n = raw_input(prompt)
	try:
		n = int(n)
		if n > len(player_symbols):
			raise Exception("Too many players!")
		if n < 2:
			print "You will face the computer! Do you wish to begin? (yes/no)"
			begin_ok = 0
			while (not begin_ok):
				resp = raw_input(prompt)
				if (resp.lower() == "yes"):
					begins = 1
					begin_ok = 1
				elif (resp.lower() == "no"):
					begins = 0
					begin_ok = 1
				else:
					print "Please enter a valid response, \"yes\" or \"no\""

			computer = 1
		n_players = n
	except:
		print "Please enter a number betwen 1 and 4"

if (computer and not begins):
	players.append("Computer")


for i in range(0, n_players):
	print "Please enter name for player " + str(i+1) + "."
	name_ok = 0
	while (not name_ok):
		p = raw_input(prompt)
		# XXX: check if p is empty??
		# XXX: check if another player has same name as p ??!?!?!?
		# XXX: check if a player has the name "Computer" ?
		players.append(p)
		name_ok = 1

if (computer and begins):
	players.append("Computer")

print "Now what size would you like the gameboard to be (default: 6x6)?"
has_size = 0
while (not has_size):
	size = raw_input(prompt)
	try:
		if size == '':
			size = '6x6' # default !
		(w,h) = size.split('x')
		print "Boarding will be " + str(int(w)) + "x" + str(int(h))
		has_size = 1
	except:
		print "Invalid size!"

print "And how many discs in a row does it take to win? It's your decision... (default: 4)"
has_discs = 0
while (not has_discs):
	discs = raw_input(prompt)
	try:
		if discs == '':
			discs = '4' # default !
		discs = int(discs)
		gameboard = game.board(size, discs) # useless, but makes "sure" that the input doesn't generate some exception..
		has_discs = 1
	except ValueError:
		print "Please enter a number?!"
	except Exception as e:
		print e

player_str = "Alright "
for i in range(0, len(players)):
	if i == len(players)-1:
		player_str += " and "
	else:
		if i != 0:
			player_str += ", "
	player_str += players[i]
		
print """
Alright %s, let's get ready to rumble! The gameboard will be a %r and you'll need %r discs in a row to win the game!
""" % (player_str,size,discs)

while(1):
	resp = raw_input("Are you brave enough? yes/no ")
	if (resp.lower() == "yes"):
		startgame(game.board(size,discs), computer)
	elif (resp.lower() == "no"):
		sys.exit()
	else:
		print "Silence equals approval!"
		startgame(game.board(size,discs), computer)


