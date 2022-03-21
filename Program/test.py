import wx
import wx.grid as wxgrid

from db_functions import *
import globals



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
                self.SetCellValue(r,c, str(rows[r][c]))

       
        



class MyForm(wx.Frame):

    def OnQuit(self, e):
        self.Close()

    def printer(self):
        self.print("TESTER")
    
    def __init__(self):

        wx.Frame.__init__(self, parent=None, title="An Eventful Grid", size=(800,450))
        panel = wx.Panel(self)

        myGrid = MyGrid(panel)

        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(myGrid, 1)

        panel.SetSizer(sizer)

        button = wx.Button(panel, label="Close", size=(50,50))
        self.Bind(wx.EVT_BUTTON, self.OnCloseMe, button)
        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)

        sizer.Add(button, 0, wx.ALL | wx.CENTER, 5) 

        menubar = wx.MenuBar()

        fileMenu = wx.Menu()
        fileMenu.Append(wx.ID_SAVE, '&Save')

        qmi = wx.MenuItem(fileMenu, wx.ID_EXIT, '&Quit')
        fileMenu.Append(qmi)

        self.Bind(wx.EVT_MENU, self.OnQuit, qmi)

        functionMenu = wx.Menu()
        #functionMenu.Append(wx.ID_ANY, '&Update')
        tester = wx.MenuItem(functionMenu, wx.ID_ANY, '&Update')
        functionMenu.Append(tester)
        self.Bind(wx.EVT_MENU, self.printer(), tester)

        menubar.Append(fileMenu, '&File')
        menubar.Append(functionMenu, '&Functions')
        
        self.SetMenuBar(menubar)
        self.SetSize((350, 250))
        self.Centre()

        
        
    


    def OnCloseMe(self, event):
        self.Close(True)

    def OnCloseWindow(self, event):
        self.Destroy() 




if __name__ == "__main__":
    app = wx.App()
    frame = MyForm()
    frame.Show()
    app.MainLoop()