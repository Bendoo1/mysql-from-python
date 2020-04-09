import os
import pymysql

#Get username from AWS C9
#(modify this variable in running on another environment)
username = os.getenv('C9_USER')
print(username)
# Connect to the DB
connection = pymysql.connect(host='localhost', user=username, password='', db='Chinook')

try:
    #Run a query
    with connection.cursor() as cursor:
        sql = "SELECT * FROM Artist;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
        
finally:
    #Close connection, regardless of successful query
    connection.close()
