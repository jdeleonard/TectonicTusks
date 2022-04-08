import wx
import wx.grid as wxgrid
import datetime
from db_functions import *


class PastFoodFrame(wx.Frame):

    def __init__(self, parent):

        self.date = ""

        wx.Frame.__init__(self, parent, title = "Get Past Inventory", size = (700,700))
        self.past_date_panel = PastDatePanel(self)

        self.past_date_panel.Show()
        

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.past_date_panel, 1, wx.EXPAND)
        self.SetSizer(self.sizer)

    def displayPastGrid(self, today):
        self.date = today
        self.past_date_panel.Hide()

        # Create and show the PastFoodPanel
        self.past_food_panel = PastFoodPanel(self)
        self.sizer.Add(self.past_food_panel, 1, wx.EXPAND)
        self.SetSizer(self.sizer)
        self.past_food_panel.Show()



class PastDatePanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)

        dateLabel = wx.StaticText(self, -1, "Date: ")
        self.dateText = wx.TextCtrl(self, -1)

        button = wx.Button(self, label="Get Inventory", size=(100,50))
        self.Bind(wx.EVT_BUTTON, self.displayPast, button)

        sizer = wx.FlexGridSizer(cols=2, hgap=6, vgap=6)
        sizer.AddMany([dateLabel,self.dateText,button])

        self.SetSizer(sizer)

    def displayPast(self, event):
        date2 = self.dateText.GetValue()
        self.dateText.SetValue("")
        self.GetParent().displayPastGrid(date2)



class PastFoodPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)
        pastGrid = PastFoodGrid(self)
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(pastGrid, 1)
        self.SetSizer(sizer)




class PastFoodGrid(wxgrid.Grid):

    def __init__ (self, parent):

        wxgrid.Grid.__init__(self, parent)
        conn = opendb("food.db")
        date = self.GetParent().GetParent().date

        numRows = getNumOfRowsPastFood(conn, date)

        if (numRows > 0):
            
            rows = getAllRowsPastFood(conn, date)

            self.CreateGrid(numRows, 4)

            self.SetColLabelValue(0, "ID")
            self.SetColLabelValue(1, "Food")
            self.SetColLabelValue(2, "Amount")
            self.SetColLabelValue(3, "Date")

    
            for r in range(numRows):
                for c in range(4):
                    self.SetCellValue(r,c, str(rows[r][c]))

        else:
            errorLabel = wx.StaticText(self, -1, "No Posts found from {}".format(date))
