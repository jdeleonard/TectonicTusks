import sqlite3
import time
from datetime import date

# Function to open the database connection
# The name of the database file is passed
def opendb(dbFile):

    conn = None
    try:
        conn = sqlite3.connect(dbFile)
    except Error as e:
        print(e)

    return conn

def deleteItemSQL(conn, id):
    cursor = conn.cursor()
    query = "DELETE FROM food WHERE id = {}".format(id)
    cursor.execute(query)
    conn.commit()

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


def updateRow(conn, id, amount):
    cursor = conn.cursor()
    query = "UPDATE food SET amount=? where id=?"
    cursor.execute(query, (amount, id))
    conn.commit()

# returns date as datetime.date with given id
def getExpireDate(conn, id):
    cursor = conn.cursor()
    query = "SELECT expires FROM food WHERE id=?"
    cursor.execute(query, (id, ))
    return cursor.fetchone()[0]

# returns inventory amount with given id
def getInventoryAmount(conn, id):
    cursor = conn.cursor()
    query = "SELECT amount FROM food WHERE id=?"
    cursor.execute(query, (id, ))
    return cursor.fetchone()[0]

# returns id with given name
def getID(conn, name):
    try:
        cursor = conn.cursor()
        query = "SELECT id FROM food WHERE name=?"
        cursor.execute(query, (name, ))
        return cursor.fetchone()[0]
    except:
        print("There is no ",name)
        return False


# returns boolean for if the id is present or not, true if present, false if not present
def checkID(conn, id):
    cursor = conn.cursor()
    query = "SELECT EXISTS (SELECT amount FROM food WHERE id=?)"
    cursor.execute(query, (id, ))
    return bool(cursor.fetchone()[0])


# Update Table information Functions
def UpdateButton(conn):
    cursor = conn.cursor()
    query = """UPDATE food SET amount = ? WHERE id = ?"""  # working line
    #Trows = cursor.fetchall()
    id = 1 # working
    amount = 200  #working
    val = (amount, id) #working
    cursor.execute(query, val) #working
    conn.commit()

    #for rows in Trows:
#        id = 1 #rows[0]
 #       name = 'Let' #rows[1]
  #      amount = 99 #rows[2]
   #     #unit = 'lb' #rows[3]
    #    cursor.execute(query, (name, amount, unit, id))
     #   conn.commit()


    #conn.commit()


# Past Food Functions

# Main called function to save the food into past_food
def saveFoodForDay(conn):
    cursor = conn.cursor()
    query = "SELECT id, name, amount FROM food"
    cursor.execute(query)
    rows = cursor.fetchall()
    insertFoodBackupsForDay(conn, rows)

# Checks to make sure that the user hasn't already saved for the day
# If the user has saved for the day -- delete all entries for the day and replace them
def checkForAlreadyPost(conn):
    today = date.today()
    cursor = conn.cursor()
    query = "SELECT * FROM past_food where date='{}'".format(today)
    cursor.execute(query)
    rows = cursor.fetchall()

    if (len(rows) > 0):
        query = "DELETE FROM past_food where date='{}'".format(today)
        cursor.execute(query)
        conn.commit()

# Inserts the current items in the main 'food' table, and enters them into the 'past_food' -- as a way to save the contents
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

# Returns all the saved contents of past_food for a specified date
def getAllRowsPastFood(conn, date):
    cursor = conn.cursor()
    query = "SELECT food_id, name, amount, date FROM past_food WHERE date='{}'".format(date)
    cursor.execute(query)
    rows = cursor.fetchall()
    return rows

# Returns the number of rows that are saved for a specified date
def getNumOfRowsPastFood(conn, date):
    cursor = conn.cursor()
    query = "SELECT COUNT(*) FROM past_food WHERE date='{}'".format(date)
    cursor.execute(query)
    numRowsList = cursor.fetchall()

    for row in numRowsList:
        for r in row:
            numRows = r
    return numRows

# Returns a tuple of all the unique dates in the past_food table
def getAllPastFoodDates(conn):
    cursor = conn.cursor()
    query = "SELECT DISTINCT date FROM past_food"
    cursor.execute(query)
    all_db_dates = cursor.fetchall()
    return all_db_dates