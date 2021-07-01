from typing import ClassVar

class Atm():
    def __init__(self , CashWithdrawl , BalanceEnquiry):
        self.CashWithdrawl = CashWithdrawl
        self.BalanceEnquiry = BalanceEnquiry

    def setAtm(self):
        print("started")    

bank = Atm("will u like to withdraw" , "check balance")   
print(bank.CashWithdrawl)
print(bank.BalanceEnquiry)
print(bank.setAtm())     

