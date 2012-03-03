#!/usr/bin/env python

# example helloworld.py

import pygtk
pygtk.require('2.0')
import gtk

class HelloWorld(gtk.Window):
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
		super(HelloWorld, self).__init__()
		# create a new window

		self.set_title("Disconnect")
		self.set_size_request(1300, 850)
		self.set_position(gtk.WIN_POS_CENTER)

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

		menubox = gtk.VBox(False, 2)
		menubox.pack_start(menubar, False, False, 0)

		self.add(menubox)

		afbrigdi = gtk.ComboBox()
		afbrigdi.append_text("Venjulegur")
		afbrigdi.appenx_text("Ofugt")
		valbox = gtk.HBox(False, 2)
		valbox.pack_start(afbrigdi, False, False, 0)
		self.add(valbox)


		self.connect("destroy", gtk.main_quit)
		# Creates a new button with the label "Hello World".
		self.button = gtk.Button("Hello World")
		self.button.connect("clicked", self.hello, None)

		self.quit = gtk.Button("Quit")
		self.quit.connect_object("clicked", gtk.Widget.destroy, self)
		# This packs the button into the window (a GTK container).
		fix = gtk.Fixed()
		fix.put(self.button, 0, 0)
		fix.put(self.quit, 50, 50)
		self.add(fix)
		self.show_all()

# If the program is run directly or passed as an argument to the python
# interpreter then create a HelloWorld instance and show it
if __name__ == "__main__":
	hello = HelloWorld()
	gtk.main()
