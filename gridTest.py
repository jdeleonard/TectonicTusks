import wx 
import wx.grid as wxgrid
import sqlite3




def getNumOfRows():
    connection = sqlite3.connect("food.db")
    cursor = connection.cursor()

    query = "SELECT COUNT(*) FROM food"

    cursor.execute(query)

    numRowsList = cursor.fetchall()

    for row in numRowsList:
        for r in row:
            numRows = r
    return numRows

def getAllRows():

    connection = sqlite3.connect("food.db")
    cursor = connection.cursor()

    query = "SELECT * FROM food"

    cursor.execute(query)

    rows = cursor.fetchall()

    return rows



class GridFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent)
        grid = wxgrid.Grid(self, -1)

        grid.CreateGrid(getNumOfRows(), 5)

        grid.SetColSize(4, 120)

        grid.SetColLabelValue(0, "ID")
        grid.SetColLabelValue(1, "Food")
        grid.SetColLabelValue(2, "Amount")
        grid.SetColLabelValue(3, "Unit")
        grid.SetColLabelValue(4, "Expiration Date")

        rows = getAllRows()


        numRows = getNumOfRows()
      

        for r in range(getNumOfRows()):
            for c in range(5):
                grid.SetCellValue(r, c, str(rows[r][c]))



      
        self.Show()



if __name__ == '__main__':

    app = wx.App(100)
    frame = GridFrame(None)
    app.MainLoop()

    
        