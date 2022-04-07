import wx, sqlite3

from InventoryGrid import *

class InventoryPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)
        myGrid = InventoryGrid(self)
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(myGrid, 1)
        self.SetSizer(sizer)


class InsertionPanel(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)

        idLabel = wx.StaticText(self, -1, "ID: ")
        self.idText = wx.TextCtrl(self, -1)

        foodLabel = wx.StaticText(self, -1, "Food Name: ")
        self.foodText = wx.TextCtrl(self, -1)

        unitLabel = wx.StaticText(self, -1, "Unit: ")
        self.unitText = wx.TextCtrl(self, -1)

        edateLabel = wx.StaticText(self, -1, "Expiration Date: ")
        self.edateText = wx.TextCtrl(self, -1)

        button = wx.Button(self, label="Add Item", size=(75,75))
        self.Bind(wx.EVT_BUTTON, self.insertItem, button)

        sizer = wx.FlexGridSizer(cols=2, hgap=6, vgap=6)
        sizer.AddMany([idLabel,self.idText,foodLabel,self.foodText,unitLabel,self.unitText,edateLabel,self.edateText, button])

        self.SetSizer(sizer)


    def insertItem(self, event):

        conn = opendb("food.db")

        id = self.idText.GetValue()
        food = self.foodText.GetValue()
        unit = self.unitText.GetValue()
        edate = self.edateText.GetValue()

        self.idText.SetValue("")
        self.foodText.SetValue("")
        self.unitText.SetValue("")
        self.edateText.SetValue("")

        if (id != ""):
            insertRow(conn, id, food, unit, edate)

        self.GetParent().GetParent().refreshGrid()
