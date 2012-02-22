import game

print "Performing tests:"
b = game.board('6x6',3)
r = b.play('x',0)
total = 15
successful = 0

# Testing phase 1 is to verify that a) the fourinarow variable is set only when a player wins
# and b) that after it has been set, any attempts to play will fail
if (not r or b.fourinarow):
	print "1: TEST FAILED"
else:
	successful += 1
	print "1: TEST SUCCESSFUL"

r = b.play('x',1)
if (not r or b.fourinarow):
	print "2: TEST FAILED"
else:
	successful += 1
	print "2: TEST SUCCESSFUL"

r = b.play('x',2)
if (not r or b.fourinarow != 'x'):
	print "3: TEST FAILED"
else:
	successful += 1
	print "3: TEST SUCCESSFUL"

r = b.play('o',0)
if (r):
	print "4: TEST FAILED"
else:
	successful += 1
	print "4: TEST SUCCESSFUL"

print "Testing phase 1 complete, %d tests successful"%successful


try:
	b = game.board('1x1', 2)
	print "5: TEST FAILED"
except:
	successful += 1
	print "5: TEST SUCCESSFUL"

