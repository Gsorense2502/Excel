#!/usr/bin/env python3

import wx

class MainWindow(wx.Frame):
    def __init__(self, parent, title):

        wx.Frame.__init__(self, parent, title=title, size=(-1,-1))

        # self.panel = wx.Panel(self, size=(-1,300))

        # buttons bar

        self.top_button_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.btn_left = wx.Button(self, -1, label="left")
        self.btn_right = wx.Button(self, -1, label="right")

        self.btn_left.Bind(wx.EVT_BUTTON, self.OnLeft)
        self.btn_right.Bind(wx.EVT_BUTTON, self.OnRight)

        self.top_button_sizer.Add(self.btn_left, 1, wx.EXPAND)
        self.top_button_sizer.Add(self.btn_right, 1, wx.EXPAND)

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.display_sizer = wx.BoxSizer(wx.VERTICAL)
        self.text_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.display_text = wx.StaticText(self, label="Push a button!")
        self.display_buttons_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.text_sizer.Add(self.display_text, 0, wx.ALIGN_CENTER, 5)
        self.display_sizer.Add(self.text_sizer, 1, wx.ALIGN_CENTER, 5)
        self.display_sizer.Add(self.display_buttons_sizer, 0, wx.EXPAND)

        self.sizer.Add(self.top_button_sizer, 0, wx.TOP | wx.EXPAND)
        # self.sizer.Add(self.panel)
        self.sizer.Add(self.display_sizer, 1, wx.EXPAND)

        self.SetSizerAndFit(self.sizer)
        self.Show()

    def OnLeft(self,e):
        # for child in self.display_buttons_sizer.GetChildren():
        #     child.Destroy()
        # ^ my attempt to "clear" causes a SegFault
        for child in self.display_buttons_sizer.GetChildren():
            child.Destroy()
        self.display_text.SetLabel("Hey lefty!")
        self.btn_hey = wx.Button(self, -1, label="Hey yourself lefty.")
        self.btn_whoa = wx.Button(self, -1, label="Whoa there lefty.")
        self.display_buttons_sizer.Add(self.btn_hey, 1, wx.EXPAND)
        self.display_buttons_sizer.Add(self.btn_whoa, 1, wx.EXPAND)

        self.sizer.Layout()

    def OnRight(self,e):
        # for child in self.display_buttons_sizer.GetChildren():
        #     child.Destroy()
        # ^ my attempt to "clear" causes a SegFault!
        self.display_text.SetLabel("Hey righty!")
        self.btn_hey = wx.Button(self, -1, label="Hey yourself righty.")
        self.btn_whoa = wx.Button(self, -1, label="Whoa there righty.")
        self.display_buttons_sizer.Add(self.btn_hey, 1, wx.EXPAND)
        self.display_buttons_sizer.Add(self.btn_whoa, 1, wx.EXPAND)

        self.sizer.Layout()

app = wx.App(False)
frame = MainWindow(None, "MWE")
app.MainLoop()