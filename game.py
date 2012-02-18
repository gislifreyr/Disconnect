

class board:
	def __init__(self, size='4x4', discs=4):
		self.size = size
		self.board = []
		self.UNUSED = '_'
		self.NTOWIN = discs
		self.init()
		self.fourinarow = None
	def init(self):
		(h,w) = self.size.split('x')
		self.height = int(h)
		self.width = int(w)
		for n in range(0,self.height):
			row = []
			for j in range(0,self.width):
				row.append(self.UNUSED) # default unused cell
			self.board.append(row)

	def draw(self):
		rstr = ''
		for n in range(0, self.width):
			rstr += ' ' + str(n) + '  '
		print rstr
		for row in self.board:
			rstr = ''
			for cell in row:
				rstr += "[" + cell + "] "
			print rstr

	def inuse(self,x,y):
		try:
			if (self.board[x][y] != self.UNUSED):
				return True
			else:
				return False
		except Exception as e:
			print e
			return True # out-of-bounds cells are considered "in use", so we avoid handling these exceptions

	def play(self, symbol, col):
		if (len(self.board[0]) <= col):
			raise Exception("Column out of bounds");
		# Let's start at the "bottom" and work our way up
		for n in range(self.height-1, -1, -1):
			#print "Checking [" + str(col) + "][" + str(n) + "]"
			if (not self.inuse(n, col)): # this cell is free, let's add the symbol and return True
				self.board[n][col] = symbol
				# we have successfully placed the symbol, let's check for 4-in-a-row!
				self.fourinarow = self.checkinarow(symbol, n, col)
				return True
		return False

	# Usage:  x = b.checkinarow(sym, r, c)
	# Before: b is a board object, b.board[r][c] == sym
	# After: x = sym if there are b.NTOWIN sym in a row, vertically, horizontally or diagonally, else x = None
	def checkinarow(self, symbol, row, col):
		nfound = 0
		# case 1: check horizontally!
		#print "base: " + str(row) + ":" + str(col)
		start = max(col - self.NTOWIN, 0)
		end = min(col + self.NTOWIN, self.width)
		#print "checking: " + str(start) + " -> " + str(end)
		for i in range(start, end): 
			#print "check: " + str(row) + ":" + str(i) + "(" + self.board[row][i] + ")"
			if (self.board[row][i] == symbol):
				nfound += 1
				if (nfound >= self.NTOWIN):
					return symbol
			else:
				nfound = 0

		#print "horizontal nfound = " + str(nfound)
		nfound = 0
		# case 2: check vertically!
		start = max(row - self.NTOWIN, 0)
		end = min(row + self.NTOWIN, self.height)
		for i in range(start, end):
			if (self.board[i][col] == symbol):
				nfound += 1
				if (nfound >= self.NTOWIN):
					return symbol
			else:
				nfound = 0
		#print "vertical nfound = " + str(nfound)

		# case 3: ... diagonal something?
		# case 4: ... diagonal something else?
		# if we reach here, then we don't have 4-in-a-row !
		return None
