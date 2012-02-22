import game

print "Performing tests:"
b = game.board('6x6',3)
r = b.play('x',0)
tests = 0
successful = 0

# Testing phase 1 is to verify that a) the fourinarow variable is set only when a player wins
# and b) that after it has been set, any attempts to play will fail
tests += 1
if (not r or b.fourinarow):
	print "1: TEST FAILED"
else:
	successful += 1
	print "1: TEST SUCCESSFUL"

tests += 1
r = b.play('x',1)
if (not r or b.fourinarow):
	print "2: TEST FAILED"
else:
	successful += 1
	print "2: TEST SUCCESSFUL"

tests += 1
r = b.play('x',2)
if (not r or b.fourinarow != 'x'):
	print "3: TEST FAILED"
else:
	successful += 1
	print "3: TEST SUCCESSFUL"

tests += 1
r = b.play('o',0)
if (r):
	print "4: TEST FAILED"
else:
	successful += 1
	print "4: TEST SUCCESSFUL"

print "Testing phase 1 complete, %d tests successful"%successful


#  Testing phase 2 deals with various invalid game setups and moves
tests += 1
try:
	b = game.board('1x1', 2)
	print "5: TEST FAILED"
except:
	successful += 1
	print "5: TEST SUCCESSFUL"

b = game.board('6x6') #def
r1 = False
r2 = False
tests += 1
try:
	r1 = b.play('a', 100000)
	print "6: TEST FAILED"
except:
	print "6: TEST SUCCESSFUL"
	successful += 1

tests += 1
if (r1):
	print "7: TEST FAILED"
else:
	print "7: TEST SUCCESSFUL"
	successful += 1

tests += 1
try:
	r2 = b.play('a', -1)
	print "8: TEST FAILED"
except:
	print "8: TEST SUCCESSFUL"
	successful += 1

tests += 1
if (r2):
	print "9: TEST FAILED"
else:
	print "9: TEST SUCCESSFUL"
	successful += 1

print "Testing phase 2 complete, %d tests successful"%successful

if successful == tests:
	print "ALL TESTS SUCCEEDED, GOOD FOR YOU!"
else:
	print "%d/%d TESTS SUCCESSFUL, PLEASE CHECK YOUR CODE!"%(successful,tests)
