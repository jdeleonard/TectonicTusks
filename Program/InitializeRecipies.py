import ast
from Recipies import *
from os.path import exists

class InitializeRecipies:


    def validateFoodFile():
        # file doesn't exist
        if not exists("recipies.txt"):
            # create file
            recipieFile = open("recipies.txt", "x")


    def initializeRecipiesFromFile():

        # make sure file is present
        InitializeRecipies.validateFoodFile()

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

            if Recipies.searchRecipie(recipieName) == None :
                Recipies.addRecipie(recipieName, dict)

    def saveRecipiesToFile():

        # make sure file is present
        InitializeRecipies.validateFoodFile()

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
            #print(fileFormatedString)

            currentRecipie = currentRecipie.next
            i += 1



    def appendRecipieToFile(toAdd : str):

        # make sure file is present
        InitializeRecipies.validateFoodFile()

        # open recipie file for writing
        recipieFile = open("recipies.txt", "a")

        recipieFile.write(toAdd)
        recipieFile.write("\n")


    def checkDictFormat(toCheck : str) -> bool:

        temp = toCheck

        temp = temp.replace(",","")
        temp = temp.replace(" ","")
        temp = temp.replace(":","")
        temp = temp.replace("\n","")

        return temp.isnumeric()
