import wx
import ast
from Recipies import *
from InitializeRecipies import *

# window wrapper for recipie frame
class AddRecipieFrame(wx.Frame):

    # initializer
    def __init__(self, parent, title):
        super(AddRecipieFrame, self).__init__(parent, title=title)

        # define member variables
        self.closeCount = 0
        self.name = ""
        self.dict = ""
        self.saved = False
        self.myPanel = None

        # initialize UI
        self.InitUI()

        # center window
        self.Centre()

    # initialize frame ui
    def InitUI(self):
        # create panel
        self.myPanel = AddRecipiePanel(self)

        # bind events
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.Bind(wx.EVT_BUTTON, self.OnButtonClicked)


    # activates on close of the window, makes sure user doesn't quit without saving unless wanted
    def OnClose(self, e):

        # inputted information is saved, don't prompt user and close
        if self.isSaved() == True:
            self.Destroy()

        # inputted information isn't saved, prompt user
        else:

            # first attempt at closing, prompt user
            if self.closeCount != 1:
                print("Recipie not saved, to discard close again")
                self.closeCount += 1

            # second attempt at closing, close
            else:
                self.Destroy()



    # returns boolean if the information inputted hasn't been saved, to determine if a popup should deter user from quitting without saving
    def isSaved(self) -> bool:
        return self.myPanel.submitButton.gotSaved or ( (not self.myPanel.nameGrab.hasEdited) and (not self.myPanel.ingredientGrab.hasEdited) )


    # submit button clicked, save inputted recipie
    def OnButtonClicked(self, e):

        # get name and ingredients
        name = self.myPanel.nameGrab.getName()
        ingredients = self.myPanel.ingredientGrab.getName()

        # format string for file saving
        formatString = (name + "/{" + ingredients + "}").replace("\n", "")

        # save recipie to file
        InitializeRecipies.appendRecipieToFile(formatString)




# content as a whole in the recipie panel
class AddRecipiePanel(wx.Panel):

    # initializer
    def __init__(self, *args, **kw):
        super(AddRecipiePanel, self).__init__(*args, **kw)

        # set member variable
        self.nameGrab = None
        self.ingredientGrab = None
        self.submitButton = None

        self.Bind(wx.EVT_BUTTON, self.OnButtonClicked)

        # initialize UI
        self.InitUI()


    # create all content in panel, buttons, text boxes, labels, and space them
    def InitUI(self):

        # main sizer
        mainSizer = wx.BoxSizer(wx.VERTICAL)


        # horizontal sizer 1
        subSizer1 = wx.BoxSizer(wx.HORIZONTAL)

        # Name label
        nameLabel = wx.StaticText(self, -1, "Name:")
        nestedSizer1 = wx.BoxSizer()
        nestedSizer1.Add(nameLabel, flag=wx.RIGHT, border=30)
        subSizer1.Add(nestedSizer1, flag=wx.LEFT|wx.TOP|wx.BOTTOM, border=5)

        # Name grabber
        self.nameGrab = RecipieNameGrabber(self)
        subSizer1.Add(self.nameGrab, flag = wx.EXPAND|wx.ALIGN_LEFT|wx.ALL, border = 5)

        mainSizer.Add(subSizer1)



        # horizontal sizer 2
        subSizer2 = wx.BoxSizer(wx.HORIZONTAL)

        # Ingredients label
        ingredientsLabel = wx.StaticText(self, -1, "Ingedients:")
        nestedSizer2 = wx.BoxSizer()
        nestedSizer2.Add(ingredientsLabel, flag=wx.RIGHT, border = 0)
        subSizer2.Add(nestedSizer2, flag = wx.EXPAND|wx.ALIGN_LEFT|wx.ALL, border = 5)

        # Ingredients grabber
        self.ingredientGrab = IngredientsGrabber(self, -1, "ID:AMOUNT,\nID:AMOUNT,\nID:AMOUNT", style = wx.TE_MULTILINE)
        subSizer2.Add(self.ingredientGrab, flag = wx.EXPAND|wx.ALIGN_LEFT|wx.ALL, border = 5)

        mainSizer.Add(subSizer2)


        # horizontal sizer 3
        subSizer3 = wx.BoxSizer(wx.HORIZONTAL)

        # submit button
        self.submitButton = SubmitButton(self, label = 'Submit')
        subSizer3.Add(self.submitButton, 1, wx.ALIGN_CENTER)

        mainSizer.Add(subSizer3, 1, wx.EXPAND)


        # set the main sizer
        self.SetSizer(mainSizer)


    # activates on submit button press
    def OnButtonClicked(self, e):

        # format is correct, send button activation to AddRecipieFrame
        if InitializeRecipies.checkDictFormat(self.ingredientGrab.getName()):
            e.Skip()

        # format ins't correct
        else: #TODO fix
            print("Formatting error, follow given format")


# text box that is for the recipie name
class RecipieNameGrabber(wx.TextCtrl):

    # initializer
    def __init__(self, *args, **kw):
        super(RecipieNameGrabber, self).__init__(*args, **kw)

        # set member variables
        self.savedName = False
        self.hasEdited = False

        # initialize UI for text box
        self.InitUI()


    # Initialize UI and properties for the textbox
    def InitUI(self):

        self.Bind(wx.EVT_TEXT, self.OnType)


    # Gets called when a key is typed or edited in the text boxe
    def OnType(self, event):
        # set name to content in the text box
        name = self.getName()

        # set boolean properties about the text box
        self.savedName = False
        self.hasEdited = True

    # returns the content inside the text box
    def getName(self) -> str:
        return self.GetValue()



# text box that is for the ingrident / ingredients
class IngredientsGrabber(wx.TextCtrl):

    # Initializer
    def __init__(self, *args, **kw):
        super(IngredientsGrabber, self).__init__(*args, **kw)

        # set member variables
        self.savedIngredients = False
        self.hasEdited = False

        # initialize UI for text box
        self.InitUI()


    # Initialize UI and properties for the textbox
    def InitUI(self):

        self.Bind(wx.EVT_TEXT, self.OnType)


    # Gets called when a key is typed or edited in the text boxe
    def OnType(self, event):
        dict = self.getName()
        self.savedIngredients = False
        self.hasEdited  = True


    # returns the content inside the text box
    def getName(self) -> str:
        return self.GetValue()




# Button for submitting the recipie information
class SubmitButton(wx.Button):


    # initializer
    def __init__(self, *args, **kw):
        super(SubmitButton, self).__init__(*args, **kw)

        # set member variables
        self.gotSaved = False

        self.Bind(wx.EVT_BUTTON, self.OnButtonClicked)

    # activates on press of the submit button
    def OnButtonClicked(self, e):

        # saved information to False
        self.gotSaved = True
        # send event to further classes
        e.Skip()




def main():

    app = wx.App()
    ex = AddRecipieFrame(None, title='Add Recipie')
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
