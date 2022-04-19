import wx
import ast
from Recipies import *
from InitializeRecipies import *


#name : str = ""
#dict : str = ""
#saved = False

class AddRecipieFrame(wx.Frame):

    def __init__(self, parent, title):
        super(AddRecipieFrame, self).__init__(parent, title=title)

        self.closeCount = 0
        self.name = ""
        self.dict = ""
        self.saved = False
        self.myPanel = None

        self.Bind(wx.EVT_BUTTON, self.OnButtonClicked)

        self.InitUI()
        self.Centre()

    def InitUI(self):
        self.myPanel = AddRecipiePanel(self)
        self.Bind(wx.EVT_CLOSE, self.OnClose)


    # activates on close of the window, makes sure user doesn't quit without saving unless wanted
    def OnClose(self, e):
        if self.isSaved() == True:
            self.Destroy()
            print("Closed")
        else:
            if self.closeCount != 1:
                print("Recipie not saved, to discard close again")
                self.closeCount += 1
            else:
                self.Destroy()



    # returns boolean if the information inputted hasn't been saved, to determine if a popup should deter user from quitting without saving
    def isSaved(self) -> bool:
        return self.myPanel.submitButton.gotSaved or ( (not self.myPanel.nameGrab.hasEdited) and (not self.myPanel.ingredientGrab.hasEdited) )


    # submit button clicked, save inputted recipie
    def OnButtonClicked(self, e):
        print("Reached frame class")

        name = self.myPanel.nameGrab.getName()
        ingredients = self.myPanel.ingredientGrab.getName()

        formatString = (name + "/{" + ingredients + "}").replace("\n", "")

        print(formatString)

        InitializeRecipies.appendRecipieToFile(formatString)





class AddRecipiePanel(wx.Panel):

    def __init__(self, *args, **kw):
        super(AddRecipiePanel, self).__init__(*args, **kw)
        self.nameGrab = None
        self.ingredientGrab = None
        self.submitButton = None

        self.Bind(wx.EVT_BUTTON, self.OnButtonClicked)

        self.InitUI()

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



    def OnButtonClicked(self, e):

        if InitializeRecipies.checkDictFormat(self.ingredientGrab.getName()):
            e.Skip()

        else: #TODO fix
            print("Formatting error, follow given format")


class RecipieNameGrabber(wx.TextCtrl):

    def __init__(self, *args, **kw):
        super(RecipieNameGrabber, self).__init__(*args, **kw)
        self.savedName = False
        self.hasEdited = False
        self.InitUI()

    def InitUI(self):

        self.Bind(wx.EVT_TEXT, self.OnType)

    def OnType(self, event):
        name = self.getName()
        self.savedName = False
        self.hasEdited = True

    def getName(self) -> str:
        return self.GetValue()



class IngredientsGrabber(wx.TextCtrl):

    def __init__(self, *args, **kw):
        super(IngredientsGrabber, self).__init__(*args, **kw)
        self.savedIngredients = False
        self.hasEdited = False
        self.InitUI()

    def InitUI(self):

        self.Bind(wx.EVT_TEXT, self.OnType)

    def OnType(self, event):
        dict = self.getName()
        self.savedIngredients = False
        self.hasEdited  = True

    def getName(self) -> str:
        return self.GetValue()


class SubmitButton(wx.Button):

    def __init__(self, *args, **kw):
        super(SubmitButton, self).__init__(*args, **kw)

        self.gotSaved = False

        self.Bind(wx.EVT_BUTTON, self.OnButtonClicked)

    def OnButtonClicked(self, e):

        self.gotSaved = True
        e.Skip()




def main():

    app = wx.App()
    ex = AddRecipieFrame(None, title='Add Recipie')
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
