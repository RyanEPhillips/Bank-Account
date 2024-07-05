import random

class BankAccount:
    def __init__(self, accountNumber, accountHolder, balance):
        self.__accountNumber = accountNumber
        self._accountHolder = accountHolder
        self.__balance = balance

    @property
    def accountNumber(self):
        return self.__accountNumber

    @classmethod
    def createNewAccount(cls, accountHolder, initialDeposit):
        accountNumber = random.randint(100000, 999999)
        return cls(accountNumber, accountHolder, initialDeposit)

    def deposit(self, amount):
        self.__balance += amount
        print(f"Thank you {self._accountHolder}, ${amount} has been deposited in the account and now have a balance of ${self.__balance}")
    
    def withdrawal(self, amount):
        if amount > self.__balance:
            print(f"I'm sorry {self._accountHolder} there is not enough money to cover that")
        else:
            self.__balance -= amount
        print(f"You have withdrawn {amount} and now have ${self.__balance}")

    def getBalance(self):
        if self.__balance > 0:
            print(f"You have ${self.__balance}")
        else:
            print("You have no money!")

    def displayAccountInfo(self):
        print(f"Hello, {self._accountHolder}, Your current balance for {self.__accountNumber} is {self.__balance}")
        
if __name__ == "__main__":

    account1 = BankAccount.createNewAccount("Clark", 500)
    account2 = BankAccount.createNewAccount("Raven", 1000)
    account3 = BankAccount.createNewAccount("Belamy", 5000)
    account4 = BankAccount.createNewAccount("John", 10000)

    account1.displayAccountInfo()
    account2.displayAccountInfo()
    account3.displayAccountInfo()
    account4.displayAccountInfo()

    account1.deposit(1500)
    account3.deposit(2500)
    account2.withdrawal(2500)
    account4.withdrawal(1005)

    account1.displayAccountInfo()
    account2.displayAccountInfo()
    account3.displayAccountInfo()
    account4.displayAccountInfo()


