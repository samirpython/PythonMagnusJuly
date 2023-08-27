class Sample():
    def m1(self):
        print("m1 function")

    def m2(self):
        print("m2 function")

    def __init__(self,a,b):
        print(a+b)

obj1=Sample(10,20)
obj1.m1()
obj1.m2()
