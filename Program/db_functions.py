import sqlite3

from datetime import date
  

def opendb(dbFile): 

    conn = None
    try:
        conn = sqlite3.connect(dbFile)
    except Error as e:
        print(e)

    return conn



def getNumOfRows(conn):
    
    cursor = conn.cursor()
    query = "SELECT COUNT(*) FROM food"
    cursor.execute(query)
    numRowsList = cursor.fetchall()

    for row in numRowsList:
        for r in row:
            numRows = r
    return numRows


def getAllRows(conn):

    cursor = conn.cursor()
    query = "SELECT * FROM food"
    cursor.execute(query)
    rows = cursor.fetchall()

    return rows


def insertRow(conn, id, name, unit, edate):
    cursor = conn.cursor()
    query = "INSERT INTO food(id, name, amount, unit, expires) VALUES(?, ?, 0, ?, ?)"
    cursor.execute(query, (id, name, unit, edate))
    conn.commit()


def checkForAlreadyPost(conn):
    today = date.today()
    cursor = conn.cursor()
    query = "SELECT * FROM past_food where date = ?"
    print(today)
    cursor.execute(query, (today))
    rows = cursor.fetchall()
    if (rows > 0):
        print (">0")
    else:
        print ("<0")



def saveFoodForDay(conn):
    cursor = conn.cursor()
    query = "SELECT id, name, amount FROM food"
    cursor.execute(query)
    rows = cursor.fetchall()
    insertFoodBackupsForDay(conn, rows)
    

def insertFoodBackupsForDay(conn, list):
    today = date.today()
    checkForAlreadyPost(conn)
    cursor = conn.cursor()
    query = "INSERT INTO past_food (date, food_id, name, amount) VALUES(?, ?, ?, ?)"

    for rows in list:
        food_id = rows[0]
        name = rows[1]
        amount = rows[2]
        
        cursor.execute(query, (today, food_id, name, amount))
        conn.commit()