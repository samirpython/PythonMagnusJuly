from mysql import connector
myDBConnection = connector.connect(host='localhost',user='root',password='root',database='pythonmagnus')
c1 = myDBConnection.cursor()

#c1.execute("select * from emp where deptno=10")
c1.execute("select * from emp")
result = c1.fetchall()
#print(result)
for i in result: #To print the data one by one not in list
    print(i)
myDBConnection.close()