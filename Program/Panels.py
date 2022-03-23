import wx, sqlite3

from InventoryGrid import *

class PanelOne(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)
        #txt = wx.TextCtrl(self)
        myGrid = MyGrid(self)
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(myGrid, 1)
        self.SetSizer(sizer)


class PanelTwo(wx.Panel):

    def insertItem(self, event):

        conn = opendb("food.db")

        id = self.idText.GetValue()
        food = self.foodText.GetValue()
        unit = self.unitText.GetValue()
        edate = self.edateText.GetValue()

        if (id != ""):
            insertRow(conn, id, food, unit, edate)

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


        sizer = wx.FlexGridSizer(cols=2, hgap=6, vgap=6)
        sizer.AddMany([idLabel,self.idText,foodLabel,self.foodText,unitLabel,self.unitText,edateLabel,self.edateText])
    

        button = wx.Button(self, label="Add Item", size=(50,50))
        self.Bind(wx.EVT_BUTTON, self.insertItem, button)



        self.SetSizer(sizer)
