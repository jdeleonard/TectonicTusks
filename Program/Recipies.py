from db_functions import *
from datetime import datetime
from datetime import date


# Recipies Data Structure:
# Member variables: Name of item, ingredients (dictionary), Link to next recipie

class Recipies:

    # Constructor, takes name (String), ingredients (Dictionary), next (Link to next recipie)
    # Dictionary format: {database id for ingredient : amount, etc..., etc...}
    def __init__(self, name, ingredients, next):
        self.name = name
        self.ingredients = ingredients
        self.next = next


    # Returns the last recipie, mainly used for adding to end of linked list
    def getLastRecipie():

        # set up the last variable
        last = firstRecipie

        # loop through linked list (Recipie) until last Recipie is found
        while last.next != None:
            last = last.next

        # return last recipie
        return last


    # Returns the total amount of recipies in the linked list
    def getNumRecipies():

        # set up last variable and count for linked list nodes
        last = firstRecipie
        count = 1

        # loop through linked list (Recipie) and incriment by 1 to get count
        while last.next != None:
            count += 1
            last = last.next

        # return the total amount of recipies in the list
        return count


    # Adds a recipie to the end of the linked list (Recipie), returnns added item (only used if needed)
    # takes: String name, Dictionary (see above format) ingredients
    def addRecipie(name, ingredients):

        # Set up placeholder variable for node (recipie) added
        recipieAdded = None

        # If its the first recipie being added, change beginning node of list
        if (firstRecipie.name == "Null"):

            # set member variables
            firstRecipie.name = name
            firstRecipie.ingredients = ingredients

            # set return node to node added
            recipieAdded = firstRecipie

        # Not the first recipie being added
        else:
            # set the last node's next node to the new node
            last = Recipies.getLastRecipie()
            last.next = Recipies(name, ingredients, None)

            # set return node to node added
            recipieAdded = last.next

        # return the node added
        return recipieAdded


    # Searches data structure for node that contains the inputed name, returns that node
    def searchRecipie(name):

        # set up variable for returning and looping
        found = firstRecipie

        i = 0

        # loop through linked list (Recipie) and return once the name is found
        while i < Recipies.getNumRecipies():

            if found.name == name:
                return found
            found = found.next
            i += 1

        # not found, print a message and return None
        # print("NOT FOUND", name, "NOT FOUND")
        # print("Iterated", i, "times.")

        return None


    # Searches through all the items ingredients to make sure they're in the inventory
    def checkIfPresent(self):

        # Set up return variable
        present = True

        # Loop through all the recipies ingredients
        for item in self.ingredients:
            if checkID(opendb("food.db"), item) == False:
                present = False

        # Return value
        return present


    # Searches through all the items ingredients to make sure there's enough of the ingredient to produce
    def checkAvailability(self):

        # make sure all the items are present in the database
        if self.checkIfPresent():

            # Check to make sure there is enough inventory for each item
            for item in self.ingredients:

                # get total amount of inventory for the given food item
                totInventory = getInventoryAmount(opendb("food.db"), item)

                # If there isn't enough inventory to produce item, return false
                if totInventory - self.ingredients[item] < 0:
                    return False

            # Enough inventory to produce item, return True
            return True

        # Not all items are present in the inventory
        else:
            return False


    # Removes required amount of ingredients for recipie from the database, NOTE: can't be called if not enough items in inventory
    def order(self):
        # loop through all the recipie ingredients
        for item in self.ingredients:

            conn = opendb("food.db")

            countNeeded = self.ingredients[item]
            countTotal = getInventoryAmount(conn, item)

            updateRow(conn, item, countTotal - countNeeded)


    # returns the amount of days till the expiration on the item expiring the soonest
    def getLowestDaysTillExperation(self) -> int:

        today = date.today()

        dayDiff = [0]
        dayDiff.clear()

        # get the lowest expiration date from all of ingredients
        for item in self.ingredients:
            expireDateString = getExpireDate(opendb("food.db"), item)
            expireDate = datetime.strptime(expireDateString, '%Y-%m-%d').date()
            daydifference = (expireDate - today).days
            dayDiff.append(daydifference)

        if dayDiff:
            lowestDifference = dayDiff[0]

            for diff in dayDiff:
                if diff < lowestDifference:
                    lowestDifference = diff

            return lowestDifference

        return -1

    # Prints the node's name and ingredients, used for debugging
    def printRecipieNode(self):
        print(self.name, " ingredients: ")
        for item in self.ingredients:
            print("Item: ", item, "  Amount: ", self.ingredients[item])







# Global variable for recipies, DO NOT CHANGE OR DELETE
firstRecipie = Recipies("Null", {}, None)
