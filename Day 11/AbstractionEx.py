
from abc import ABC,abstractmethod

class Accounts:
    def savings(self):
        print("No minimum balance and eran up to 7.5 % interest")

class Loans(ABC):
    @abstractmethod
    def pl(self):
        print("Personal Loans")
    @abstractmethod
    def hl(self):
        print("Home Loans")

class FinalAccount(Accounts,Loans):
    def pl(self):
        print("Personal loan with 11% interest")
    def hl(self):
        print("Home Loan with 8% floating interest")

obj1=FinalAccount()
obj1.savings()
obj1.hl()
obj1.pl()