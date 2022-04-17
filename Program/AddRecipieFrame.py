import wx

class AddRecipieFrame(wx.Frame):

    def __init__(self, parent, title):
        super(AddRecipieFrame, self).__init__(parent, title=title)

        self.InitUI()
        self.Centre()

    def InitUI(self):
        myPanel = AddRecipiePanel(self)
        self.Bind(wx.EVT_CLOSE, self.OnClose)

    def OnClose(self, e):

        print("Closed")


class AddRecipiePanel(wx.Panel):

    def __init__(self, *args, **kw):
        super(AddRecipiePanel, self).__init__(*args, **kw)
        self.nameGrab = None
        self.ingredientGrab = None
        self.submitButton = None

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
        nameGrab = RecipieNameGrabber(self)
        subSizer1.Add(nameGrab, flag = wx.EXPAND|wx.ALIGN_LEFT|wx.ALL, border = 5)

        mainSizer.Add(subSizer1)



        # horizontal sizer 2
        subSizer2 = wx.BoxSizer(wx.HORIZONTAL)

        # Ingredients label
        ingredientsLabel = wx.StaticText(self, -1, "Ingedients:")
        nestedSizer2 = wx.BoxSizer()
        nestedSizer2.Add(ingredientsLabel, flag=wx.RIGHT, border = 0)
        subSizer2.Add(nestedSizer2, flag = wx.EXPAND|wx.ALIGN_LEFT|wx.ALL, border = 5)

        # Ingredients grabber
        ingredientGrab = IngredientsGrabber(self, -1, "{\nID:AMOUNT\nID:AMOUNT\n}", style = wx.TE_MULTILINE)
        subSizer2.Add(ingredientGrab, flag = wx.EXPAND|wx.ALIGN_LEFT|wx.ALL, border = 5)

        mainSizer.Add(subSizer2)


        # horizontal sizer 3
        subSizer3 = wx.BoxSizer(wx.HORIZONTAL)

        # submit button
        submitButton = SubmitButton(self, label = 'Submit')
        subSizer3.Add(submitButton, 1, wx.ALIGN_CENTER)


        mainSizer.Add(subSizer3, 1, wx.EXPAND)


        # set the main sizer
        self.SetSizer(mainSizer)


class RecipieNameGrabber(wx.TextCtrl):

    def __init__(self, *args, **kw):
        super(RecipieNameGrabber, self).__init__(*args, **kw)
        self.InitUI()

    def InitUI(self):

        self.Bind(wx.EVT_TEXT, self.OnType)

    def OnType(self, event):
        print(self.getName())

    def getName(self) -> str:
        return self.GetValue()



class IngredientsGrabber(wx.TextCtrl):

    def __init__(self, *args, **kw):
        super(IngredientsGrabber, self).__init__(*args, **kw)
        self.InitUI()

    def InitUI(self):

        self.Bind(wx.EVT_TEXT, self.OnType)

    def OnType(self, event):
        print(self.getName())

    def getName(self) -> str:
        return self.GetValue()


class SubmitButton(wx.Button):

    def __init__(self, *args, **kw):
        super(SubmitButton, self).__init__(*args, **kw)
        self.Bind(wx.EVT_BUTTON, self.OnButtonClicked)

    def OnButtonClicked(self, e):
        print("Pressed Submit")




def main():

    app = wx.App()
    ex = AddRecipieFrame(None, title='Add Recipie')
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
