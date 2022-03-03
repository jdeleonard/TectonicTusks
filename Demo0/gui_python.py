import wx
import wx.grid as grid
import sqlite3


def insertDB(first, last):
	connection = sqlite3.connect("test.db")
	if (connection):
		cursor = connection.cursor()
		query = "INSERT INTO people(first, last) values('{}', '{}')".format(first, last)
		cursor.execute(query)

	else:
		print("Database Connection Error")

	connection.commit()



def removeDB(id):
	connection = sqlite3.connect("test.db")
	if (connection):
		cursor = connection.cursor()
		query = "DELETE FROM people WHERE id={}".format(id)
		cursor.execute(query)

	else:
		print("Database Connection Error")

	connection.commit()


def getName(id):
	connection = sqlite3.connect("test.db")
	if (connection):
		cursor = connection.cursor()
		query = "SELECT first, last FROM people WHERE id={}".format(id)
		cursor.execute(query)
		result = cursor.fetchone()
		return result
	
	else:
		print("Database Connection Error")


class MyFrame(wx.Frame):
	def __init__(self):

		super().__init__(parent=None, title="Python Window")
		panel = wx.Panel(self)

		my_sizer = wx.BoxSizer(wx.VERTICAL)

		self.first_ctrl = wx.TextCtrl(panel)
		self.last_ctrl = wx.TextCtrl(panel)
		self.id_ctrl = wx.TextCtrl(panel)
		

		my_btn = wx.Button(panel, label='Insert Person')
		my_btn.Bind(wx.EVT_BUTTON, self.test_press)

		get_btn = wx.Button(panel, label="Get Person")
		get_btn.Bind(wx.EVT_BUTTON, self.get_press)


		my_sizer.Add(self.first_ctrl, 0, wx.ALL | wx.LEFT, 5)
		my_sizer.Add(self.last_ctrl, 0, wx.ALL | wx.RIGHT, 5)
		my_sizer.Add(my_btn, 0, wx.ALL | wx.LEFT, 5)
		my_sizer.Add(self.id_ctrl, 0, wx.ALL | wx.CENTER, 5)
		my_sizer.Add(get_btn, 0, wx.ALL | wx.CENTER, 5)
		
		panel.SetSizer(my_sizer)

		self.Show()


	def test_press(self, event):
		first_name = self.first_ctrl.GetValue()
		last_name = self.last_ctrl.GetValue()
		if not first_name or not last_name:
			print("You didn't enter anything!")
		else:
			insertDB(first_name, last_name)

			
	def get_press(self, event):
		val = self.id_ctrl.GetValue()
		print(getName(val))







if __name__ == '__main__':

	app = wx.App()
	frame = MyFrame()
	app.MainLoop()


	

