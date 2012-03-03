#!/usr/bin/env python

# example helloworld.py

import pygtk
pygtk.require('2.0')
import gtk

# XXX: Modify GraphicalBoard object to draw a gameboard as we see fit!
class GraphicalBoard(gtk.DrawingArea):
    # Draw in response to an expose-event
    __gsignals__ = { "expose-event": "override" }
    # Handle the expose-event by drawing
    def do_expose_event(self, event):
        # Create the cairo context
        cr = self.window.cairo_create()
        # Restrict Cairo to the exposed area; avoid extra work
        cr.rectangle(event.area.x, event.area.y,
                event.area.width, event.area.height)
        cr.clip()
        self.draw(cr, *self.window.get_size())

    def draw(self, cr, width, height):
	print "Drawing on a window of width=" + str(width) + " and height=" + str(height)
        # Fill the background with gray
        cr.set_source_rgb(0.5, 0.5, 0.5)
        cr.rectangle(0, 0, width, height)
        cr.fill()

class GUIDisconnect(gtk.Window):
	# This is a callback function. The data arguments are ignored
	# in this example. More on callbacks below.
	def hello(self, widget, data=None):
		print "Hello World"

	def delete_event(self, widget, event, data=None):
		# If you return FALSE in the "delete_event" signal handler,
		# GTK will emit the "destroy" signal. Returning TRUE means
		# you don't want the window to be destroyed.
		# This is useful for popping up 'are you sure you want to quit?'
		# type dialogs.
		print "delete event occurred"

		# Change FALSE to TRUE and the main window will not be destroyed
		# with a "delete_event".
		return False

	def __init__(self):
		super(GUIDisconnect, self).__init__()
		# create a new window

		self.set_title("Disconnect")
		self.set_position(gtk.WIN_POS_CENTER)
		self.set_size_request(800,600)

		#menubar
		menubar = gtk.MenuBar()
		#menubar items
		filem = gtk.MenuItem("File")
		helpm = gtk.MenuItem("Help")
		#submenus
		filemenu = gtk.Menu()
		filem.set_submenu(filemenu)
		helpmenu = gtk.Menu()
		helpm.set_submenu(helpmenu)
		#add items in submenu
		quit = gtk.MenuItem("Quit")
		quit.connect("activate", gtk.main_quit)
		filemenu.append(quit)
		sos = gtk.MenuItem("View help")
		helpmenu.append(sos)
		about = gtk.MenuItem("About")
		helpmenu.append(about)

		menubar.append(filem)
		menubar.append(helpm)

		outer_container = gtk.VBox(False, 2)
		outer_container.pack_start(menubar, False, False, 0)


		self.afbrigdi = gtk.ComboBox()
		self.afbrigdi.append_text("Venjulegur")
		self.afbrigdi.append_text("Ofugt")

		self.button = gtk.Button("Hello World")
		self.button.connect("clicked", self.hello, None)

		self.quit = gtk.Button("Quit")
		self.quit.connect_object("clicked", gtk.Widget.destroy, self)

		inner_container= gtk.HBox(False, 2)
		buttonbox = gtk.VBox(False, 2);

		buttonbox.pack_start(self.afbrigdi, False, False, 0)
		buttonbox.pack_start(self.button);
		buttonbox.pack_start(self.quit);

		inner_container.pack_start(buttonbox, False, False, 0);
		# Create and add the gameboard
		self.board = GraphicalBoard()
		inner_container.pack_start(self.board);

		outer_container.pack_start(inner_container, True, True, 0)

		self.add(outer_container)

		self.connect("destroy", gtk.main_quit)
		# Creates a new button with the label "Hello World".
		# This packs the button into the window (a GTK container).
		self.show_all()

if __name__ == "__main__":
	g = GUIDisconnect()
	gtk.main()

