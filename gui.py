#!/usr/bin/env python

# example helloworld.py

import pygtk
pygtk.require('2.0')
import gtk
import game


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
		self.board = game.board()
		self.gboard = game.GraphicalBoard(self.board)
		inner_container.pack_start(self.gboard);

		outer_container.pack_start(inner_container, True, True, 0)

		self.add(outer_container)

		self.connect("destroy", gtk.main_quit)
		# Creates a new button with the label "Hello World".
		# This packs the button into the window (a GTK container).
		self.show_all()

if __name__ == "__main__":
	g = GUIDisconnect()
	gtk.main()

