#!/usr/bin/env python
# ~!~ encoding: utf-8 ~!~
import wx
import wxgame
import game
import wx.lib.dialogs


class GUIDisconnect(wx.Frame):
	def __init__(self, parent, id, title):
		"""Constructor"""
		wx.Frame.__init__(self, parent, id, title, size=(600,450),)
		self.IN_GAME = 0 # THIS DEFAULTS TO 0

		self.SetBackgroundColour('#A32076') # please change asap!!!
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

		opponent_lable = wx.StaticText(self, -1, 'Andstæðingur', pos=(10, initpos))
		initpos += 17
		self.opponent = wx.ComboBox(self, -1, size=(125, -1), value='Mennskur', pos=(10,initpos), choices=['Mennskur', 'Tölva'], style=wx.CB_READONLY)
		initpos += 30
		start = wx.Button(self, -1, 'Spila', size=(100, -1), pos=(10, initpos))

		self.Bind(wx.EVT_BUTTON, self.new_game, start) ### SVONA BIND-AR MAÐUR EVENTA VIÐ UI-COMPONENT/TAKKA?

		

		# Create and position the main panel
		self.Center()
		
                # ---MENUBAR---
		START = 1
		APP_EXIT = 2
		ABOUT = 3
		HELP = 4

		menubar = wx.MenuBar()
		GameMenu = wx.Menu()
		
		NewGame_mi = wx.MenuItem(GameMenu, START, '&Nýr leikur\tCtrl+n') 
		quit_mi = wx.MenuItem(GameMenu, APP_EXIT, '&Hætta\tCtrl+Q')
		
		GameMenu.AppendItem(NewGame_mi)
		GameMenu.AppendItem(quit_mi)

		self.Bind(wx.EVT_MENU, self.new_game, id=START)
		self.Bind(wx.EVT_MENU, self.OnQuit, id=APP_EXIT)

		HelpMenu = wx.Menu()

		ViewHelp_mi = wx.MenuItem(HelpMenu, HELP, '&Sýna hjálp\tF1')
		About_mi = wx.MenuItem(HelpMenu, ABOUT, '&Um Disconnect')

		HelpMenu.AppendItem(ViewHelp_mi)
		HelpMenu.AppendItem(About_mi)

		self.Bind(wx.EVT_MENU, self.About, id=ABOUT)
		self.Bind(wx.EVT_MENU, self.ViewHelp, id=HELP)
		menubar.Append(GameMenu, '&Game')
		menubar.Append(HelpMenu, '&Help')
		self.SetMenuBar(menubar)
		
	def OnQuit(self, e):
		self.Close()	

	def ntowin(self):
		ntowin = int(self.skifur.GetValue())
		return ntowin

	def Against(self):
                Against = self.opponent.GetValue()
                return Against
                
	def new_game(self, event):      # --- teiknar mynd af nyju bordi yfir gamla, gamla sést ef stærd breytist.
		print "Stofna nýjan leik!"
		afbrigdi = self.afbrigdi.GetValue()
		print "afbrigdi=" + afbrigdi
		staerd = self.size.GetValue()
 		print "staerd=" + staerd
 		print self.Against()
		try:
			ntowin = self.ntowin()
		except:
			wx.MessageBox('Villa! Skífufjöldi þarf að vera heiltala!', 'Error', wx.OK | wx.ICON_INFORMATION)
			return
		print "ntowin=" + str(ntowin)
		if self.Against() == 'Mennskur':        # --- ekki alveg klár á hvort þetta sé besta leiðin
                        self.board = game.board(self.size.GetValue(), ntowin)
                        self.gboard = wxgame.GraphicalBoard(self, self.board, 2) # XXX: hardcode 2 players !
                        self.panel = self.gboard
                        self.IN_GAME = 1
                #if self.Against() == 'Tölva': TBD
                        # ---TBD---
                        
	def ViewHelp(self, event):
		h = open('help', 'r')
		msg = h.read()
		h.close()

		help_dialog = wx.lib.dialogs.ScrolledMessageDialog(self, msg, 'Disconnect - hjálp')
		help_dialog.ShowModal()
		help_dialog.Destroy()

	def About(self, e):
		description = """Disconnect er skemmtilegur leikur fyrir fólk á öllum aldri. En varaðu þig, þetta er algjör tímaþjófur."""

		info = wx.AboutDialogInfo()

		info.SetName('Disconnect')
		info.SetDescription(description)
		info.SetCopyright(' (C) 2012 The Gits')
		info.SetWebSite('github.com/gislifreyr/Disconnect')
		info.AddDeveloper('Björgvin Vilbergsson - bjv12@hi.is')
		info.AddDeveloper('Gísli Freyr Brynjarsson - gfb3@hi.is')
		info.AddDeveloper('Steinn E. Sigurðarson - ses@hi.is')

		wx.AboutBox(info)

def main():
	app = wx.App(False)
	frame = GUIDisconnect(None, -1, 'Disconnect')
	frame.Show()
	app.MainLoop()

if __name__ == '__main__':
	main()
