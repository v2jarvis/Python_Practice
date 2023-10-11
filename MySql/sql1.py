#connect the database and show the record
import mysql.connector
connection=mysql.connector.Connect(host='localhost',user='root',password='',database='v2jarvis')
print(connection) #if the mysql connected then print this address=<mysql.connector.connection.MySQLConnection object at 0x00000287AB8CE200> if not then show the error
cur=connection.cursor()
cur.execute('select * from admin')
for i in cur:
    print(i)
