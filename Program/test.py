import wx
import wx.grid as gridlib

from db_functions import *
import globals



class MyGrid(gridlib.Grid):

    def __init__(self, parent):
        gridlib.Grid.__init__(self,parent)
        self.CreateGrid(12,8)
        



class MyForm(wx.Frame):
    
    def __init__(self):
        wx.Frame.__init__(self, parent=None, title="An Eventful Grid", size=(800,450))
        panel = wx.Panel(self)

        myGrid = MyGrid(panel)

        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(myGrid, 1)
        panel.SetSizer(sizer)

        button = wx.Button(panel, label="Close", pos=(750,400), size=(50,50))
        self.Bind(wx.EVT_BUTTON, self.OnCloseMe, button)
        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)

    def OnCloseMe(self, event):
        self.Close(True)

    def OnCloseWindow(self, event):
        self.Destroy() 




if __name__ == "__main__":
    app = wx.App()
    frame = MyForm()
    frame.Show()
    app.MainLoop()