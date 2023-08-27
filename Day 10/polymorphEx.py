class Car_2022:
    def roof(self):
        print("Sunroof")
    def wheels(self):
        print("Normal Alloy Wheels")
    def Music(self):
        print('7" Touch screen music system')

class Car_2023(Car_2022):
    def roof(self):
        #print("Panaromic Sun roof")
        super().roof()

    def Music(self):
        print('11" Music Touch Player')

    def MobileConnect(self):
        print("Hyundai Blue Mobile Connect")
obj1 = Car_2023()
obj1.roof()
obj1.wheels()
obj1.Music()
obj1.MobileConnect()



