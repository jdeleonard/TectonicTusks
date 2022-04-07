import sqlite3
import datetime
import time


def opendb(dbFile):

    conn = None
    try:
        conn = sqlite3.connect(dbFile)
    except Error as e:
        print(e)

    return conn

def deleteItemSQL(conn, id):
    cursor = conn.cursor()
    query = "DELETE FROM food WHERE id = %s"
    idForDelete = (id, )
    cursor.execute(query, idForDelete)
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
