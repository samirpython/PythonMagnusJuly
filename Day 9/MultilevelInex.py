class GrandParent:
    def a1(self):
        print("3 Assets")

class Parent(GrandParent):
    def a2(self):
        print("2 Assests ")
class Son(Parent):
    def a3(self):
        print("1 Asset")

obj1 = Son() 
obj1.a1()
obj1.a2()
obj1.a3()
