import sqlite3

db = sqlite3.connect("shadesOfYellow.db")

cursor = db.cursor()

#SQL code
sql = "SELECT * FROM shadesOfYellow"

cursor.execute(sql)

results = cursor.fetchall()

print(results)

db.close