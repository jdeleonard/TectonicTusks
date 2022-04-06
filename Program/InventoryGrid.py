import sqlite3, wx, globals
import wx.grid as wxgrid
import datetime

from db_functions import *


class InventoryGrid(wxgrid.Grid):

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


def shouldBeRed(edate):
    now = datetime.datetime.now()

    eyear = int(edate[0:4])
    emonth = int(edate[5:7])
    eday = int(edate[8:10])
    edate = datetime.datetime(eyear, emonth, eday)

    if (now >= edate):
        return True
    elif(now < edate):
        return False