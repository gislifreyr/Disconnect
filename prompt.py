import sys,game

def startgame():
	board = game.board(size)
	while (1):
		r = raw_input(prompt)
		if (r == "exit"):
			return

prompt = '>> '

print "Welcome to Skifurod!"
print "The game that will blow your mind!"
print "Please enter name for player 1."
p1 = raw_input(prompt)

print "Please enter name for player 2."
p2 = raw_input(prompt)

print "Now what size would you like the gameboard to be?"
has_size = 0
while (not has_size):
	size = raw_input("> (e.g 6x6 or 6x3) ")
	try:
		(w,h) = size.split('x');
		print "Boarding will be " + str(int(w)) + "x" + str(int(h))
		has_size = 1
	except:
		print "Invalid size!"

print "And how many discs in a row does it take to win? It's your decision..."
discs = raw_input("> (e.g. 3 or 4) ")

print """
Alright %r and %r, let's get ready to rumble! The gameboard will be a %r and you'll need %r discs in a row to win the game!
""" % (p1,p2,size,discs)

while(1):

	resp = raw_input("Are you brave enough? yes/no ")
	if (resp.lower() == "yes"):
		startgame()
	elif (resp.lower() == "no"):
		sys.exit()
	else:
		print "We do not accept players that can not answer a simple question! \n Goodbye!"
		sys.exit()


