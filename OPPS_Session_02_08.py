'''
A Python program to create a Bank clas where deposits and withdrawals can be handled using instance methods.
'''
import sys


class Bank:
    def __init__(self, name):
        self.name = name
        self.balance =0
    def deposit(self, amount):
        if(amount>0):
            self.balance= self.balance+amount
        return self.balance
    def withdraw(self,amount):
        if(amount>self.balance):
            print('Not sufficient balance ')
        else:
            self.balance = self.balance-amount
        return self.balance

name = input("Enter name")
account = Bank(name)
while(True):
    print('d - deposit, w - withdraw, e- Exit')
    choice = input("Enter choice")
    if(choice=='e' or choice=='E'):
        sys.exit()
    amt = float(input("Enter amount"))
    if(choice=='d' or choice=='D'):
        print('Balance after deposit ', account.deposit(amt))
    if (choice == 'w' or choice == 'W'):
        print('Balance after withdrawal ', account.withdraw(amt))
