# class Student:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
        
#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print("your average marks is : ", sum/4)
        
        
# s1 = Student("Bijaya", [23, 34, 56,78])
# s1.get_avg()




# ChatGpt Questions

# class Student:
#     def __init__(self,name, marks):
#         self.name = name 
#         self.marks = marks
        
#     def get_average(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         average = sum / len(self.marks)
#         return average
        
        
        
# s1 = Student("Manish", [70,80,90])
# print("your average score is : ", s1.get_average())


# Rectangle

# class Rectangle:
#     def __init__(self,length,width):
#         self.length = length
#         self.width = width
        
#     def area(self):
#         total = self.length*self.width
#         print("Total area of Rectangle :", total)
        
#     def perimeter(self):
#         Per_rectangle = 2 * (self.length + self.width)
#         return Per_rectangle
        
# rec = Rectangle(10, 12)     
# rec.area() 
# rec.perimeter()


# Bank Account
# class BankAccount: TRIED CODE, ITS NOT CORRECT

#     def __init__(self, name,balance):
#         self.name = name 
#         self.balance = balance
        
#     def deposit(self):
#         bal= 0
#         bal += self.balance
#         return bal
    
#     def withdraw(self):
#         if(self.balance >= withdraw):
#            bal -= withdraw
#            return bal
#         else:
#             print("you don't ahve enough money to withdrae")
        
        
# bank = BankAccount("Manish", 100)
# print(bank.deposit())

# class BankAccount: # its working code

#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance
        
#     def deposit(self, amount):
#         self.balance += amount
#         return self.balance
    
#     def withdraw(self, amount):
#         if self.balance >= amount:
#             self.balance -= amount
#             return self.balance
#         else:
#             print("You don't have enough money to withdraw")
#             return self.balance
    
#     def show_balance(self):
#         print(f"{self.name}'s current balance: {self.balance}")
        

# # Example usage
# bank = BankAccount("Manish", 100)

# print("After deposit:", bank.deposit(50))     # Deposit 50
# print("After withdrawal:", bank.withdraw(30)) # Withdraw 30
# bank.show_balance()



# Employee Bonus

# class Employee:
#     def __init__(self,name, salary):
#         self.name = name 
#         self.salary = salary
        
        
#     def calculate_bonus(self):
#         if(self.salary >= 50000):
#             bonus = self.salary * 10/100
#             self.salary += bonus
#             return self.salary
#         else:
#             bonus = self.salary * 5/100
#             self.salary +=bonus
#             return self.salary
           
           
           
# emp = Employee("Biju", 100000)
# print("After bonus, you total salary will be : ", emp.calculate_bonus())



# Book Details
# class Book:
#     def __init__(self,title,author,price):
#      self.title = title
#      self.author = author
#      self.price = price
     
#     def discount(self, discount):
#         self.discount = discount
#         discount_price = self.price*self.discount
#         self.price -= discount_price
#         return self.price
    
    
    
    
# dis =Book("Physics", "Bijaya", 800)
# print(dis.discount(0.10))


# Design a Library System

# class Library:
#     def __init__(self, bookId, stuedentId ):
#         self.bookId = bookId
#         self.studentId = stuedentId
        
        
#     def addBook(self):
        
    
    