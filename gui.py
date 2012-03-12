#!/usr/bin/env python
# ~!~ encoding: utf-8 ~!~
import game,wxgame,wx


class GUIDisconnect(wx.Frame):
	def __init__(self):
		"""Constructor"""
		wx.Frame.__init__(self, None, size=(600,450))
		self.IN_GAME = 0 # THIS DEFAULTS TO 0

		self.SetBackgroundColour('white') # please change asap!!!
		initpos = 10;

		afbrigdi_label = wx.StaticText(self, -1, 'Afbrigði', pos=(10, initpos))
		initpos += 17
		self.afbrigdi = wx.ComboBox(self, -1, size=(125, -1), pos=(10, initpos), value='venjulegt', choices= ['venjulegt', 'öfugt'], style=wx.CB_READONLY)
		initpos += 30

		size_label = wx.StaticText(self, -1, "Stærð borðs", pos=(10, initpos))
		initpos += 17
		self.size = wx.ComboBox(self, -1, size=(125, -1), value="3x6", pos=(10,initpos), choices=['3x6', '6x7', '6x6', '4x4'], style=wx.CB_READONLY)
		initpos += 30

		skifu_label = wx.StaticText(self, -1, "Fjöldi skífa", pos=(10, initpos))
		initpos += 17
		self.skifur = wx.ComboBox(self, -1, size=(125, -1), value="4", pos=(10,initpos), choices= ['3', '4', 'custom'], style=wx.CB_READONLY)
		initpos += 30
		start = wx.Button(self, -1, 'Spila', size=(100, -1), pos=(10, initpos))

		self.Bind(wx.EVT_BUTTON, self.new_game, start) ### SVONA BIND-AR MAÐUR EVENTA VIÐ UI-COMPONENT/TAKKA? 

		# Create and position the main panel
		self.Center()

                APP_EXIT=1
		menubar = wx.MenuBar()
		fileMenu = wx.Menu()
		qmi = wx.MenuItem(fileMenu, APP_EXIT, '&Quit\tCtrl+Q')
		fileMenu.AppendItem(qmi)

		self.Bind(wx.EVT_MENU, self.OnQuit, id=APP_EXIT)

		menubar.Append(fileMenu, '&Game')
		self.SetMenuBar(menubar)
		
	def OnQuit(self, e):
                self.Close()	
                
	def new_game(self, event):
		print "Stofna nýjan leik!"
		print "afbrigdi=" + self.afbrigdi.GetValue()
		print "staerd=" + self.size.GetValue()
		print "ntowin=" + self.skifur.GetValue()
		self.board = game.board(self.size.GetValue())
		self.gboard = wxgame.GraphicalBoard(self, self.board, 2) # XXX: hardcode 2 players !
		self.panel = self.gboard
		self.IN_GAME = 1

if __name__ == "__main__":
    app = wx.App(False)
    frame = GUIDisconnect()
    frame.Show()
    app.MainLoop()
