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
				cr.set_source_rgb(random.random(), random.random(), random.random())
				cr.rectangle(startx, starty, slotw, sloth)
				cr.fill()
				starty += sloth+margin_px
			starty = margin_px
			startx += slotw+margin_px
