# Purpose : Create a bank account class that has two attributes: owner, balance
# Author:   Claudia Hill
# Date:     1/6/2020
# Description: Two methods deposit, withdraw - may not exceed the available balance
# Udemy Bootcamp OOP Challenge

class Account():

    #bank account with two attributes - owner, balance
    def __init__(self,owner,balance = 0):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return (f"Account owner: {self.owner}\nAccount balance: {self.balance}")

    def __str2__(self):
        return self.owner

    def __len__(self):
        return self.balance

    def deposit(self,deposit):
        self.balance = self.balance + deposit
        return "Deposit Accepted"

    def withdraw(self,withdraw):
        if (self.balance  - withdraw < 0):
            return "Funds Unavailable"
        else:
            self.balance = self.balance - withdraw
            return "Withdraw Accepted"


#Test code
'''
#test # 1. Instantiate the class
acct1 = Account('Jose',100)

# test 2. Print the object
print(acct1)
#Account owner:   Jose
#Account balance: $100

#test 3. Show the account owner attribute
print(acct1.owner)
#'Jose'

#test 4. Show the account balance attribute
print(acct1.balance)
#100

#test 5. Make a series of deposits and withdrawals
print(acct1.deposit(50))

print(acct1.balance)

#Deposit Accepted
acct1.withdraw(75)
#Withdrawal Accepted

print(acct1.balance)

# 6. Make a withdrawal that exceeds the available balance
print(acct1.withdraw(500))
#Funds Unavailable!

print(acct1.balance)
'''

print("-----------------")
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
a.withdraw(600)
#Withdrawl accepted
print("-----------------")
print(a)
#Owner: Sam
#Balance: 0
print("-----------------")
a.withdraw(1)
#Sorry not enough fund
print("-----------------")
print(a)
#Owner: Sam
#Balance: 0
print("-----------------")
