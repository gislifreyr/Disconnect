#!/usr/bin/python -u
import wx,random

class GraphicalBoard(wx.Panel):
	""""""
	def __init__(self, parent, board):
		"""Constructor"""
		wx.Panel.__init__(self, parent=parent, size=(400,350), pos=(120,60))
		self.SetBackgroundStyle(wx.BG_STYLE_CUSTOM)
		self.frame = parent
		self.board = board

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

		width = 400 # XXX: make dynamic: self.GetUpdateRegion.GetBox().width ????
		height = 350 # XXX: make dynamic: self.GetUpdateRegion.GetBox().height ????
		# Background rectangle
		#ytop = 68
		#height = 200
		#dc.SetBrush(wx.Brush((0, 0, 100), wx.SOLID))
		#dc.DrawRectangle(60, ytop, 300, height)
		# Track the mouse cursor with a circle
		#dc.SetBrush(wx.Brush((200, 0, 0), wx.SOLID))
		#dc.DrawCircle(self.pos[0], self.pos[1], 50)
                bwidth = self.board.width;
                bheight = self.board.height;
                margin_px = 10
                width -= margin_px
                height -= margin_px
                # let's calculate the dimensions of each of our disc-slots, based on this information
                # we'll have a 10px margin between slots
                slotw = (width - (margin_px * bwidth)) / bwidth;
                sloth = (height - (margin_px * bheight)) / bheight;
                print "Slot width=" + str(slotw) + " height=" + str(sloth)
                (startx,starty) = (margin_px,margin_px)
                for row in range(bwidth):
                        for col in range(bheight):
                                dc.SetBrush(wx.Brush((random.randrange(0,255), random.randrange(0,255), random.randrange(0,255)), wx.SOLID))
                                dc.DrawRectangle(startx, starty, slotw, sloth)
                                starty += sloth+margin_px
                        starty = margin_px
                        startx += slotw+margin_px

		print self.pos # debugging

	def OnLeftDown(self, event):
		pt = event.GetPosition() # position tuple
		self.pos = pt
		print "Mouse click at ", pt
		self.Refresh() # force a redraw of the panel


	def OnMovement(self, event):
		pt = event.GetPosition() # position tuple
		self.pos = pt # keep track of mouse movement
		self.Refresh()
