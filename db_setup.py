import sqlite3

connection = sqlite3.connect("food.db")

cursor = connection.cursor()


query = """CREATE table food (
                    id INTEGER PRIMARY KEY,
                    name VARCHAR(100),
                    amount FLOAT(10),
                    unit VARCHAR(50),
                    expires DATE
                    )"""

cursor.execute(query)

connection.commit()

