import wx
import wx.grid as wxgrid
import sqlite3

import globals

from db_functions import *


class GridFrame(wx.Frame):
    def __init__(self, parent):

        conn = opendb("food.db")
        
        wx.Frame.__init__(self, parent)

        grid = wx.Panel(self)
        grid = wxgrid.Grid(self, -2)

        grid.CreateGrid(getNumOfRows(conn), globals.TABLE_COLS)

        grid.SetColSize(4, 120)

        grid.SetColLabelValue(0, "ID")
        grid.SetColLabelValue(1, "Food")
        grid.SetColLabelValue(2, "Amount")
        grid.SetColLabelValue(3, "Unit")
        grid.SetColLabelValue(4, "Expiration Date")

        rows = getAllRows(conn)


        numRows = getNumOfRows(conn)
      
        for r in range(getNumOfRows(conn)):
            for c in range(globals.TABLE_COLS):
                grid.SetCellValue(r, c, str(rows[r][c]))

                
        self.Show()

#  class InsertFrame(wx.Frame):
#     def __init__(self, parent, id):
#         wx.Frame.__init__(self,parent,id, 'Frame with Button', size=(300,100))
#         panel = wx.Panel(self)
#         button = wx.Button(panel, label="Close", pos=(125,10), size=(50,50))
#         self.Bind(wx.EVT_BUTTON, self.OnCloseMe, button)
#         self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)

#     def OnCloseMe(self, event):
#         self.Close(True)

#     def OnCloseWindow(self, event):
#         self.Destroy() 


if __name__ == '__main__':

    

    app = wx.App(100)

    frame = GridFrame(parent=None)

    #frame2 = InsertFrame(parent=frame, id=-1)
    #frame2.Show()
    app.MainLoop()
