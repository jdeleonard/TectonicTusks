import wx
import sqlite3


def insertDB(q):
	connection = sqlite3.connect("test.db")
	if (connection):
		cursor = connection.cursor()
		cursor.execute(q)

	else:
		print("Database Connection Error")

	connection.commit()



def removeDB(q):
	connection = sqlite.connect("test.db")
	if (connection):
		cursor = connection.cursor()
		cursor.execute(q)

	else:
		print("Database Connection Error")

	connection.commit()


class MyFrame(wx.Frame):
	def __init__(self):

		super().__init__(parent=None, title="Hello World")
		panel = wx.Panel(self)

		self.text_ctrl = wx.TextCtrl(panel, pos=(5,5))
		my_btn = wx.Button(panel, label='Press Me', pos=(5,55))
		my_btn.Bind(wx.EVT_BUTTON, self.test_press)


		self.Show();


	def test_press(self, event):
		value = self.text_ctrl.GetValue()
		if not value:
			print("You didn't enter anything!")
		else:

			connection = sqlite3.connect("test.db")
			cursor = connection.cursor()

			query = 'INSERT INTO people VALUES(2, "{}", \"rydecki\")'.format(value)
			print (query)
			cursor.execute(query)
			connection.commit()



if __name__ == '__main__':


	insertDB("INSERT INTO people values (3, 'alen', 'tan')")

	#app = wx.App()
	#frame = MyFrame()
	#app.MainLoop()


