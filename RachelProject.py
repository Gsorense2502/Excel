import wx
import wx.adv
import pandas as pd
from DataFun import *
from datetime import datetime
import docx
from docx import *

class HelloFrame(wx.Frame):
    """
    A Frame that says Hello World
    """
    
    PepsData =  pd.DataFrame(pd.read_csv("C:\\Users\\gsorensen\\Documents\\JS\\New folder\\MasterList.csv"))
    FileV = "C:\\Users\\gsorensen\\Documents\\JS\\New folder"
    PepsDataUpdated = GetVaildClients(PepsData)
    ClientNames = GetNames(PepsDataUpdated)
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y")

    

    
    

    




    def __init__(self, *args, **kw):


        
        # ensure the parent's __init__ is called
        super(HelloFrame, self).__init__(*args, **kw)

        # create a panel in the frame
        pnl = wx.Panel(self)

        self.SetSize(600,400)
        font = wx.Font(10, wx.SCRIPT, wx.NORMAL, wx.BOLD)
        # put some text with a larger bold font on it
        st = wx.StaticText(pnl, label="Notes")
        
        #font = font.Bold()
        st.SetFont(font)

        # and create a sizer to manage the layout of child widgets
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(st, wx.SizerFlags().Border(wx.TOP|wx.LEFT, 25))
        pnl.SetSizer(sizer)

        # create a menu bar
        self.makeMenuBar()

        

        
        # and a status bar
        self.CreateStatusBar()
        self.SetStatusText("Therapy Notes")


        self.Send = wx.Button(pnl,pos=(450, 250),size = (100,40),label = 'Run')
        self.T1 = wx.TextCtrl(pnl,pos=(2, 65),size = (575,160),style = wx.TE_MULTILINE)
        self.patients = wx.Choice(pnl,choices = self.ClientNames ,pos=(250, 250),size = (155,40))
        self.patients.SetFont(font)
        #self.cal = wx.adv.CalendarCtrl(pnl,pos=(0, 170) , date = wx.DateTime.Now())
        #self.cal.Bind(wx.adv.EVT_CALENDAR, self.OnDate)
        self.T2 = wx.StaticText(pnl, -1, self.date_time, (510, 45))
        self.T3 = wx.StaticText(pnl, -1, "Current Date", (500, 25))
        
        self.T3.SetFont(font)
        self.Bind(wx.EVT_BUTTON, self.SendText, self.Send)

    def OnDate(self,event):
        print(self.cal.GetDate())

    def SendText (self,event):
        Noted = self.T1.GetValue()
        patient = self.patients.GetStringSelection()
        NoteDate = self.date_time
        Path = self.FileV
        
        SendForNotes(Noted,patient,NoteDate,Path)

        wx.MessageBox("A note has been entered for " + patient + ".")
        self.T1.SetValue( '\n\n')
        


        
    def makeMenuBar(self):
        """
        A menu bar is composed of menus, which are composed of menu items.
        This method builds a set of menus and binds handlers to be called
        when the menu item is selected.
        """

        # Make a file menu with Hello and Exit items
        fileMenu = wx.Menu()
        # The "\t..." syntax defines an accelerator key that also triggers
        # the same event
        helloItem = fileMenu.Append(-1, "&Add a Patient...\tCtrl-P",
                "Help string shown in status bar for this menu item")
        fileMenu.AppendSeparator()
        # When using a stock ID we don't need to specify the menu item's
        # label
        exitItem = fileMenu.Append(wx.ID_EXIT)

        # Now a help menu for the about item
        helpMenu = wx.Menu()
        aboutItem = helpMenu.Append(wx.ID_ABOUT)

        # Make the menu bar and add the two menus to it. The '&' defines
        # that the next letter is the "mnemonic" for the menu item. On the
        # platforms that support it those letters are underlined and can be
        # triggered from the keyboard.
        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, "&File")
        menuBar.Append(helpMenu, "&Help")

        # Give the menu bar to the frame
        self.SetMenuBar(menuBar)

        # Finally, associate a handler function with the EVT_MENU event for
        # each of the menu items. That means that when that menu item is
        # activated then the associated handler function will be called.
        self.Bind(wx.EVT_MENU, self.OnHello, helloItem)
        self.Bind(wx.EVT_MENU, self.OnExit,  exitItem)
        self.Bind(wx.EVT_MENU, self.OnAbout, aboutItem)


    def OnExit(self, event):
        """Close the frame, terminating the application."""
        self.Close(True)

    



    def OnHello(self, event):
        MessageBox('Wow')
    #     """Say hello to the user."""
    #     class AddPeeps(wx.Frame):
    #           def __init__(self, *args, **kw):


        
    #     # ensure the parent's __init__ is called
    #             super(AddPeeps, self).__init__(*args, **kw)

    #             pnl = wx.Panel(self)

    #             self.SetSize(600,400)
    # if __name__ == '__main__':
    # # When this module is run (not imported) then create the app, the
    # # frame, show it, and start the event loop.
    #     app = wx.App()
    #     frm = AddPeeps(None, title='Add Partipants')
    #     frm.Show()
    #     app.MainLoop()



    def OnAbout(self, event):
        """Display an About Dialog"""
        wx.MessageBox("This is a wxPython Hello World sample",
                      "About Hello World 2",
                      wx.OK|wx.ICON_INFORMATION)


if __name__ == '__main__':
    # When this module is run (not imported) then create the app, the
    # frame, show it, and start the event loop.
    app = wx.App()
    frm = HelloFrame(None, title='Therapy Notes')
    frm.Show()
    app.MainLoop()