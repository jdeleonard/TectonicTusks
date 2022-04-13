import ast
from Recipies import *

class InitializeRecipies:

    def initializeRecipiesFromFile():

        # open the recipie file for reading
        recipieFile = open("recipies.txt", "r")

        # loop through all the lines in the recipie file
        for line in recipieFile:

            # if the line isn't blank, break the line up into name and recipie components
            if line:
                brokenLine = line.split("/")

            # file isn't formatted correctly, exit loop
            if len(brokenLine) != 2:
                print("ERROR, RECIPIES FILE FORMAT ERROR")
                break;

            # get the name of the recipie
            recipieName = brokenLine[0]

            # get the dictionary ingredients list
            stringDict = brokenLine[1]
            dict = ast.literal_eval(stringDict)

            Recipies.addRecipie(recipieName, dict)

    def saveRecipiesToFile():

        # open recipie file for writing
        recipieFile = open("recipies.txt", "w")

        currentRecipie = firstRecipie


        i = 0

        while i < Recipies.getNumRecipies():
            name = currentRecipie.name
            ingredients = currentRecipie.ingredients
            ingredientsString = (str(ingredients))

            fileFormatedString = name + "/" + ingredientsString
            recipieFile.write(fileFormatedString)
            recipieFile.write("\n")
            print(fileFormatedString)

            currentRecipie = currentRecipie.next
            i += 1
