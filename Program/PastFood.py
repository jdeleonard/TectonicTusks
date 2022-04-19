import wx
import wx.grid as wxgrid
import datetime
from db_functions import *

# This is the new frame that pops up when 'Past Inventory' is selected in the menu.
class PastFoodFrame(wx.Frame):

    def __init__(self, parent):
        self.date = ""

        # Create the frame and show PastDatePanel First
        wx.Frame.__init__(self, parent, title = "Get Past Inventory", size = (700,700))
        self.past_date_panel = PastDatePanel(self)

        self.past_date_panel.Show()
        
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.past_date_panel, 1, wx.EXPAND)
        self.SetSizer(self.sizer)

    # Switches the panels so the grid now shows with the selected date
    def displayPastGrid(self, today):
        self.date = today
        self.past_date_panel.Hide()

        # Create and show the PastFoodPanel
        self.past_food_panel = PastFoodPanel(self)
        self.sizer.Add(self.past_food_panel, 1, wx.EXPAND)
        self.SetSizer(self.sizer)
        self.past_food_panel.Show()


# Panel that is the GUI for selecting which past date you want to look at
class PastDatePanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)

        dateLabel = wx.StaticText(self, -1, "Date: ")

        # Creation and population of the dropdown box
        conn = opendb("food.db")
        all_db_dates = getAllPastFoodDates(conn)
        allDates = []

        for line in all_db_dates:
            for item in line:
                allDates.append(item)

        self.combo = wx.ComboBox(self, value="--Date--", choices=allDates)


        button = wx.Button(self, label="Get Inventory", size=(100,50))
        self.Bind(wx.EVT_BUTTON, self.displayPast, button)

        sizer = wx.FlexGridSizer(cols=2, hgap=6, vgap=6)
        sizer.AddMany([dateLabel,self.combo,button])

        self.SetSizer(sizer)

    # Calls the function to display the grid
    def displayPast(self, event):
        date2 = self.combo.GetValue()
        self.GetParent().displayPastGrid(date2)


# Panel that holds the grid of the past food amounts
class PastFoodPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)
        pastGrid = PastFoodGrid(self)
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(pastGrid, 1)
        self.SetSizer(sizer)



# Grid that contains the past food amounts
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

            # Populate the cells
            for r in range(numRows):
                for c in range(4):
                    self.SetCellValue(r,c, str(rows[r][c]))

        else:
            errorLabel = wx.StaticText(self, -1, "No Posts found from {}".format(date))
