from mysql import connector

myDBConnection = connector.connect(host='localhost',user='root',password='root')

print(myDBConnection)
