class Car:
    # class attribute
    wheel=4

    # Constructor / Initializer
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    # Instance Method
    def display_info(self):
        print(f"{self.year} {self.make} {self.model}")


# Creating Objects
car_1 = Car("Toyota", "Camry", 2022)
car_2 = Car("Honda", "Civic", 2021)

car_1.display_info()
car_2.display_info()


# 1. Difference between a class attribute and an instance attribute

# Class attribute

    # Shared across all objects of the class.

    # Defined directly inside the class, outside any method.

    # Example: bank_name = "HDFC" → every BankAccount object will have the same bank name.

    # Changing it at the class level affects all instances (unless overridden in an object).

# Instance attribute

    # Unique to each object.

    # Defined inside the constructor (__init__) using self.

    # Example: self.balance = 0 → each account object has its own separate balance.

# LETS DO QUICK DEMO
class BankAccount:
    bank_name = "HDFC"   # Class Attribute

    def __init__(self, acc_no, holder):
        self.acc_no = acc_no    # Instance Attribute
        self.holder = holder    # Instance Attribute
        self.balance = 0        # Instance Attribute

a_1 = BankAccount(1234, "Akanchha")
a_2 = BankAccount(1235, "Yasharth")

print(a_1.bank_name)
print(a_2.bank_name)
print(a_1.balance)
print(a_2.balance)

# Change class attribute
BankAccount.bank_name = "ICICI"
print(a_1.bank_name)
print(a_2.bank_name)

# Change instance attribute
a_1.balance = 500
print(a_1.balance)     # 500 (only for a1)
print(a_2.balance)     # 0 (independent)
