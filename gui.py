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
		self.connect("destroy", gtk.main_quit)
		# Sets the border width of the window.
		self.set_border_width(10)
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
