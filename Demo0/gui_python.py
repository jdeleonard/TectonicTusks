import wx
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


class MyFrame(wx.Frame):
	def __init__(self):

		super().__init__(parent=None, title="Hello World")
		panel = wx.Panel(self)

		self.first_ctrl = wx.TextCtrl(panel, pos=(5,5))
		self.last_ctrl = wx.TextCtrl(panel, pos=(5, 35))

		my_btn = wx.Button(panel, label='Insert Person', pos=(5,55))
		my_btn.Bind(wx.EVT_BUTTON, self.test_press)

		self.Show()


	def test_press(self, event):
		first_name = self.first_ctrl.GetValue()
		last_name = self.last_ctrl.GetValue()
		if not first_name or not last_name:
			print("You didn't enter anything!")
		else:
			insertDB(first_name, last_name)

			


if __name__ == '__main__':

	app = wx.App()
	frame = MyFrame()
	app.MainLoop()


