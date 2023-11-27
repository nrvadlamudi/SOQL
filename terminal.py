# Create command line interface (CLI) 

import sys
import wx
import obfuscator

class Terminal(wx.Frame):
    def __init__(self, parent, title):
        super(Terminal, self).__init__(parent, title=title, size=(400, 300))
        self.InitUI()
        self.Centre()
        self.Show()

    def InitUI(self):
        panel = wx.Panel(self)
        font = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)
        font.SetPointSize(9)

        vbox = wx.BoxSizer(wx.VERTICAL)

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        self.lbl = wx.StaticText(panel, label='Enter something: ')
        hbox1.Add(self.lbl, flag=wx.RIGHT, border=8)
        self.txt = wx.TextCtrl(panel)
        hbox1.Add(self.txt, proportion=1)
        vbox.Add(hbox1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

        vbox.Add((-1, 10))

        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        btn1 = wx.Button(panel, label='Ok', size=(70, 30))
        hbox2.Add(btn1)
        btn2 = wx.Button(panel, label='Close', size=(70, 30))
        hbox2.Add(btn2, flag=wx.LEFT|wx.BOTTOM, border=5)
        vbox.Add(hbox2, flag=wx.ALIGN_RIGHT|wx.RIGHT, border=10)

        # Add text output to bottom of window
        vbox.Add((-1, 10))
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        self.lbl2 = wx.StaticText(panel, label='Output: ')
        hbox3.Add(self.lbl2, flag=wx.RIGHT, border=8)
        self.txt2 = wx.TextCtrl(panel, style=wx.TE_READONLY)
        hbox3.Add(self.txt2, proportion=1)
        vbox.Add(hbox3, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

        panel.SetSizer(vbox)

        btn1.Bind(wx.EVT_BUTTON, self.OnSubmit)
        btn2.Bind(wx.EVT_BUTTON, self.OnClose)

    def OnSubmit(self, e):
        user_input = self.txt.GetValue()
        user_input = obfuscator.ManipulateInput(user_input)
        self.txt2.SetValue(user_input)

    def OnClose(self, e):
        self.Close(True)

if __name__ == '__main__':
    app = wx.App()
    Terminal(None, title='Terminal')
    app.MainLoop()

