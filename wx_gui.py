import wx
import sys
from wx.lib.mixins.listctrl import CheckListCtrlMixin, ListCtrlAutoWidthMixin

packages = [('abiword', '5.8M', 'base'), ('adie', '145k', 'base'),
	('airsnort', '71k', 'base'), ('ara', '717k', 'base'), ('arc', '139k', 'base'),
	('asc', '5.8M', 'base'), ('ascii', '74k', 'base'), ('ash', '74k', 'base')]

class CheckListCtrl(wx.ListCtrl, CheckListCtrlMixin, ListCtrlAutoWidthMixin):
	def __init__(self, parent):
		wx.ListCtrl.__init__(self, parent, -1, style=wx.LC_REPORT | wx.SUNKEN_BORDER)
		CheckListCtrlMixin.__init__(self)
		ListCtrlAutoWidthMixin.__init__(self)


class Repository(wx.Frame):
	def __init__(self, parent, id, title):
		wx.Frame.__init__(self, parent, id, title, size=(600, 600))

		panel = wx.Panel(self, -1)

		vbox = wx.BoxSizer(wx.VERTICAL)
		hbox = wx.BoxSizer(wx.HORIZONTAL)

		leftPanel = wx.Panel(panel, -1)
		rightPanel = wx.Panel(panel, -1)

		self.log = wx.TextCtrl(rightPanel, -1, style=wx.TE_MULTILINE)
		self.list = CheckListCtrl(rightPanel)
		self.list.InsertColumn(0, 'Package', width=140)
		self.list.InsertColumn(1, 'Size')
		self.list.InsertColumn(2, 'Repository')

		for i in packages:
			index = self.list.InsertStringItem(sys.maxint, i[0])
			self.list.SetStringItem(index, 1, i[1])
			self.list.SetStringItem(index, 2, i[2])

		vbox2 = wx.BoxSizer(wx.VERTICAL)

		afbrigdi = wx.ComboBox(leftPanel, -1, size=(125, -1), value="Afbrigdi",  choices= ['venjulegt', 'ofugt'], style=wx.CB_READONLY)
		size = wx.ComboBox(leftPanel, -1, size=(125, -1), value="Staerd bords", choices=['6x6', '4x4', 'custom'], style=wx.CB_READONLY)
		texti1 = wx.StaticText(leftPanel, -1, ("'rows' x 'cols'"), (10,10))
		c_size = wx.TextCtrl(leftPanel, -1, ("m x n"))
		skifur = wx.ComboBox(leftPanel, -1, size=(125, -1), value="Fjoldi skifa", choices= ['3', '4', 'custom'], style=wx.CB_READONLY)
		texti2 = wx.StaticText(leftPanel, -1, ("Number of discs"), (10,10))
		c_discs = wx.TextCtrl(leftPanel, -1, ("i"))
		apply = wx.Button(leftPanel, -1, 'Apply', size=(100, -1))


		#self.Bind(wx.EVT_BUTTON, self.OnSelectAll, id=afbrigdi.GetId())
		#self.Bind(wx.EVT_BUTTON, self.OnDeselectAll, size.GetId())
		#self.Bind(wx.EVT_BUTTON, self.OnApply, id=apply.GetId())

		vbox2.Add(afbrigdi, 0, wx.TOP, 5)
		vbox2.Add(size)
		vbox2.Add(texti1)
		vbox2.Add(c_size)
		vbox2.Add(skifur)
		vbox2.Add(texti2)
		vbox2.Add(c_discs)
		vbox2.Add(apply)

		leftPanel.SetSizer(vbox2)

		vbox.Add(self.list, 1, wx.EXPAND | wx.TOP, 3)
		vbox.Add((-1, 10))
		vbox.Add(self.log, 0.5, wx.EXPAND)
		vbox.Add((-1, 10))

		rightPanel.SetSizer(vbox)

		hbox.Add(leftPanel, 0, wx.EXPAND | wx.RIGHT, 5)
		hbox.Add(rightPanel, 1, wx.EXPAND)
		hbox.Add((3, -1))

		panel.SetSizer(hbox)

		self.Centre()
		self.Show(True)

		def OnSelectAll(self, event):
			num = self.list.GetItemCount()
			for i in range(num):
				self.list.CheckItem(i)

		def OnDeselectAll(self, event):
			num = self.list.GetItemCount()
			for i in range(num):
				self.list.CheckItem(i, False)

		def OnApply(self, event):
			num = self.list.GetItemCount()
			for i in range(num):
				if i == 0: self.log.Clear()
				if self.list.IsChecked(i):
					self.log.AppendText(self.list.GetItemText(i) + '\n')

app = wx.App()
Repository(None, -1, 'Repository')
app.MainLoop()
