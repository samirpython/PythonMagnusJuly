from mysql import connector

myDbConnection = connector.connect(host='localhost', user='root', password='root', database='PythonMagnus')
c1 = myDbConnection.cursor()

vempno = int(input("Enter the Empnum value: "))
vename = input("Enter the Ename value: ")
vsal = int(input("Enter the sal value: "))
vdeptno = int(input("Enter the deptno value: "))

c1.execute("insert in to emp (empno, ename, sal, deptno) values (%s,%s,%s,%s)", (vempno, vename, vsal, vdeptno))

myDbConnection.commit()
myDbConnection.close()
