#!/usr/bin/env python
# ~!~ encoding: utf-8 ~!~
import game,wxgame,wx


class GUIDisconnect(wx.Frame):
	def __init__(self):
		"""Constructor"""
		wx.Frame.__init__(self, None, size=(600,450))

		self.SetBackgroundColour('white') # please change asap!!!

		afbrigdi = wx.ComboBox(self, -1, size=(125, -1), value="Afbrigdi",  pos=(10,10), choices= ['venjulegt', 'ofugt'], style=wx.CB_READONLY)
		size = wx.ComboBox(self, -1, size=(125, -1), value="Staerd bords", pos=(10,40), choices=['6x6', '4x4', 'custom'], style=wx.CB_READONLY)
		texti1 = wx.StaticText(self, -1, ("'rows' x 'cols'"), pos=(10, 70))
		#c_size = wx.TextCtrl(self, -1, ("m x n"))
		#skifur = wx.ComboBox(self, -1, size=(125, -1), value="Fjoldi skifa", pos=(10,10), choices= ['3', '4', 'custom'], style=wx.CB_READONLY)
		#texti2 = wx.StaticText(self, -1, ("Number of discs"), (10,10))
		#c_discs = wx.TextCtrl(self, -1, ("i"))
		#apply = wx.Button(self, -1, 'Apply', size=(100, -1))

		#self.Bind(wx.EVT_BUTTON, self.OnClickButtonPress, button) ### SVONA BIND-AR MAÐUR EVENTA VIÐ UI-COMPONENT/TAKKA? 

		self.board = game.board()
                self.gboard = wxgame.GraphicalBoard(self,self.board)
		self.panel = self.gboard
		# Create and position the main panel
		self.Center()

	def OnClickButtonPress(self, event):
		print "Button pressed!"

if __name__ == "__main__":
    app = wx.App(False)
    frame = GUIDisconnect()
    frame.Show()
    app.MainLoop()
