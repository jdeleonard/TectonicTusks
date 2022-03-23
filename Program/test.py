import wx
import wx.grid as wxgrid

from db_functions import *
import globals



class MyGrid(wxgrid.Grid):

    def getInfo(self):
        conn = opendb("food.db")
        numRows = getNumOfRows(conn)

        for i in range(numRows):
            print(self.GetCellValue(i, 0))

    def __init__(self, parent):

        conn = opendb("food.db")
        wxgrid.Grid.__init__(self,parent)

        self.CreateGrid(getNumOfRows(conn), globals.TABLE_COLS)
        self.SetColSize(4,120)

        readOnlyAttr = wxgrid.GridCellAttr()
        readOnlyAttr.SetReadOnly(True)
        self.SetColAttr(0, readOnlyAttr)
        self.SetColAttr(1, readOnlyAttr)
        self.SetColAttr(3, readOnlyAttr)
        self.SetColAttr(4, readOnlyAttr)


        self.SetColLabelValue(0, "ID")
        self.SetColLabelValue(1, "Food")
        self.SetColLabelValue(2, "Amount")
        self.SetColLabelValue(3, "Unit")
        self.SetColLabelValue(4, "Expiration Date")


        
        

        rows = getAllRows(conn)

        numRows = getNumOfRows(conn)

        for r in range(numRows):
            for c in range(globals.TABLE_COLS):
                self.SetCellValue(r,c, str(rows[r][c]))


        idAndAmounts = []
        for i in range(numRows):
            tmp = [self.GetCellValue(i,0), self.GetCellValue(i, 2)]
            idAndAmounts.append(tmp)

        print(idAndAmounts)
        
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

        self.idText.SetValue("")
        self.foodText.SetValue("")
        self.unitText.SetValue("")
        self.edateText.SetValue("")

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


        button = wx.Button(self, label="Add Item", size=(75,75))
        self.Bind(wx.EVT_BUTTON, self.insertItem, button)


        sizer = wx.FlexGridSizer(cols=2, hgap=6, vgap=6)
        sizer.AddMany([idLabel,self.idText,foodLabel,self.foodText,unitLabel,self.unitText,edateLabel,self.edateText, button])
    





        self.SetSizer(sizer)

        

class MyForm(wx.Frame):

    def OnQuit(self, e):
        self.Close()


    
    def onSwitchPanels(self, event):
        if self.panel_one.IsShown():
            self.SetTitle("Panel Two Showing")
            self.panel_one.Hide()
            self.panel_two.Show()
        else:
            self.SetTitle("Panel One Showing")

            # Essentially a Refresh of the Panel -- shows updated database table
            self.panel_one.Destroy()
            self.panel_one = PanelOne(self)
            self.sizer = wx.BoxSizer(wx.VERTICAL)
            self.sizer.Add(self.panel_one, 1, wx.EXPAND)
            self.SetSizer(self.sizer)

            self.panel_one.Show()
            self.panel_two.Hide()

        self.Layout()
        
        
    def updateDB(self, event):
        conn = opendb("food.db")

        numRows = getNumOfRows(conn)



        #updateRow(conn, 20, 20)



        # Refresh the Panel
        self.panel_one.Destroy()
        self.panel_one = PanelOne(self)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.panel_one, 1, wx.EXPAND)
        self.SetSizer(self.sizer)
        self.panel_one.Show()
        self.Layout()

    def __init__(self):

        wx.Frame.__init__(self, parent=None, title="Inventory Sheet", size=(1200,1000))

        self.panel_one = PanelOne(self)
        self.panel_two = PanelTwo(self)
        
        self.panel_two.Hide()


        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.panel_one, 1, wx.EXPAND)
        self.sizer.Add(self.panel_two, 1, wx.EXPAND)
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

        fileMenu = wx.Menu()

        switchItem = fileMenu.Append(wx.ID_ANY, "Switch Panels", "")
        self.Bind(wx.EVT_MENU, self.onSwitchPanels, switchItem)

        updateItem = fileMenu.Append(wx.ID_ANY, "Update Sheet", "")
        self.Bind(wx.EVT_MENU, self.updateDB, updateItem)

        quitItem = wx.MenuItem(fileMenu, wx.ID_EXIT, '&Quit')
        fileMenu.Append(quitItem)
        self.Bind(wx.EVT_MENU, self.OnQuit, quitItem)

        menubar.Append(fileMenu, '&File')

        self.SetMenuBar(menubar)
        # self.SetSize((350, 250))
        # self.Centre()

        
        
    


    def OnCloseMe(self, event):
        self.Close(True)

    def OnCloseWindow(self, event):
        self.Destroy() 




if __name__ == "__main__":
    app = wx.App()
    frame = MyForm()
    frame.Show()
    app.MainLoop()