import wx

from Panels import *


class InsertionFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, title="Insert New Item", size = (300,300))
        self.insert_panel = InsertionPanel(self)