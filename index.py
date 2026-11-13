# 1. Student Age Validation
class Student:
    def __init__(self, age):
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if 18 <= value <= 60:
            self.__age = value
        else:
            print("Invalid age")

s = Student(20)
s.age = 25
print(s.age)


# 2. Bank Account
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if value >= 0:
            self.__balance = value
        else:
            print("Invalid balance")

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")

b = BankAccount(5000)
b.deposit(1000)
b.withdraw(2000)
print(b.balance)


# 3. Employee Salary
class Employee:
    def __init__(self, name, dept, salary):
        self.name = name
        self._department = dept
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if value >= 15000:
            self.__salary = value
        else:
            print("Invalid salary")

    def display(self):
        print(self.name, self._department, self.__salary)

e = Employee("Ravi", "IT", 25000)
e.display()


# 4. Product Price
class Product:
    def __init__(self, price):
        self.__price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value > 0:
            self.__price = value
        else:
            print("Invalid price")

    def display(self):
        print("Price:", self.__price)

p = Product(500)
p.price = 800
p.display()


# 5. User Login System
class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        if len(value) >= 8:
            self.__password = value
        else:
            print("Invalid password")

    def login(self, username, password):
        if self.username == username and self.__password == password:
            print("Login Successful")
        else:
            print("Login Failed")

u = User("Ravi", "python123")
u.login("Ravi", "python123")