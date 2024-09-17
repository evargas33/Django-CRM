import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'milo',
    passwd = 'Comp@dr3s33',
    
)

#prepare cursor object

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE elderco")

print("All Done!")