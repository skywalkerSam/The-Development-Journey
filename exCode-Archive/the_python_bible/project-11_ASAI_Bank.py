
# ASAI BANK

#parent class for all accounts
class account:
    def __init__(self, name, balance, min_balance):      #constructor
        self.name = name
        self.balance = balance
        self.min_balance = min_balance

    #deposit()
    def deposit(self, amount):
        self.balance += amount

    #withdraw()
    def withdraw(self, amount):
        if self.balance - amount >= self.min_balance:
            self.balance -= amount
        else:
            print('Sorry, You have not enough balance to withdraw !')    #minimum balance
    
    #statement
    def statement(self):
        print('Account balance; {} INR'.format(self.balance))


#current_account
class current(account):
    def __init__(self, name, balance):      #constructor
        super().__init__(name, balance, min_balance = -1000)    #constructor

    def __str__(self):     #string_return
        return "Current Account Holder; {} & Account Balance; {}".format(self.name, self.balance)


#savings_account
class savings(account):
    def __init__(self, name, balance):      #constructor
        super().__init__(name, balance, min_balance = 0)      #super() constructor

    def __str__(self):    #string_return
        return "Savings Account Holder; {} & Account Balance; {}".format(self.name, self.balance)




#account1, current
account1 = current('Captain', 36999)   #account opening
print(account1)

account1.deposit(3669)
account1.statement()

account1.withdraw(6000)
account1.statement()

account1.withdraw(36999)   #min_balance alert
account1.statement()

account1.deposit(3369)
account1.statement()

print(account1)
account1.withdraw(39036)
account1.statement()    #because min_balance is -1000 for current accounts
print(account1)

account1.withdraw(2)   #not enough balance



print('\n')



#account2, savings
account2 = savings('Murlidhar Singh', 336699)   #account opening
print(account2)

account2.deposit(333)
account2.statement()

account2.withdraw(666)
account2.statement()

account2.withdraw(3366999)   #min_balance alert
account2.statement()

account2.deposit(36936999)
account2.statement()

print(account2)
account2.withdraw(37273365)
account2.statement()    






