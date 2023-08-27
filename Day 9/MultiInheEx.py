class Father:
    def Home(self):
        print("2 flats and 2 plots with House")

    def Bike (self):
        print("Harley Davidson")

class Mother:
    def Car(self):
        print("2 Cars")
    def Cash(self):
        print("1 Billion farm house")

class Son(Father,Mother):
    pass

obj1 = Son()
obj1.Home()
obj1.Car()
obj1.Cash()
obj1.Bike()
