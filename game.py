# -*- coding: utf-8 -*-
import math,gtk,random

class GraphicalBoard(gtk.DrawingArea):
	# Draw in response to an expose-event
	__gsignals__ = { "expose-event": "override" }
	# Handle the expose-event by drawing
	def __init__(self, board = None):
		super(GraphicalBoard, self).__init__()
		self.board = board
	def do_expose_event(self, event):
		# Create the cairo context
		cr = self.window.cairo_create()
		# Restrict Cairo to the exposed area; avoid extra work
		cr.rectangle(event.area.x, event.area.y, event.area.width, event.area.height)
		cr.clip()
		self.drawbg(cr, *self.window.get_size())  # XXX: gæti verið fallegra
		self.drawboard(cr, *self.window.get_size())

	def drawbg(self, cr, width, height):
		print "Drawing on a window of width=" + str(width) + " and height=" + str(height)
		# Fill the background with gray
		cr.set_source_rgb(0.5, 0.5, 0.5)
		cr.rectangle(0, 0, width, height)
		cr.fill()

	def drawboard(self, cr, width, height):
		bwidth = self.board.width;
		bheight = self.board.height;
		# let's calculate the dimensions of each of our disc-slots, based on this information
		# we'll have a 10px margin between slots
		slotw = (width - (10 * bwidth)) / bwidth;
		sloth = (height - (10 * bheight)) / bheight;
		print "Slow width=" + str(slotw) + " height=" + str(sloth)
		(startx,starty) = (10,10)
		for row in range(bwidth):
			starty = 0
			for col in range(bheight):
				cr.set_source_rgb(random.random(), random.random(), random.random())
				cr.rectangle(startx, starty, slotw, sloth)
				cr.fill()
				starty += sloth+10
			startx += slotw+10

class board:
	def __init__(self, size='3x6', discs=4):
		self.size = size
		self.board = []
		self.board_heatmap = []
		self.UNUSED = '_'
		self.NTOWIN = discs
		self.fourinarow = None
		self.freespaces = -1 # ... something impossible
		return self.init()
	def init(self):
		(h,w) = self.size.split('x')
		self.height = int(h)
		self.width = int(w)
		self.freespaces = self.height * self.width
		if (self.height < self.NTOWIN and self.width < self.NTOWIN):
			raise Exception("The number of discs-in-a-row to win, may not be greater than both board dimensions!")

		for n in range(self.height):
			row = []
			for j in range(self.width):
				row.append(self.UNUSED) # default unused cell
			self.board.append(row)

		# initialize heatmap
		for n in range(self.height):
			row = []
			for col in range(self.width):
				row.append(self.heat_value(col-(self.width/2)))
			self.board_heatmap.append(row)

	def heat_value(self, n):
		return 1-(n*n)/50.0 # 1 - (x^2 / 50.0)

	def __getitem__(self,pos):
		return self.board[pos]

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

	def draw_gui(self,something):
		# XXX: TBD!
		return False

	def inuse(self,row,col):
		try:
			if (self.board[row][col] != self.UNUSED):
				return True
			else:
				return False
		except Exception as e:
			print e
			return True # out-of-bounds cells are considered "in use", so we avoid handling these exceptions

	def play(self, symbol, col):
		if (self.freespaces == 0):
			print "BOARD IS FULL!"
			return False
		if (self.fourinarow):
                        print self.fourinarow
			return False # game is over, we won't allow more moves
		if (len(self.board[0]) <= col or col < 0):
			raise Exception("Column out of bounds");
		# Let's start at the "bottom" and work our way up
		for n in range(self.height-1, -1, -1):
			#print "Checking [" + str(col) + "][" + str(n) + "]"
			if (not self.inuse(n, col)): # this cell is free, let's add the symbol and return True
				self.board[n][col] = symbol
				# we have successfully placed the symbol, let's check for 4-in-a-row!
				self.checkinarow()
				self.freespaces -= 1 # let's keep track of free spaces
				return True
		return False

	def checkinarow(self):
                eval_value = self.evaluate()
		if (eval_value == 1.0):
			self.fourinarow = 'X'
		elif (eval_value == -1.0):
			self.fourinarow = 'O'

	def evaluate(self):
		max1 = 0
		last_value = 0
		current_value = 0
		try:
			# Fara yfir dálka 
			for j in range(self.height):
                                last_value = 0
                                current_value = 0 
				for i in range(self.width):   
					if (self.get_value(j,i) == last_value):
						current_value += self.get_value(j,i)
						max1 = self.get_maxvalue(current_value, max1)
					else:
						current_value = self.get_value(j,i)
						max1 = self.get_maxvalue(current_value, max1)
						last_value = current_value

			for i in range(self.width):
                                last_value = 0
                                current_value = 0 
				for j in range(self.height):
					if self.get_value(j,i) == last_value:
					    current_value += self.get_value(j,i)
					    max1 = self.get_maxvalue(current_value, max1)
					else:
					    current_value = self.get_value(j,i)
					    max1 = self.get_maxvalue(current_value, max1)
					    last_value = current_value
					#print 'j: ' + str(j) + ' i: ' + str(i) + ' current: ' + str(current_value) + ' last: ' + str(last_value) + ' cell value: ' + str(self.get_value(j,i)) + ' max1: ' + str(max1)

			# Check diagonal 
			for j in range(self.height):
				j_t = j
				i_t = 0
				last_value = 0
                                current_value = 0 
				while (j_t >= 0 and i_t < self.width):
					if self.get_value(j_t,i_t) == last_value:
					    current_value += self.get_value(j_t,i_t)
					    max1 = self.get_maxvalue(current_value, max1)
					else:
					    current_value = self.get_value(j_t,i_t)
					    max1 = self.get_maxvalue(current_value, max1)
					    last_value = current_value
					j_t -= 1
					i_t += 1
	        
			for i in range(self.width):
				j_t = self.height-1
				i_t = i
				last_value = 0
                                current_value = 0 
				while (j_t >= 0 and i_t < self.width):
					if self.get_value(j_t,i_t) == last_value:
					    current_value += self.get_value(j_t,i_t)
					    max1 = self.get_maxvalue(current_value, max1)
					else:
					    current_value = self.get_value(j_t,i_t)
					    max1 = self.get_maxvalue(current_value, max1)
					    last_value = current_value
					j_t -= 1
					i_t += 1
			
			for j in range(self.height):
				j_t = j
				i_t = self.width-1
				last_value = 0
                                current_value = 0 
				while (j_t >= 0 and i_t >= 0):
					if self.get_value(j_t,i_t) == last_value:
					    current_value += self.get_value(j_t,i_t)
					    max1 = self.get_maxvalue(current_value, max1)
					else:
					    current_value = self.get_value(j_t,i_t)
					    max1 = self.get_maxvalue(current_value, max1)
					    last_value = current_value
					j_t -= 1
					i_t -= 1       


			for i in range(self.width-1,-1,-1):
				j_t = self.height-1
				i_t = i
				last_value = 0
                                current_value = 0 
				while (j_t >= 0 and i_t >= 0):
					if self.get_value(j_t,i_t) == last_value:
					    current_value += self.get_value(j_t,i_t)
					    max1 = self.get_maxvalue(current_value, max1)
					else:
					    current_value = self.get_value(j_t,i_t)
					    max1 = self.get_maxvalue(current_value, max1)
					    last_value = current_value
					j_t -= 1
					i_t -= 1                
			return float(float(max1)/float(self.NTOWIN))

		except Exception as e:
			print 'evaluate:'
			print e    

	def get_value(self,row,col):
		if self.board[row][col] == 'X':
			return 1
		elif self.board[row][col] == 'O':
			return -1
		else:
			return 0

	def get_maxvalue(self, current_value, max1):
		try:
			if math.fabs(float(current_value)) > math.fabs(float(max1)):
			   return current_value
			else:
			   return max1
		except Exception as e:
			print 'get_maxvalue'
			print e


class computer:
	def __init__(self, board, difficulty = 3):
		self.difficulty = difficulty
		self.board = board

	def legal_moves(self):
		M = []
		for i in range(self.board.width):
			for j in range(self.board.height-1,-1,-1):
				if not self.board.inuse(j,i):
					L = [j, i]
					M.append(L)
					#print str(L[0])+','+str(L[1])
					break
		return M
 
	def play(self, symbol): #XXX: smá hax að þetta noti ekki board.play
		if (self.board.freespaces == 0): # ^ ^ ^
			print "BOARD IS FULL!"
			return False
		player_symbol = symbol
		v = []
		M = self.legal_moves()
		for L in (M):
			self.board[L[0]][L[1]] = player_symbol
			if symbol == 'X':
				symbol = 'O'
			else:
				symbol = 'X'
			v.append(self.minimax_value(player_symbol, symbol, self.difficulty))
			self.board[L[0]][L[1]] = self.board.UNUSED
		best_move = 0
		if player_symbol == 'X':
			best_move = max(v)
		else:
			best_move = min(v)
		
		for i in range(len(v)):
			move = v[i]
			print "move=" + str(M[i]) + " : " + str(i) + " einkunn: " + str(move)
		L = M[v.index(best_move)]
		#print "Computer (" + player_symbol + ") choosing move: " + str(L) + " (" + str(best_move) + ")"
		self.board.play(player_symbol, L[1])
	    
	def minimax_value(self, player_symbol, symbol, iterations):
		if iterations == 0:
			return self.board.evaluate()
		iterations -= 1
		v = []
		M = self.legal_moves()
		if len(M) == 0:
			return self.board.evaluate()
		for L in (M):
			self.board[L[0]][L[1]] = symbol
			multiplier = self.board.board_heatmap[L[0]][L[1]]
			print "column: " + str(L[1]) + " multiplier: " + str(multiplier)
			if symbol == 'X':
				symbol = 'O'
			else:
				symbol = 'X'
			mv = self.minimax_value(player_symbol, symbol, iterations)
			print "minimax value=" + str(mv) + " after multiplier=" + str(multiplier*mv)
			v.append(multiplier * mv)
			self.board[L[0]][L[1]] = self.board.UNUSED
		if player_symbol == 'X':
			return max(v)
		else:
			return min(v)
