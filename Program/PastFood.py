import wx
import wx.grid as wxgrid
import datetime
from db_functions import *

def calculateChange(prevDay, curDay):
    prevDay = float(prevDay)
    curDay = float(curDay)

    if (prevDay != 0):
        percent = (((prevDay - curDay) / prevDay) * 100) * -1
    elif (prevDay == 0 and curDay == 0):
        percent = 0
    else:
        percent = 100

    return float(f'{percent:.2f}')


class PastFoodFrame(wx.Frame):

    def __init__(self, parent):

        self.date = ""

        wx.Frame.__init__(self, parent, title = "Get Past Inventory", size = (625,300))
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
        self.Layout()



class PastDatePanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)

        dateLabel = wx.StaticText(self, -1, "Date: ")

        conn = opendb("food.db")
        all_db_dates = getAllPastFoodDates(conn)
        allDates = []
        
        for line in all_db_dates:
            for item in line:
                allDates.append(item)
        

        self.combo = wx.ComboBox(self, value="--Date--", choices=allDates )

        button = wx.Button(self, label="Get Inventory", size=(100,50))
        self.Bind(wx.EVT_BUTTON, self.displayPast, button)

        sizer = wx.FlexGridSizer(cols=2, hgap=6, vgap=6)
        sizer.AddMany([dateLabel,self.combo,button])

        self.SetSizer(sizer)

    def displayPast(self, event):
        date2 = self.combo.GetValue()
        self.GetParent().displayPastGrid(date2)



class PastFoodPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)
        pastGrid = PastFoodGrid(self)
        sizer = wx.BoxSizer(wx.VERTICAL)

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

            self.CreateGrid(numRows, 5)

            self.SetColLabelValue(0, "ID")
            self.SetColLabelValue(1, "Food")
            self.SetColLabelValue(2, "Amount")
            self.SetColLabelValue(3, "Date")
            self.SetColLabelValue(4, "% Difference - Then vs. Current Day")
            self.SetColSize(4,220)


            currentFood = getAllRows(conn)
            comparedFood = getAllRowsPastFood(conn, date)

            matching = []

            for cur in currentFood:
                for prev in comparedFood:
                    if (cur[0] == prev[0]):
                        matching.append(calculateChange(prev[2], cur[2]))
    
            for r in range(numRows):
                for c in range(5):
                    if (c < 4):
                        self.SetCellValue(r,c, str(rows[r][c]))
                    elif (len(matching) > 0 and r < len(matching)):
                        percentNum = matching[r]
                        if (percentNum > 0):
                            percentString = "+" + str(percentNum) + "%"
                            self.SetCellTextColour(r,c,"green")

                        elif(percentNum == 0):
                            percentString = "0.0%"

                        else:
                            percentString = str(percentNum) + "%"
                            self.SetCellTextColour(r,c,"red")


                        self.SetCellValue(r,c, percentString)
                    else:
                        self.SetCellTextColour(r,c,"red")
                        self.SetCellValue(r,c, "-100%")

                    

        else:
            errorLabel = wx.StaticText(self, -1, "No Posts found from {}".format(date))
