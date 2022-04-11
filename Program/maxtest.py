from db_functions import *
from Recipies import *
from OrderPanel import *
from datetime import datetime
from datetime import date

if __name__ == '__main__':

    conn = opendb("food.db")

    breadID = getID(conn, "Bread")
    print(breadID)

    mango = Recipies.addRecipie("Pasta", {1:2, 2:40})
    mango.printRecipieNode()
    print()

    mango2 = Recipies.addRecipie("Fish", {3:10, 4:3})
    mango2.printRecipieNode()
    print()

    mango3 = Recipies.addRecipie("Chicken Rice", {9:0.5, 3: 1})
    mango3.printRecipieNode()
    print()



    r = Recipies.searchRecipie("Pasta")
    print(r.checkAvailability())



    print(mango.getLowestDaysTillExperation())




    app = wx.App()
    ex = OrderFrame(None)
    ex.Show()
    app.MainLoop()
