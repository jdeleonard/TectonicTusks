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
from DeleteRecipieFrame import *


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

        self.delete_recipie_panel = DeleteRecipiePanel(self)
        self.delete_recipie_panel.Hide()


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

        deleteRecipie = fileMenu.Append(wx.ID_ANY, "Delete Recipies", "")
        self.Bind(wx.EVT_MENU, self.onDeleteRecipieClick, deleteRecipie)

        quitItem = wx.MenuItem(fileMenu, wx.ID_EXIT, '&Quit')
        fileMenu.Append(quitItem)
        self.Bind(wx.EVT_MENU, self.OnQuit, quitItem)



        # 'Save' Dropdown in Menu
        saveMenu = wx.Menu()

        #updateItem = saveMenu.Append(wx.ID_ANY, "Save", "")
        #self.Bind(wx.EVT_MENU, self.onUpdateButton, updateItem)

        updateItem = saveMenu.Append(wx.ID_ANY, "Update Item Amount", "")
        self.Bind(wx.EVT_MENU, self.onUpdateButton, updateItem)

        saveForDayItem = saveMenu.Append(wx.ID_ANY, "Post Inventory for Day", "")
        self.Bind(wx.EVT_MENU, self.onSaveForDay, saveForDayItem)



        menubar.Append(fileMenu, '&File')
        menubar.Append(saveMenu, '&Save')

        self.SetMenuBar(menubar)

    def deleteItem(self, event):
        framer = deleteFrame(self)
        self.Show()

    # Function that calls updateFrame to open
    def onUpdateButton(self, event):
        framer = updateFrame(self)
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


    def onDeleteRecipieClick(self, event):
        deleteRecipieFrame = DeleteFrame(self)
        deleteRecipieFrame.Show()



    def onSaveForDay(self, event):
        conn = opendb("food.db")
        saveFoodForDay(conn)






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

# shows error message for incorrect IDs
def ShowMessage(self):
    wx.MessageBox('Not valid ID', 'Error',
        wx.OK | wx.ICON_INFORMATION)

# Update Frame Panel that prompts user to enter unique ID and amounts/expiration dates to be edited then calls UpdateButton function
# to edit database with user inputed values
class updateFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent=parent, title="Update Window", size=(300, 100))
        panel = wx.Panel(self)
        conn = opendb("food.db")
        temp = wx.TextEntryDialog(None, "Enter Update Item ID", "Update Options", "Item ID")
        #temp1 = wx.TextEntryDialog(None, "Enter new Amount", "Update", "Amount")
        if temp.ShowModal() == wx.ID_OK:
            updateID = temp.GetValue()
            check = checkID(conn, updateID)
            if checkID(conn, updateID) == 1:
                temp1 = wx.TextEntryDialog(None, "Enter new Amount", "Update", "New Amount")
                if temp1.ShowModal() == wx.ID_OK:
                    amount = temp1.GetValue()
                    temp2 = wx.TextEntryDialog(None, "Enter Expiration date changes:", "Exp. Update","New Expiration Date" )
                    if temp2.ShowModal() == wx.ID_OK:
                        exp = temp2.GetValue()
                        UpdateButton(conn, updateID, amount, exp)
                        self.Close(True)
                        self.GetParent().refreshGrid()
            else:
                print("error")
                ShowMessage(self)
        else:
            self.Close(True)


if __name__ == '__main__':

    addedFirstRecipie = False

    # Add Food Items To Order Screen
    InitializeRecipies.initializeRecipiesFromFile()

    # Validate Database File Exists
    checkForDatabase()

    app = wx.App()

    frame = MainForm()
    frame.Show()

    app.MainLoop()
