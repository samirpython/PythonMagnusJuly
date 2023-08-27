class Teacher:
    def English(self):
        print("English Language")
class Student1 (Teacher):
    def Maths(self):
        print("Mathamatics")

class Student2(Teacher):
    pass

obj1= Student1()
obj2= Student2()
obj1.English()
obj2.English()
obj1.Maths()

