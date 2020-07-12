import wx
import wx.adv
from DataFun import *
import docx
from docx import *
from wx.adv import CalendarCtrl, GenericCalendarCtrl, CalendarDateAttr

class HelloFrame(wx.Frame):
    """
    A Frame that says Hello World
    """
    
    ClientNames,date_time, FileV = OnStart()
    DigCode = GetCode('Diagnosis Codes.csv')
    TreatCode = GetCode('Treatment Codes.csv')

    

    
    

    




    def __init__(self, *args, **kw):


        
        # ensure the parent's __init__ is called
        super(HelloFrame, self).__init__(*args, **kw)
        
     


        # create a panel in the frame
        pnl = wx.Panel(self)

        self.SetSize(600,750)
        font = wx.Font(10, wx.SCRIPT, wx.NORMAL, wx.BOLD)

        fontforCode = wx.Font(7, wx.SCRIPT, wx.NORMAL, wx.BOLD)
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
 
        
        

       
        self.T2 = wx.StaticText(pnl, -1, self.date_time, (510, 45))
        self.T3 = wx.StaticText(pnl, -1, "Current Date", (500, 25))

        self.patients = wx.Choice(pnl,choices = self.ClientNames ,pos=(0, 250),size = (155,40))
        self.Dig = wx.Choice(pnl,choices = self.DigCode,pos=(0, 290) )
        self.Treat = wx.Choice(pnl,choices = self.TreatCode,pos=(0, 330) )

        #,size = (225,40)

        self.patients.SetFont(font)
        
        self.cal = wx.adv.CalendarCtrl(pnl,pos=(0, 355) , date = wx.DateTime.Now())
        self.cal.Hide()
        
        
        self.T2 = wx.StaticText(pnl, -1, self.date_time, (510, 45))
        self.T3 = wx.StaticText(pnl, -1, "Current Date", (500, 25))

        self.SessValue = wx.StaticText(pnl, -1, self.date_time, (310, 45))
        self.SessButton = wx.Button(pnl, -1, size = (100,40), pos =(310, 250),label = 'Session Calander')
        self.SessDate = wx.StaticText(pnl, -1, "Session Date", (300, 25))
        
        
        
        self.T3.SetFont(font)
        self.SessDate.SetFont(font)

        self.Bind(wx.EVT_BUTTON, self.SendText, self.Send)
        
        self.Bind(wx.EVT_BUTTON, self.GetSessDate, self.SessButton)
       

    def OnDate(self,event):


        datePicker = self.cal.GetDate()
        #sel_date = datePicker.GetValue()
        #y = datePicker.GetYear()
        #m = datePicker.getMonth()
        #d = datePicker.GetDay()
        dateFinal = datePicker.Format("%m/%d/%Y")

        #dateFinal = wx.DateTimeFromDMY(d,m,y)
        #datePicker.FormatISODate()
        dateFinal = str(dateFinal)

        self.SessValue.SetLabel(dateFinal) 


        
        
        self.cal.Hide()

    def SendText (self,event):
        Noted = self.T1.GetValue()
        patient = self.patients.GetStringSelection()
        NoteDate = self.date_time
        Path = self.FileV
        Treat = self.Treat.GetStringSelection()
        Dig = self.Dig.GetStringSelection()
        SessDate = self.SessValue.GetLabelText()
        
        SendForNotes(Noted,patient,NoteDate,Path,Treat,Dig,SessDate)

        wx.MessageBox("A note has been entered for " + patient + ".")
        self.T1.SetValue( '\n\n')
    def GetSessDate(self,event):
        self.cal.Show()
        
        
        self.hideSessDate(wx.adv.EVT_CALENDAR)


        #self.cal.Bind(wx.adv.EVT_CALENDAR, self.OnDate)
        #self.cal.Hide()
        

    def hideSessDate(self, event):
        self.cal.Bind(wx.adv.EVT_CALENDAR, self.OnDate)
        #self.cal.Hide()



    # def InitUI(self):

    #     pnl = wx.Panel(self)
        

    #     font = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)

    #     font.SetPointSize(7)

      

    #     # self.DigCodes = wx.Choice(pnl,choices = self.DigCode ,pos=(0, 250),size = (190,40))
    #     # self.DigCodes.SetFont(font)



    #     vbox = wx.BoxSizer(wx.HORIZONTAL)
    #     pnl.SetBackgroundColour('#4f5049')

    #     hbox1 = wx.BoxSizer(wx.VERTICAL)
    #     st1 = wx.Choice(pnl,choices = self.ClientNames)
    #     st1.SetFont(font)
    #     hbox1.Add(st1, 1,border=10, flag=wx.BOTTOM)

       
        
    #     vbox.Add(hbox1, flag=wx.BOTTOM, border=10)

    #     vbox.Add((0, 25))

    #     hbox2 = wx.BoxSizer(wx.VERTICAL)
    #     st2 = wx.Choice(pnl,choices = self.DigCode)
    #     st2.SetFont(font)
    #     hbox2.Add(st2, 1, flag=wx.BOTTOM )
    #     vbox.Add(hbox2, flag=wx.LEFT | wx.TOP, border=10)

    #     vbox.Add((35, 25))


    #     hbox3 = wx.BoxSizer(wx.VERTICAL)
    #     st3 = wx.Choice(pnl,choices = self.TreatCode)
    #     st3.SetFont(font)
    #     hbox3.Add(st3, 1, flag=wx.BOTTOM )
    #     vbox.Add(hbox1, flag=wx.BOTTOM, border=10)

    #     vbox.Add((55, 25))

    #     Texter = wx.BoxSizer(wx.HORIZONTAL)

    #     T1 = wx.TextCtrl(pnl,size = (575,160),style = wx.TE_MULTILINE)

    #     Texter.Add(T1, 1, flag=wx.CENTER )
    #     vbox.Add((60,125))

        
    #     #vbox.SetSizeHints(self)
        
    #     pnl.SetSizer(vbox)

        
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