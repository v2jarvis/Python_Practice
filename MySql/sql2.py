#add the values in table and execute the command
import mysql.connector
connection=mysql.connector.Connect(host='localhost',user='root',password='',database='v2jarvis')
cur=connection.cursor()
id=2
name='sachin'
address='noida'
mobile=4566577555
cur.execute(f"insert into admin values('{id}','{name}','{address}','{mobile}')")
connection.commit()

