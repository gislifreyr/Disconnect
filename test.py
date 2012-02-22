import game

print "Performing tests:"
b = game.board('6x6',3)
r = b.play('x',0)
if (not r or b.fourinarow):
	print "1: TEST FAILED"
else:
	print "1: TEST SUCCESSFUL"

r = b.play('x',1)
if (not r or b.fourinarow):
	print "2: TEST FAILED"
else:
	print "2: TEST SUCCESSFUL"

r = b.play('x',2)
if (not r or b.fourinarow != 'x'):
	print "3: TEST FAILED"
else:
	print "3: TEST SUCCESSFUL"

r = b.play('o',0)
if (r):
	print "4: TEST FAILED"
else:
	print "4: TEST SUCCESSFUL"

