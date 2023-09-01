class EligibleError(Exception):
    pass
class Sample:
    def Eligible(self,age,percentage):
        if age<18 or percentage<60:
            raise EligibleError("Not eligible for admission")
        else:
            print("Admission Successful")

obj1=Sample()
try:
    obj1.Eligible(18,61)
except EligibleError as e:
    print(e)
