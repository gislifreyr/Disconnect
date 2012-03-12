#!/usr/bin/python -u
# ~!~ encoding: utf-8 ~!~
import wx,random

def withinbounds(b,c): # b = boundaries, c = click
	(bx1, by1, bx2, by2) = b
	(cx, cy) = c
	#print "Checking if cx=" + str(cx) + " is between (" + str(bx1) + "," + str(bx2) + ")"
	#print "Checking if cy=" + str(cy) + " is between (" + str(by1) + "," + str(by2) + ")"
	if (cx > bx1 and cx < bx2) and (cy > by1 and cy < by2):
		return True
	return False

class GraphicalBoard(wx.Panel):
	""""""
	def __init__(self, parent, board, nplayers):
		"""Constructor"""
		self.parent = parent
		(pwidth, pheight) = parent.GetSize()
		l_offset = 150
		t_offset = 60
		self.width = pwidth - l_offset
		self.height = pheight - t_offset - 50
		wx.Panel.__init__(self, parent=parent, size=(self.width,self.height), pos=(l_offset,t_offset))
		self.SetBackgroundStyle(wx.BG_STYLE_CUSTOM)
		self.frame = parent
		self.board = board # ATH: row / col
		self.board_slots = [] # ATH: col / row
		self.symbol_colors = {
			'X': (255,0,0),
			'O': (0,0,255),
			'Y': (0,255,0)
		}
		self.player_symbols = ['X','O','Y']
		self.curplayer = 0
		self.nplayers = nplayers

		# Keep track of mouse cursor
		self.pos=(0,0)
		self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)

		# Mouse events
		self.Bind(wx.EVT_LEFT_DOWN, self.OnLeftDown)
		self.Bind(wx.EVT_MOTION, self.OnMovement)

	def OnEraseBackground(self, evt):
		"""
		Draw the background
		"""
		dc = evt.GetDC()

		if not dc:
		    dc = wx.ClientDC(self)
		    rect = self.GetUpdateRegion().GetBox()
		    dc.SetClippingRect(rect)
		dc.Clear()

		width = self.width
		height = self.height
		bwidth = self.board.width;
                bheight = self.board.height;

		slotsize = min(width/bwidth, height/bheight)
		width = slotsize * bwidth
		height = slotsize * bheight

                margin_px = 10
                width -= margin_px
                height -= margin_px
                # let's calculate the dimensions of each of our disc-slots, based on this information
                # we'll have a 10px margin between slots
                slotw = (width - (margin_px * bwidth)) / bwidth;
                sloth = (height - (margin_px * bheight)) / bheight;
                #print "Slot width=" + str(slotw) + " height=" + str(sloth)
                (startx,starty) = (margin_px,margin_px)
		self.board_slots = []
                for col in range(bwidth):
			rows = []
                        for row in range(bheight):
                                dc.SetBrush(wx.Brush((150,150,150), wx.SOLID))
                                dc.DrawRectangle(startx, starty, slotw, sloth)
				dc.SetBrush(wx.Brush((255, 255, 255), wx.SOLID)) #teiknum tóman hring
				dc.DrawEllipse(startx, starty, slotw-1, sloth-1)
				rows.append((startx, starty, startx+slotw, starty+sloth))
				# let's draw a game symbol here
				try:
					dc.SetBrush(wx.Brush(self.symbol_colors[self.board.board[row][col]], wx.SOLID))
					dc.DrawEllipse(startx, starty, slotw-1, sloth-1)
				except:
					next # unused slot
                                starty += sloth+margin_px

                        starty = margin_px
                        startx += slotw+margin_px
			self.board_slots.append(rows)

		#print self.board_slots
		#print self.pos # debugging

	# Mouse click (left mouse)
	def OnLeftDown(self, event):
		if (self.parent.IN_GAME == 0):
			return
		pt = event.GetPosition() # position tuple
		self.pos = pt
		print "Mouse click at ", pt
		for c in range(len(self.board_slots)):
			col = self.board_slots[c]
			for r in range(len(col)):
				slot = col[r]
				if (withinbounds(slot, pt)):
					print "Adding game symbol to: row:" + str(r) + " / col:" + str(c)
					self.board.play(self.player_symbols[self.curplayer], c)
                                        if self.board.fourinarow == self.player_symbols[self.curplayer]:
                                                print 'four in a row'
                                                self.parent.IN_GAME = 0
                                                wx.MessageBox('Til hamingju tu vannst') #prentar ádur en hún teiknar disk.
                                                
					# --- eftir ad koma ntowin in í evaluate fallid (athugar bara 4 í röd) 
					# XXX: if player has won, use wx.MessageBox to congratulate player (how many moves?)
					self.curplayer += 1
					if (self.curplayer >= self.nplayers):
						self.curplayer = 0

		self.Refresh() # force a redraw of the panel
		# XXX: now curplayer is the next one, are we playing against a computer?
		#      ... where do we make the computer play?  Here? self.computer.play() ?
		# Muna að kalla þá aftur í self.Refresh() til að endurteikna skjáinn eftir að tölvan hefur gert


	def OnMovement(self, event):
		pt = event.GetPosition() # position tuple
		self.pos = pt # keep track of mouse movement
		self.Refresh()
