from db_functions import *



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

    # Prints the node's name and ingredients, used for debugging
    def printRecipieNode(self):
        print(self.name, " ingredients: ")
        for item in self.ingredients:
            print("Item: ", item, "  Amount: ", self.ingredients[item])



# Global variable for recipies, DO NOT CHANGE OR DELETE
firstRecipie = Recipies("Null", {}, None)
