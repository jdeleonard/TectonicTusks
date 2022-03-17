import wx
import wx.grid as wxgrid
import sqlite3

import globals

from db_functions import *


class GridFrame(wx.Frame):
    def __init__(self, parent):

        conn = opendb("food.db")

        wx.Frame.__init__(self, parent)
        grid = wxgrid.Grid(self, -1)

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



if __name__ == '__main__':

    

    app = wx.App(100)
    frame = GridFrame(None)
    app.MainLoop()
