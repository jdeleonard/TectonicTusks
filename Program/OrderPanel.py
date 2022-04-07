import wx
from enum import Enum


class InventoryStatus(Enum):
    OUT = 0
    LOW = 1
    MEDIUM = 2
    HIGH = 3


class OrderPanel(wx.Panel):

    def __init__(self, *args, **kw):
        super(OrderPanel, self).__init__(*args, **kw)
        self.InitUI()

    def InitUI(self):
        # create buttons and display them
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        spacer = wx.FlexGridSizer(2, 3, 20, 50)

        buttonTacos = OrderButton(self, label='Tacos')
        buttonPasta = OrderButton(self, label='Pasta')
        buttonHamburger = OrderButton(self, label='Hamburger')
        buttonHotDog = OrderButton(self, label='Hot Dog')
        buttonSteak = OrderButton(self, label='Steak')
        buttonSoup = OrderButton(self, label='Soup')

        spacer.AddMany([
        (buttonTacos, 1, wx.EXPAND),
        (buttonPasta, 1, wx.EXPAND),
        (buttonHamburger, 2, wx.EXPAND),
        (buttonHotDog, 1, wx.EXPAND),
        (buttonSteak, 1, wx.EXPAND),
        (buttonSoup, 1, wx.EXPAND),
        ])

        hbox.Add(spacer, proportion=1, flag=wx.ALL|wx.EXPAND, border=15)
        self.SetSizer(hbox)

        #self.Bind(wx.EVT_BUTTON, OrderButton.OnButtonClicked, button1)
        #self.Bind(wx.EVT_BUTTON, OrderButton.OnButtonClicked, button1)


class OrderButton(wx.Button):

    def __init__(self, *args, **kw):
        super(OrderButton, self).__init__(*args, **kw)
        self.Bind(wx.EVT_BUTTON, self.OnButtonClicked)
        self.food = self.GetLabel()

    # Activates on button press
    def OnButtonClicked(self, e):
        if self.food == "Tacos":
            print("tacos")
        elif self.food == "Pasta":
            print("pasta")
        elif self.food == "Hamburger":
            print("hamburger")
        elif self.food == "Hot Dog":
            print("hot dog")
        elif self.food == "Steak":
            print("steak")
        elif self.food == "Soup":
            print("soup")
        else:
            print("ERROR: ADD BUTTON LABEL TO: OrderButton OnButtonClicked()")

    # Updates button appearance based on inventory
    def updateStatus(self):
        print("Placeholder, will complete later")

    # Updates the inventory status for the given items
    def getInventoryStatus(self):
        print("Placeholder, will complete later")
