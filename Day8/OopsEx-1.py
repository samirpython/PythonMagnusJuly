class Sample:
    a=10
    b=20
    def m1(self):
        print("M1 function")

obj1=Sample()
print(obj1.a)
print(obj1.b)
obj1.m1()
print(type(obj1))