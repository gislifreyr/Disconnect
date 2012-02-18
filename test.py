import game

b = game.board('6x6',3)
b.play('x',0)
b.draw()
if (b.fourinarow):
	print "TEST FAILED"
b.play('x',1)
b.draw()
if (b.fourinarow):
	print "TEST FAILED"
b.play('x',2)
b.draw()
if (b.fourinarow != 'x'):
	print "TEST FAILED"
