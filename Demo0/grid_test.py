import wx
import wx.grid as Grid

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title, size=(400, 300))

        self.panel = MyPanel(self)
        self.MyGrid = New_Grid(self, numRows=2, numCols=5)
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(self.MyGrid,1,wx.ALL|wx.EXPAND,0)
        self.SetSizer(mainSizer)


class MyPanel(wx.Panel):
    def __init__(self, parent):
        super(MyPanel, self).__init__(parent)


class New_Grid(Grid.Grid):
    def __init__(self, parent, numRows, numCols):
        Grid.Grid.__init__(self, parent)

        self.CreateGrid(numRows, numCols)
        self.SetRowLabelSize(35)
        self.AutoSizeColumns(True)
        # Display content
        self.displayContent()
        # ...
        self.handleEvents()

    def displayContent(self):
        myList = [
            "Col1",
            "Col2",
            "Col3",
            "Col4",
            "Set"
        ]
        x = 0
        for item in myList:
            self.SetColLabelValue(x, item)
            x += 1
        self.SetColLabelSize(25)
        self.AutoSizeColumns(True)
        self.update_Grid()

    def handleEvents(self):
        self.Bind(Grid.EVT_GRID_SELECT_CELL, self.onCellSelected)

    def onCellSelected(self, event):
        col = event.GetCol()
        if col == 5:
            Selected = event.GetRow()

    def update_Grid(self):
        img = wx.Bitmap("SET.png", wx.BITMAP_TYPE_PNG)
        self.rd = MyImageRenderer(img)
        # Buttons coordinates
        numRows = self.GetNumberRows()
        for y in range(numRows):
            self.rd.rend_row = y
            self.rd.rend_col = 4
            self.SetCellRenderer(self.rd.rend_row, self.rd.rend_col, self.rd)
            self.SetColSize(0, img.GetWidth() + 2)
            self.SetRowSize(0, img.GetHeight() + 3)
            self.SetReadOnly(self.rd.rend_row, self.rd.rend_col, True)

class MyImageRenderer(wx.grid.GridCellRenderer):
    def __init__(self, img):
        wx.grid.GridCellRenderer.__init__(self)
        self.img = img

    def Draw(self, grid, attr, dc, rect, row, col, isSelected):
        image = wx.MemoryDC()
        image.SelectObject(self.img)
        dc.SetBackgroundMode(wx.SOLID)
        if isSelected:
            dc.SetBrush(wx.Brush(wx.BLUE, wx.SOLID))
            dc.SetPen(wx.Pen(wx.BLUE, 1, wx.SOLID))
        else:
            dc.SetBrush(wx.Brush(wx.WHITE, wx.SOLID))
            dc.SetPen(wx.Pen(wx.WHITE, 1, wx.SOLID))
        dc.DrawRectangle(rect)
        width, height = self.img.GetWidth(), self.img.GetHeight()
        if width > rect.width - 2:
            width = rect.width - 2
        if height > rect.height - 2:
            height = rect.height - 2
        dc.Blit(rect.x + 1, rect.y + 1, width, height, image, 0, 0, wx.COPY, True)

    def GetBestSize(self, grid, attr, dc, row, col):
        text = grid.GetCellValue(row, col)
        dc.SetFont(attr.GetFont())
        w, h = dc.GetTextExtent(text)
        return wx.Size(w, h)


class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(parent=None,title="wxPython Window")
        self.frame.Show()
        return True


app = MyApp()
app.MainLoop()