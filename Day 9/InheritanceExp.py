class Sample:
    def m1(self):
        print("welcome m1 function")

class Demo(Sample):
    def m2(self):
        print("welcome m2 function")

obj1 = Demo()
obj1.m1()
obj1.m2() 

