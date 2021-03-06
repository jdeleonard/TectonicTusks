import wx
import wx.grid as wxgrid
import sqlite3


import globals

from db_functions import *
from InventoryGrid import *
from Panels import *
from Frames import *
from OrderPanel import *
from PastFood import *
from Recipies import *
from InitializeRecipies import *
from AddRecipieFrame import *


from datetime import datetime
from datetime import date


class MainForm(wx.Frame):

    def __init__(self):

        wx.Frame.__init__(self, parent=None, title="Inventory Sheet", size=(1000,800))

        self.invent_panel = InventoryPanel(self)

        self.insert_panel = InsertionPanel(self)
        self.insert_panel.Hide()

        self.order_panel = OrderPanel(self)
        self.order_panel.Hide()

        self.add_recipie_panel  = AddRecipiePanel(self)
        self.add_recipie_panel.Hide()


        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.invent_panel, 1, wx.EXPAND)
        self.sizer.Add(self.insert_panel, 1, wx.EXPAND)
        self.sizer.Add(self.order_panel, 1, wx.EXPAND)
        self.SetSizer(self.sizer)


        # Menubar Creation
        menubar = wx.MenuBar()

        # 'File' Dropdwon in Menu
        fileMenu = wx.Menu()

        switchItem = fileMenu.Append(wx.ID_ANY, "Switch Panels", "")
        self.Bind(wx.EVT_MENU, self.onSwitchPanels, switchItem)

        insertItem = fileMenu.Append(wx.ID_ANY, "Insert New Item", "")
        self.Bind(wx.EVT_MENU, self.onInsertNewItem, insertItem)

        deleteItem = fileMenu.Append(wx.ID_ANY, "Delete Item", "")
        self.Bind(wx.EVT_MENU, self.deleteItem, deleteItem)

        orderItem = fileMenu.Append(wx.ID_ANY, "Take Orders", "")
        self.Bind(wx.EVT_MENU, self.takeOrders, orderItem)

        addRecipieItem = fileMenu.Append(wx.ID_ANY, "Add Recipies", "")
        self.Bind(wx.EVT_MENU, self.addRecipies, addRecipieItem)

        pastFoodItem = fileMenu.Append(wx.ID_ANY, "Past Inventory", "")
        self.Bind(wx.EVT_MENU, self.onPastFoodClick, pastFoodItem)

        quitItem = wx.MenuItem(fileMenu, wx.ID_EXIT, '&Quit')
        fileMenu.Append(quitItem)
        self.Bind(wx.EVT_MENU, self.OnQuit, quitItem)

        updateItem = fileMenu.Append(wx.ID_ANY, "update Database", "")
        self.Bind(wx.EVT_MENU, self.onUpdateButton, updateItem)



        # 'Save' Dropdown in Menu
        saveMenu = wx.Menu()

        saveForDayItem = saveMenu.Append(wx.ID_ANY, "Post Inventory for Day", "")
        self.Bind(wx.EVT_MENU, self.onSaveForDay, saveForDayItem)



        menubar.Append(fileMenu, '&File')
        menubar.Append(saveMenu, '&Save')

        self.SetMenuBar(menubar)

    def deleteItem(self, event):
        framer = deleteFrame(self)
        self.Show()

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

    def refreshGrid(self):
        self.invent_panel.Destroy()
        self.invent_panel = InventoryPanel(self)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.invent_panel, 1, wx.EXPAND)
        self.SetSizer(self.sizer)
        self.Layout()

    def onInsertNewItem(self, event):
        insertFrame = InsertionFrame(self)
        insertFrame.Show()


    def onPastFoodClick(self, event):
        pastFoodFrame = PastFoodFrame(self)
        pastFoodFrame.Show()

    def onSaveForDay(self, event):
        conn = opendb("food.db")
        saveFoodForDay(conn)

    def onUpdateButton(self, event):
        print("Button Read")
        conn = opendb("food.db")
        UpdateButton(conn)
        
        



    # Activates from clicking "Take Orders" on the file menu... file->Take Orders
    def takeOrders(self, event):
        orderFrame = OrderFrame(self)
        orderFrame.Show()


    def addRecipies(self, event):
        addFrame = AddRecipieFrame(self, "Add Recipies")
        addFrame.Show()





class deleteFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent=parent, title="Delete Window", size=(300, 100))
        panel = wx.Panel(self)
        conn = opendb("food.db")
        temp = wx.TextEntryDialog(None, "Enter Item ID to Delete:", "Delete Options", "Item ID")
        if temp.ShowModal() == wx.ID_OK:
            deleteID = temp.GetValue()
            deleteItemSQL(conn, deleteID)
            self.Close(True)
            self.GetParent().refreshGrid()

        else:
            self.Close(True)




if __name__ == '__main__':

    # Add Food Items To Order Screen
    InitializeRecipies.initializeRecipiesFromFile()

    app = wx.App()

    frame = MainForm()
    frame.Show()

    app.MainLoop()
