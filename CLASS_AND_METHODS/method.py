# Create a method that will add, debit a user and then delete a function: If user account balance is 0,
# User Account name method is deleted,thus Account is deleted. 
import sys

class Account:
    def _init_(self):
        self.name = 'Grace'
        self.balance = 3000
        self.deposit = 1000
        self.withdrawal = 4000

    def acctname(self):
        return self.name

    def add(self):
        print('Your initial balance is:', self.balance)
        print('Your deposit is:', self.deposit)
        newbal = self.deposit + self.balance
        return newbal
    

    def debit(self):
        print('Your withdrawal amount is:', self.withdrawal)
        tbalance = (self.balance + self.deposit)
        newbal2 = tbalance - self.withdrawal
        if self.withdrawal > tbalance:
            print('Insufficient balance')
            sys.exit()
        
        elif self.withdrawal <= tbalance:
            return newbal2
    def delete(self):
        tbalance = (self.balance + self.deposit)
        if tbalance - self.withdrawal == 0:
            del Account.add
            del Account.acctname
            print('Your Account is deleted')
        else:
            print('Your Account is still Active')   


# Create Object of the class
myaccount = Account()
print('Account name is:', Account.acctname(myaccount))
print('Total balance is:', Account.add(myaccount))
print('Current balance is:', Account.debit(myaccount))
Account.delete(myaccount)
