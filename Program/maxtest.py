from db_functions import *
from Recipies import *
from OrderPanel import *
from datetime import datetime
from datetime import date
from InitializeRecipies import *

if __name__ == '__main__':

    InitializeRecipies.initializeRecipiesFromFile()

    app = wx.App()
    ex = OrderFrame(None)
    ex.Show()
    app.MainLoop()
