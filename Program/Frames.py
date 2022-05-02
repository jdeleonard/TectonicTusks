import wx

from Panels import *
from MessageFrame import *


class InsertionFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, title="Insert New Item", size = (300,300))
        self.insert_panel = InsertionPanel(self)




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
                ShowMessage(self)
        else:
            self.Close(True)


# shows error message for incorrect IDs
def ShowMessage(self):
        wx.MessageBox('Not valid ID', 'Error',
            wx.OK | wx.ICON_INFORMATION)





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