from db_functions import *

connect = opendb("food.db")


class Sandwitch:
    # Recipie Dictionary: ID, RECIPIE AMOUNT
    recipie = { getID(connect, "Bread"): 2,
                getID(connect, "Chicken"): 1
              }

# recipie: called with using a item's (class) recipie
def order(recipie):
    for item in recipie:
        amount = recipie[item]
        currentAmount = getInventoryAmount(connect, item)
        updateRow(connect, item, currentAmount - amount)
