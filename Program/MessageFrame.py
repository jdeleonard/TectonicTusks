import wx

# Creates window for message
class MessageWindow(wx.Frame):

    # initializer
    def __init__(self, parent, title):
        super(MessageWindow, self).__init__(parent, title=title)

        # generate UI
        self.InitUI()

        # center window
        self.Centre()

    # initialize UI
    def InitUI(self):
        myPanel = MessagePanel(self)


# Creates message
class MessagePanel(wx.Panel):

    # initializer
    def __init__(self, *args, **kw):
        super(MessagePanel, self).__init__(*args, **kw)
        # Initialize UI
        self.InitUI()


    # Initialize UI, Centers message: 'Are you sure you want to quit without saving?'
    def InitUI(self):
        # set front for the whole panel
        font = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)
        font.SetPointSize(20)

        # Create Sizers
        vboxCenter = wx.BoxSizer(wx.VERTICAL)
        hbox = wx.BoxSizer(wx.HORIZONTAL)

        # Create Message
        st1 = wx.StaticText(self, label="Are you sure you want to quit without saving?\nClose again to quit without saving.")
        st1.SetFont(font)

        # Space the message in the panel
        hbox.Add(st1, 0, wx.CENTER)

        vboxCenter.Add((0,0), 1, wx.EXPAND)
        vboxCenter.Add(hbox, flag=wx.CENTER)
        vboxCenter.Add((0,0), 1, wx.EXPAND)

        self.SetSizer(vboxCenter)
