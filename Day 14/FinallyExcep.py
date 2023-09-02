class Sample:
    def m1(self):
        a=10
        b=10
        try:
            print(a/b)
        except ZeroDivisionError as e:
            print(e)
        finally:
            print("Zero Error Division Done")
    def m2(self):
        c=10
        d=10
        try:
            print(d)
        except NameError as e1:
            print(e1)
        finally:
            print("Name Error Done")
obj1 = Sample()
obj1.m1()
obj1.m2()

