from db_functions import *
from Recipies import *
from OrderPanel import *


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

    mango3 = Recipies.addRecipie("Hamburger", {5:2 , 9:6, 16:1})
    mango3.printRecipieNode()
    print()

    mango4 = Recipies.addRecipie("Sandwitch", {20:2, 3:1})
    mango4.printRecipieNode()
    print()

    mango5 = Recipies.addRecipie("Steak", {1:2 , 3:6, 123:1000})
    mango5.printRecipieNode()
    print()

    mango6 = Recipies.addRecipie("Soup", {5:2 , 9:7})
    mango6.printRecipieNode()
    print()

    mango7 = Recipies.addRecipie("Backpack", {3:3 , 9:7, 20:8})
    mango7.printRecipieNode()
    print()

    mango8 = Recipies.addRecipie("Horse", {3:3 , 9:7, 20:8})
    mango8.printRecipieNode()
    print()


    mango9 = Recipies.addRecipie("Pond", {3:3 , 9:7, 20:8})
    mango9.printRecipieNode()
    print()

    mango10 = Recipies.addRecipie("Duck", {3:3 , 9:7, 20:8})
    mango10.printRecipieNode()
    print()

    r = Recipies.searchRecipie("Pasta")
    print(r.checkAvailability())


    app = wx.App()
    ex = OrderFrame(None)
    ex.Show()
    app.MainLoop()
