from mysql import connector
myDbConnection = connector.connect(host='localhost', user='root', password='root', database='PythonMagnus')
c1 = myDbConnection.cursor()
c1.execute("drop table if exists emp")
c1.execute("create table emp( empno int, ename varchar(20), sal int, deptno int )")
myDbConnection.commit()
myDbConnection.close()
