import wx
import wx.grid as wxgrid
import datetime

from db_functions import *
import globals


def shouldBeRed(edate):
    now = datetime.datetime.now()

    eyear = int(edate[0:4])
    emonth = int(edate[5:7])
    eday = int(edate[8:10])
    edate = datetime.datetime(eyear, emonth, eday)

    if (now >= edate):
        return True
    elif (now < edate):
        return False
    


class MyGrid(wxgrid.Grid):

    def __init__(self, parent):

        conn = opendb("food.db")
        wxgrid.Grid.__init__(self,parent)

        self.CreateGrid(getNumOfRows(conn), globals.TABLE_COLS)
        self.SetColSize(4,120)

        self.SetColLabelValue(0, "ID")
        self.SetColLabelValue(1, "Food")
        self.SetColLabelValue(2, "Amount")
        self.SetColLabelValue(3, "Unit")
        self.SetColLabelValue(4, "Expiration Date")

        rows = getAllRows(conn)

        numRows = getNumOfRows(conn)

        for r in range(numRows):
            for c in range(globals.TABLE_COLS):
                if (c == 4):
                    edate = str(rows[r][c])
                    if (shouldBeRed(edate)):
                        self.SetCellTextColour(r,c,"red")

                self.SetCellValue(r,c, str(rows[r][c]))

    



        



        
class PanelOne(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)
        #txt = wx.TextCtrl(self)
        myGrid = MyGrid(self)
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(myGrid, 1)
        self.SetSizer(sizer)


class PanelTwo(wx.Panel):

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

        button = wx.Button(self, label="Add", size=(50,50))
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

        if (id != ""):
            insertRow(conn, id, food, unit, edate)

        self.idText.SetValue("")
        self.foodText.SetValue("")
        self.unitText.SetValue("")
        self.edateText.SetValue("")

        self.GetParent().GetParent().refr()

#########################################
# PAST FOOD CLASSES AND FUNCTIONS
class PastFoodFrame(wx.Frame):

    def __init__(self, parent):

        self.date = ""

        wx.Frame.__init__(self, parent, title = "Get Past Inventory", size = (700,700))
        self.past_date_panel = PastDatePanel(self)
        #self.past_food_panel = PastFoodPanel(self)
        

        #self.past_food_panel.Hide()
        self.past_date_panel.Show()
        

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.past_date_panel, 1, wx.EXPAND)
        #self.sizer.Add(self.past_food_panel, 1, wx.EXPAND)
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

        rows = getAllRowsPastFood(conn, date)

        numRows = getNumOfRowsPastFood(conn, date)

        self.CreateGrid(numRows, 4)

        self.SetColLabelValue(0, "ID")
        self.SetColLabelValue(1, "Food")
        self.SetColLabelValue(2, "Amount")
        self.SetColLabelValue(3, "Date")

    
        for r in range(numRows):
            for c in range(4):
                self.SetCellValue(r,c, str(rows[r][c]))



##########################################
        
class InsertFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, title = "Insert New Item", size = (300,300))
        self.test_panel = PanelTwo(self)



class MyForm(wx.Frame):

    def OnQuit(self, e):
        self.Close()

    def refr(self):
        self.panel_one.Destroy()
        self.panel_one = PanelOne(self)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.panel_one, 1, wx.EXPAND)
        self.SetSizer(self.sizer)
        self.Layout()

    def onSwitchPanels(self, event):
        if self.panel_one.IsShown():
            self.SetTitle("Panel Two Showing")
            self.panel_one.Hide()
            self.past_panel.Show()
        else:
            self.SetTitle("Panel One Showing")

            # Essentially a Refresh of the Panel -- shows updated database table
            #self.panel_one.Destroy()
            #self.panel_one = PanelOne(self)
            #self.sizer = wx.BoxSizer(wx.VERTICAL)
            #self.sizer.Add(self.panel_one, 1, wx.EXPAND)
            #self.SetSizer(self.sizer)
            #self.panel_one.Layout()
            self.refr()
            self.panel_one.Show()
            self.past_panel.Hide()
        
        self.Layout()

    def onInsertNewItem(self, event):
        frame2 = InsertFrame(self)
        frame2.Show()

    def onPastFoodClick(self, event):
        pastFoodFrame = PastFoodFrame(self)
        pastFoodFrame.Show()

    def onSaveForDay(self, event):
        conn = opendb("food.db")
        saveFoodForDay(conn)



    def __init__(self):

        wx.Frame.__init__(self, parent=None, title="Inventory Sheet", size=(800,600))

        self.panel_one = PanelOne(self)
        self.panel_two = PanelTwo(self)
        #self.past_panel = PastFoodPanel(self)
        
        self.panel_two.Hide()
        #self.past_panel.Hide()


        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.panel_one, 1, wx.EXPAND)
        self.sizer.Add(self.panel_two, 1, wx.EXPAND)
        #self.sizer.Add(self.past_panel, 1, wx.EXPAND)
        self.SetSizer(self.sizer)

        # menubar = wx.MenuBar()
        # fileMenu = wx.Menu()
        # switch_panels_item = fileMenu.Append(wx.ID_ANY, "Switch Panels", "Some Text")
        # self.Bind(wx.EVT_MENU, self.onSwitchPanels, switch_panels_item)
        # menubar.Append(fileMenu, '&File')
        # self.SetMenuBar(menubar)
        # panel = wx.Panel(self)
        # button = wx.Button(panel, label="Close", size=(50,50))
        # self.Bind(wx.EVT_BUTTON, self.OnCloseMe, button)
        # self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)

        # sizer.Add(button, 0, wx.ALL | wx.CENTER, 5) 

        menubar = wx.MenuBar()

        # File Menubar Tab
        fileMenu = wx.Menu()

        switchItem = fileMenu.Append(wx.ID_ANY, "Switch Panels", "")
        self.Bind(wx.EVT_MENU, self.onSwitchPanels, switchItem)

        insertItem = fileMenu.Append(wx.ID_ANY, "Insert New Item", "")
        self.Bind(wx.EVT_MENU, self.onInsertNewItem, insertItem)

        pastFoodItem = fileMenu.Append(wx.ID_ANY, "Past Inventory", "")
        self.Bind(wx.EVT_MENU, self.onPastFoodClick, pastFoodItem)


        quitItem = wx.MenuItem(fileMenu, wx.ID_EXIT, '&Quit')
        fileMenu.Append(quitItem)
        self.Bind(wx.EVT_MENU, self.OnQuit, quitItem)


        # Save Menubar Tab
        saveMenu = wx.Menu()

        saveForDayItem = saveMenu.Append(wx.ID_ANY, "Post Inventory for Day", "")
        self.Bind(wx.EVT_MENU, self.onSaveForDay, saveForDayItem)


        menubar.Append(fileMenu, '&File')
        menubar.Append(saveMenu, '&Save')

        self.SetMenuBar(menubar)
        # self.SetSize((350, 250))
        # self.Centre()




if __name__ == "__main__":
    app = wx.App()
    frame = MyForm()
    frame.Show()
    app.MainLoop()