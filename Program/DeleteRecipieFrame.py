import wx
from enum import Enum
from db_functions import *
import datetime
import time
from Recipies import *
from InitializeRecipies import *


# Order panel which contains all the UI components
class DeleteRecipiePanel(wx.Panel):

    # Initializer
    def __init__(self, *args, **kw):
        super(DeleteRecipiePanel, self).__init__(*args, **kw)

        # Get all the recipies from the file
        InitializeRecipies.initializeRecipiesFromFile()

        # Initialize UI
        self.InitUI()


    # Initializes all UI
    def InitUI(self):

        # Create a button for every recipie
        buttons = [None]
        buttons.clear()
        looper = firstRecipie
        numItems = Recipies.getNumRecipies()
        i = 0

        # create sizers so panel looks pretty
        numRows = numItems / 3
        if numItems % numRows != 0:
            numRows += 1

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        spacer = wx.FlexGridSizer(numRows, 3, 20, 50)

        # Create all buttons and add them to buttons[]
        while i < numItems:
            buttons.append(DeleteButton(self, label=looper.name))
            looper = looper.next
            i += 1

        # Add all buttons to spacer
        i = 0
        for button in buttons:
            spacer.Add(button, 1, wx.EXPAND)
            i += 1


        # Set a border for the window
        hbox.Add(spacer, proportion=1, flag=wx.ALL|wx.EXPAND, border=15)
        self.SetSizer(hbox)



class DeleteButton(wx.Button):

    def __init__(self, *args, **kw):
        # Construct Button
        super(DeleteButton, self).__init__(*args, **kw)
        self.Bind(wx.EVT_BUTTON, self.OnButtonClicked)

        # Set member variables food to string and recipie to the node in the recipies
        self.food = self.GetLabel()
        self.recipie = Recipies.searchRecipie(self.GetLabel())



    # Activates on button press, delete recipie
    def OnButtonClicked(self, e):

        # open database
        conn = opendb("food.db")

        first = Recipies.deleteRecipie(self.recipie)

        if first:
            InitializeRecipies.saveRecipiesToFileMinusThis(self.recipie.name)
            print("FIRST")

        self.Disable()



# wrapping panel or window for order panel
class DeleteFrame(wx.Frame):

    # initializer
    def __init__(self, *args, **kw):
         super(DeleteFrame, self).__init__(*args, **kw)

         # initialize UI and properties
         self.InitUI()

    # Initialize UI and properties
    def InitUI(self):
        # load order panel
        panel = DeleteRecipiePanel(self)
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.SetTitle('Delete Recipe')
        self.Centre()

    # activates on close of the window
    def OnClose(self, e):
        # save recipies and close
        InitializeRecipies.saveRecipiesToFile()
        self.Destroy()
