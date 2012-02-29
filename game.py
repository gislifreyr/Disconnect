# -*- coding: utf-8 -*-
import math

class board:
	def __init__(self, size='4x4', discs=4):
		self.size = size
		self.board = []
		self.UNUSED = '_'
		self.NTOWIN = discs
		self.fourinarow = None
		return self.init()
	def init(self):
		(h,w) = self.size.split('x')
		self.height = int(h)
		self.width = int(w)
		if (self.height < self.NTOWIN and self.width < self.NTOWIN):
			raise Exception("The number of discs-in-a-row to win, may not be greater than both board dimensions!")

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
				eval_value = math.fabs(self.evaluate())
				if (eval_value == 1.0):
					self.fourinarow = 'X'
				elif (eval_value == -1.0):
					self.fourinarow = 'O'
				return True
		return False

	def legal_moves(self):
		M = []
		for i in range(self.width):
			for j in range(self.height-1,-1,-1):
				if not self.inuse(j,i):
					L = []
					L.append(j)
					L.append(i)
					M.append(L)
					#print str(L[0])+','+str(L[1])
					break
		return M
 


	def computer_play(self, symbol):
		player_symbol = symbol
		v = []
		M = self.legal_moves()
		for L in (M):
			self.board[L[0]][L[1]] = player_symbol
			if symbol == 'X':
				symbol = 'O'
			else:
				symbol = 'X'
			v.append(self.minimax_value(player_symbol, symbol, 3))
			self.board[L[0]][L[1]] = self.UNUSED
		if player_symbol == 'X':
			L = M[v.index(max(v))]
			self.board[L[0]][L[1]] = player_symbol
		else:
			L = M[v.index(min(v))]
			self.board[L[0]][L[1]] = player_symbol
                eval_value = self.evaluate()
		if (eval_value == 1.0):
			self.fourinarow = 'X'
		elif (eval_value == -1.0):
			self.fourinarow = 'O'
	    

	def minimax_value(self, player_symbol, symbol, iterations):
		if iterations == 0:
			return self.evaluate()
		iterations -= 1
		v = []
		M = self.legal_moves()
		if len(M) == 0:
			return self.evaluate()
		for L in (M):
			self.board[L[0]][L[1]] = symbol
			if symbol == 'X':
				symbol = 'O'
			else:
				symbol = 'X'
			v.append(self.minimax_value(player_symbol, symbol, iterations))
			self.board[L[0]][L[1]] = self.UNUSED
		if player_symbol == 'X':
			return max(v)
		else:
			return min(v)
			
				


    

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
			print'get_maxvalue'
			print e
		

	
	def evaluate(self):
		max1 = 0
		last_value = 0
		current_value = 0
		try:
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

			return float(float(max1)/4.0)       
		except Exception as e:
			print'evaluate'
			print e    
	
	
	
