import wx
import wx.grid as wxgrid
import sqlite3

import globals

from db_functions import *
from InventoryGrid import *
from Panels import *



class MainForm(wx.Frame):

    def OnQuit(self, e):
        self.Close()
    
    def onSwitchPanels(self, event):
        if self.invent_panel.IsShown():
            self.SetTitle("Insert New Item")
            self.invent_panel.Hide()
            self.insert_panel.Show()
        else:
            self.SetTitle("Inventory Sheet")

            # Essentially a Refresh of the Panel -- shows updated database table
            self.invent_panel.Destroy()
            self.invent_panel = InventoryPanel(self)
            self.sizer = wx.BoxSizer(wx.VERTICAL)
            self.sizer.Add(self.invent_panel, 1, wx.EXPAND)
            self.SetSizer(self.sizer)

            self.invent_panel.Show()
            self.insert_panel.Hide()

        self.Layout()
        

    def __init__(self):

        wx.Frame.__init__(self, parent=None, title="Inventory Sheet", size=(1000,800))

        self.invent_panel = InventoryPanel(self)
        self.insert_panel = InsertionPanel(self)
        
        self.insert_panel.Hide()


        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.invent_panel, 1, wx.EXPAND)
        self.sizer.Add(self.insert_panel, 1, wx.EXPAND)
        self.SetSizer(self.sizer)


        # Menubar Creation
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()

        switchItem = fileMenu.Append(wx.ID_ANY, "Switch Panels", "")
        self.Bind(wx.EVT_MENU, self.onSwitchPanels, switchItem)

    
        quitItem = wx.MenuItem(fileMenu, wx.ID_EXIT, '&Quit')
        fileMenu.Append(quitItem)

        self.Bind(wx.EVT_MENU, self.OnQuit, quitItem)

        menubar.Append(fileMenu, '&File')

        self.SetMenuBar(menubar)


if __name__ == '__main__':

    app = wx.App()

    frame = MainForm()
    frame.Show()

    app.MainLoop()
