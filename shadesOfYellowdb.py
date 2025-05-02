"""Code with functions for database of shades of yellow by Amy Lian 5/2/2025"""

#imports

import sqlite3

#constants and variables

DATABASE = "shadesOfYellow.db"

#functions

#main

db = sqlite3.connect(DATABASE)

cursor = db.cursor()

#SQL code
sql = "SELECT * FROM shadesOfYellow"

cursor.execute(sql)

results = cursor.fetchall()

print(results)

db.close