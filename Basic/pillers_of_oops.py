from abc import ABC, abstractmethod

class BankAccount(ABC):    # Abstract Base Class
    bank_name = "HDFC"     # Class attribute shared by all

    def __init__(self, acc_no, holder, balance=0):
        self.acc_no = acc_no            # Instance attribute
        self.holder = holder            # Instance attribute
        self.__balance = balance        # Private attribute (Encapsulation)
        self.transaction_history = []

    def get_balance(self):
        return self.__balance
    
    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Balance cannot be negative!")
    
    # Deposit method (common for all accounts)
    def deposit(self, amount):
        if amount >=0:
            self.__balance += amount
            self.transaction_history.append(f"Deposited: {amount}")
        else:
            print("Amount is negative")
    
    # Abstract method → forces subclasses to implement withdrawal rules
    @abstractmethod
    def withdraw(self, amount):
       pass

    def display_balance(self):
        print(f"Account {self.acc_no} Balance: {self.__balance}")
    
    @classmethod
    def show_bank_name(cls):
        print(f"Bank Name: {cls.bank_name}")


# SavingsAccount inherits BankAccount
class SavingAccount(BankAccount):
    MIN_BALANCE = 1000

    # Polymorphic withdraw method
    def withdraw(self, amount):
        if self.get_balance() - amount >= self.MIN_BALANCE:
            self.set_balance(self.get_balance() - amount)
            self.transaction_history.append(f"Withdrawn: {amount}")
            print(f"Withdrawal successful! New balance: {self.get_balance()}")
        else:
            print(f"Cannot withdraw: minimum balance {self.MIN_BALANCE} required.")


# CurrentAccount inherits BankAccount
class CurrentAccount(BankAccount):
    OVERDRAFT_LIMIT = 5000

    # Polymorphic withdraw method
    def withdraw(self, amount):
        if self.get_balance() - amount >= -self.OVERDRAFT_LIMIT:
            self.set_balance(self.get_balance() - amount)
            self.transaction_history.append(f"Withdrawn: {amount}")
            print(f"Withdrawal successful! New balance: {self.get_balance()}")
        else:
            print(f"Cannot withdraw: overdraft limit {self.OVERDRAFT_LIMIT} exceeded.")
            

# ----------------- Example Usage -----------------
acc_1 = SavingAccount(101, "Akku", 5000)
acc_2 = CurrentAccount(102, "Yash", 2000)

acc_1.deposit(500)
acc_1.withdraw(4500)
acc_2.withdraw(6500)
acc_2.withdraw(4000)

acc_1.display_balance()
acc_2.display_balance()
BankAccount.show_bank_name()