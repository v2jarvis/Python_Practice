import mysql.connector
connection=mysql.connector.Connect(host='localhost',user='root',password='batlix01',database='v2jarvis')
cur=connection.cursor()
cur.execute('select * from admin')
for i in cur:
    print(i)