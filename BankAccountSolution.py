class Account():

    def __init__(self,owner,balance=0):

        self.owner = owner
        self.balance = balance

    def deposit(self,dep_amt):

        #self.balance = self.balance + dep_amt
        self.balance += dep_amt
        print(f"Added {dep_amt} to the balance")

    def withdrawl(self,wd_amt):

        if self.balance >= wd_amt:
            #self.balance = self.balance - wd_amt
            self.balance -= wd_amt
            print("Withdrawl accepted")
        else:
            print("Sorry not enough funds!")

    def __str__(self):
        return f"Owner: {self.owner} \nBalance: {self.balance}"


a = Account("Sam",500)
print(a.owner)
#Sam
print("-----------------")
print(a.balance)
#500
print("-----------------")
print(a.deposit(100))
#Added 100 to the balance
print("-----------------")
print(a)
#Owner: Sam
#Balance: 600
print("-----------------")
a.withdrawl(600)
#Withdrawl accepted
print("-----------------")
print(a)
#Owner: Sam
#Balance: 0
print("-----------------")
a.withdrawl(1)
#Sorry not enough fund
print("-----------------")
print(a)
#Owner: Sam
#Balance: 0
print("-----------------")


