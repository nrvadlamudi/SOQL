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
        self.lbl = wx.StaticText(panel, label="Enter a SQL query: ")
        hbox1.Add(self.lbl, flag=wx.RIGHT, border=8)
        self.txt = wx.TextCtrl(panel)
        hbox1.Add(self.txt, proportion=1)
        vbox.Add(hbox1, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

        vbox.Add((-1, 10))

        # Create dropdown menu
        hbox5 = wx.BoxSizer(wx.HORIZONTAL)
        self.lbl3 = wx.StaticText(panel, label="Select an obfuscation technique: ")
        hbox5.Add(self.lbl3, flag=wx.RIGHT, border=8)
        self.drp = wx.Choice(
            panel,
            choices=[
                "Inline Comment",
                "Double URL Encoding",
                "Invalid Percent Encoding",
                "Nesting Expressions",
                "Buffer Overflow",
            ],
        )
        hbox5.Add(self.drp, proportion=1)
        vbox.Add(hbox5, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

        vbox.Add((-1, 10))

        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        btn1 = wx.Button(panel, label="Ok", size=(70, 30))
        hbox2.Add(btn1)
        btn2 = wx.Button(panel, label="Close", size=(70, 30))
        hbox2.Add(btn2, flag=wx.LEFT | wx.BOTTOM, border=5)
        vbox.Add(hbox2, flag=wx.ALIGN_RIGHT | wx.RIGHT, border=10)

        # Add text output to bottom of window
        vbox.Add((-1, 10))
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        self.lbl2 = wx.StaticText(panel, label="Output: ")
        hbox3.Add(self.lbl2, flag=wx.RIGHT, border=8)
        self.txt2 = wx.TextCtrl(panel, style=wx.TE_READONLY)
        hbox3.Add(self.txt2, proportion=1)
        vbox.Add(hbox3, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

        panel.SetSizer(vbox)

        # add Copy to Clipboard button
        vbox.Add((-1, 10))
        hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        btn3 = wx.Button(panel, label="Copy to Clipboard", size=(150, 30))
        hbox4.Add(btn3)
        vbox.Add(hbox4, flag=wx.ALIGN_RIGHT | wx.RIGHT, border=10)

        btn1.Bind(wx.EVT_BUTTON, self.OnSubmit)
        btn2.Bind(wx.EVT_BUTTON, self.OnClose)
        btn3.Bind(wx.EVT_BUTTON, self.OnCopy)
        self.drp.Bind(wx.EVT_CHOICE, self.OnChoice)

    def OnSubmit(self, e):
        user_input = self.txt.GetValue()
        user_choice = self.drp.GetString(self.drp.GetSelection())
        if user_choice == "Inline Comment":
            user_input = obfuscator.ManipulateInput_Inline(user_input)
        elif user_choice == "Double URL Encoding":
            user_input = obfuscator.ManipulateInput_URL(user_input)
        elif user_choice == "Invalid Percent Encoding":
            user_input = obfuscator.ManipulateInput_Percent(user_input)
        elif user_choice == "Nesting Expressions":
            user_input = obfuscator.ManipulateInput_Nesting(user_input)
        elif user_choice == "Buffer Overflow":
            user_input = obfuscator.ManipulateInput_Overflow(user_input)
        self.txt2.SetValue(user_input)

    def OnClose(self, e):
        self.Close(True)

    def OnCopy(self, e):
        if wx.TheClipboard.Open():
            wx.TheClipboard.SetData(wx.TextDataObject(self.txt2.GetValue()))
            wx.TheClipboard.Close()

    def OnChoice(self, e):
        choice = self.drp.GetString(self.drp.GetSelection())


if __name__ == "__main__":
    app = wx.App()
    Terminal(None, title="SQL Obfuscator")
    app.MainLoop()
