import wx
from enum import Enum
from db_functions import *
import datetime
import time
from Recipies import *
from globals import *
from InitializeRecipies import *


# Order panel which contains all the UI components
class OrderPanel(wx.Panel):

    # Initializer
    def __init__(self, *args, **kw):
        super(OrderPanel, self).__init__(*args, **kw)

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
            buttons.append(OrderButton(self, label=looper.name))
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



class OrderButton(wx.Button):

    def __init__(self, *args, **kw):
        # Construct Button
        super(OrderButton, self).__init__(*args, **kw)
        self.Bind(wx.EVT_BUTTON, self.OnButtonClicked)

        # Set member variables food to string and recipie to the node in the recipies
        self.food = self.GetLabel()
        self.recipie = Recipies.searchRecipie(self.GetLabel())

        # Update button appearance if can't be ordered
        self.updateStatus()

    # Activates on button press
    def OnButtonClicked(self, e):

        # open database
        conn = opendb("food.db")

        self.recipie.order()

    # Updates button appearance based on inventory
    def updateStatus(self):

        # checks to make sure all all the ingredients are in the inventory and are enough in quanitity to make the item
        valid = self.recipie.checkAvailability()

        # item has at least one ingredient not in the inventory or at least one item that doesn't have enough inventory to produce item, disable button
        if not valid:
            self.Disable()

        # all of items ingredients are in the inventory and enough in stock
        else:

            # get the amount of days until the items soonest expiration date
            lowestDifference = self.recipie.getLowestDaysTillExperation()

            # item ingredient is expired, disable button
            if lowestDifference < 0:
                self.Disable()

            # Item is going to be expiring soon, days till expiration is defined by SELL_FAST_EXPIRING_DAYS in globals.py
            elif lowestDifference <= SELL_FAST_EXPIRING_DAYS:
                self.SetBackgroundColour((215, 252, 3, 255))





# wrapping panel or window for order panel
class OrderFrame(wx.Frame):

    # initializer
    def __init__(self, *args, **kw):
         super(OrderFrame, self).__init__(*args, **kw)

         # initialize UI and properties
         self.InitUI()

    # Initialize UI and properties
    def InitUI(self):
        # load order panel
        panel = OrderPanel(self)
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.SetTitle('Take Orders')
        self.Centre()

    # activates on close of the window
    def OnClose(self, e):

        # save recipies and close
        InitializeRecipies.saveRecipiesToFile()
        self.Destroy()
