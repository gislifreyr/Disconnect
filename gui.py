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
		self.IN_GAME = False
		self.HAS_COMPUTER = False
		self.computer = None

		self.SetBackgroundColour('#dddddd')
		initpos = 10;

		afbrigdi_label = wx.StaticText(self, -1, 'Afbrigði', pos=(10, initpos))
		initpos += 17
		self.afbrigdi = wx.ComboBox(self, -1, size=(125, -1), pos=(10, initpos), value='venjulegt', choices= ['venjulegt', 'öfugt'], style=wx.CB_READONLY)
		initpos += 30

		size_label = wx.StaticText(self, -1, "Stærð borðs", pos=(10, initpos))
		initpos += 17
		self.size = wx.ComboBox(self, -1, size=(125, -1), value="3x6", pos=(10,initpos), choices=['3x6', '6x7', '6x6', '4x4'])
		initpos += 30

		skifu_label = wx.StaticText(self, -1, "Fjöldi skífa", pos=(10, initpos))
		initpos += 17
		self.skifur = wx.ComboBox(self, -1, size=(125, -1), value="4", pos=(10,initpos), choices= ['3', '4'])
		initpos += 30

		opponent_label = wx.StaticText(self, -1, 'Andstæðingur', pos=(10, initpos))
		initpos += 17
		self.opponent = wx.ComboBox(self, -1, size=(125, -1), value='Mennskur', pos=(10,initpos), choices=['Mennskur', u'Tölva'], style=wx.CB_READONLY)

		# ef tölvan er valin sem andstæðingur, geta valið styrkleika
		initpos += 30
		self.computer_label = wx.StaticText(self, -1, "Erfiðleikastig", pos=(10, initpos))
		self.computer_label.Hide()
		initpos += 17
		self.computer_difficulty = wx.ComboBox(self, -1, size=(125, -1), value="4", pos=(10,initpos), choices= ['1', '2', '3', '4', '5'])
		self.computer_difficulty.Hide()
		self.Bind(wx.EVT_COMBOBOX, self.showhidecomputer, self.opponent)

		initpos += 60
		start = wx.Button(self, -1, 'Spila', size=(100, -1), pos=(10, initpos))

		self.Bind(wx.EVT_BUTTON, self.new_game, start) ### SVONA BIND-AR MAÐUR EVENTA VIÐ UI-COMPONENT/TAKKA?

		initpos += 40
		hveraleik_label = wx.StaticText(self, -1, "Hver á leik?", pos=(10, initpos))
		initpos +=  17
		self.nextplayer_label = wx.StaticText(self, -1, "enginn!?", pos=(10, initpos))
		self.nextplayer_label.Hide()

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

	def showhidecomputer(self, evt):
		opponent = self.Against()
		if (opponent == u'Tölva'):
			self.computer_label.Show()
			self.computer_difficulty.Show()
		else:
			self.computer_label.Hide()
			self.computer_difficulty.Hide()

	def Computer(self, symbol): # this method causes the computer to play
		assert(self.HAS_COMPUTER is not False)
		assert(self.computer is not None)
		self.update_nextplayer(str(self.gboard.curplayer+1) + " (tölvan!)") # smá hax að kalla svona inní self.gboard.curplayer....
		self.computer.play(symbol)

	def update_nextplayer(self, nplayer):
		if (self.IN_GAME):
			self.nextplayer_label.SetLabel('Spilari ' + str(nplayer))
			self.nextplayer_label.Show()
		else:
			self.nextplayer_label.Hide()

	def OnQuit(self, e):
		self.Close()	

	def ntowin(self):
		ntowin = self.skifur.GetValue()
		try:
			ntowin = int(ntowin)
			return ntowin
		except:
			wx.MessageBox('Villa! Skífufjöldi þarf að vera heiltala!', 'Error', wx.OK | wx.ICON_INFORMATION)
		return 0

	def boardSize(self):
		s = self.size.GetValue()
		try:
			(h,w) = s.split('x')
			int(h)
			int(w)
			return s
		except:
			wx.MessageBox("Úpps! Stærð þarf að vera á sniðinu AxB þar sem A og B eru heiltölur!")
		return False

	def Difficulty(self):
		d = self.computer_difficulty.GetValue()
		try:
			return int(d)
		except:
			wx.MessageBox("Úpps! Erfiðleikastig þarf að vera heiltala!", 'Error', wx.OK | wx.ICON_INFORMATION)

		return 0

	def Against(self):
                Against = self.opponent.GetValue()
                return Against

	def afbrigdi_to_gm(self, afbrigdi):
		a2gm = {u'venjulegt': 'normal', u'öfugt': 'reversed'} # unicode support í python er ljótt hax
		try:
			return a2gm[afbrigdi.lower()]
		except:
			wx.MessageBox("Exception! Gallað afbrigði valið?");
		return "error"
                
	def new_game(self, event):      # --- teiknar mynd af nyju bordi yfir gamla, gamla sést ef stærd breytist.
		print "Stofna nýjan leik!"
		afbrigdi = self.afbrigdi.GetValue()
		staerd = self.boardSize()
		assert(staerd != False)
 		print self.Against()
		ntowin = self.ntowin()
		assert(ntowin > 0)
		print "ntowin=" + str(ntowin)
		if self.Against() == 'Mennskur':        # --- ekki alveg klár á hvort þetta sé besta leiðin | ses: jamm, þetta er ekki fallegt en sleppur :-)
                        self.board = game.board(self.size.GetValue(), ntowin) 
                        self.gboard = wxgame.GraphicalBoard(self, self.board, 2) # XXX: hardcoding 2 players !
                        self.panel = self.gboard
                        self.IN_GAME = True
                if self.Against() == u'Tölva': # XXX: Erfiðleikastig?
			difficulty = self.Difficulty()
			assert(difficulty > 0)
			self.HAS_COMPUTER = True
                        self.board = game.board(self.size.GetValue(), ntowin) 
                        self.gboard = wxgame.GraphicalBoard(self, self.board, 2) # XXX: hardcoding 2 players !
			self.gboard.computer = True
			self.gboard.computer_cb = self.Computer
			self.computer = game.computer(self.board, difficulty) # XXX: hardcoded difficulty = 3 (same as in constructor of game.computer)
                        self.IN_GAME = True

		self.update_nextplayer(1) # spilari 1 á að gera í upphafi !
		self.gboard.game_mode = self.afbrigdi_to_gm(afbrigdi)
                        
	def ViewHelp(self, event):
		msg = file('help').read()

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
