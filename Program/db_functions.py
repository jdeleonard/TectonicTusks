import sqlite3


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


def printTest():
    print ("TEST PRINT")