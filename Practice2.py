
# # functions
# # check the nums  is prime 


# def is_prime_num(num):
#     if num <=1:
#         return False
#     for i in range(2, num):
#         if num %i == 0:
#             return False
#     return True
        
        
  
# print(is_prime_num(9))



# def is_string_palindrome(val):
#     reverse_value = ""
#     for char in val:
#         reverse_value = char + reverse_value
#     if val == reverse_value:
#         return True
#     return False
   
# print(is_string_palindrome("NITIN"))




# # Write a funciton to find a factorail of a num

# def fact_num(num):
#     result = 1
#     for i in range(num, 0, -1):
#         result *= i
#     return result
        
# print(fact_num(5))



 # Classes and Objects

# class Student:
#     def __init__(self, name, roll_no, marks):
#         self.name = name 
#         self.roll_no = roll_no
#         self.marks = marks
        
#     def display(self):
#         print("My name is" , self.name , " and  the studnet roll no is " , self.roll_no , "and got makrs :" , self.marks)
    
# info = Student("Biaya", 1, 98)
# info.display()
   
   
   

# Wriet a function to find Greatest Common Divisor (GCD) of two numbers

# def GCD(num1, num2):
#    gcd = 1 
#    for i in range(1, min(num1, num2)+1):
#        if num1 % i == 0 and num2 % i == 0:
#            gcd = i
#    return gcd
        
# print(GCD(200, 50))


#  Create a Car class

# class Car:
#     def __init__(self, make,model, fuel):
#         self.make = make
#         self.model = model
#         self.fuel = fuel
        
#     def drive(self, distance):
        
#         fuel_needed = distance * 0.2
#         if self.fuel >= fuel_needed:
#             self.fuel -= fuel_needed
#             print(f"you drive {distance} km. Fuel left {self.fuel}")
#         else:
#             print("Not enough fuel to drive")
      
        
        
#     def refuel(self, amount):
#         self.fuel += amount
#         print(f"car refueled by {amount}. Total fuel: {self.fuel}")
        
# my_car = Car("Ford", "Mustang", 10)
# my_car.drive(8)
# my_car.refuel(5)


#  Create a ToDoList class
# class to_Do_List:
#     def __init__(self,title, status):
#         self.title = title
#         self.status = status
        
#     def addtask(self):
#         date = int(input("please enter a date : "))
#         task = input("please enter your task for taoday: ")
#         self.title += task
#         return self.title
        
#     def removetask(self):
#         remove_task = input("Please enter a task that you wnat remove from your todolist: ")
#         self.title -= remove_task
#         return self.title
    
# my_todolist = to_Do_List("study", "check")
# print(my_todolist.addtask())
# print(my_todolist.removetask())



class ToDoList:
    def __init__(self):
        self.tasks = []   # list to store tasks

    def addtask(self):
        task = input("Enter a task: ")
        self.tasks.append(task)
        print("Task added!")

    def removetask(self):
        task = input("Enter task to remove: ")
        if task in self.tasks:
            self.tasks.remove(task)
            print("Task removed!")
        else:
            print("Task not found!")

    def showtasks(self):
        print("Your To-Do List:")
        for task in self.tasks:
            print("-", task)


my_todolist = ToDoList()

my_todolist.addtask()
my_todolist.addtask()
my_todolist.showtasks()
my_todolist.removetask()
my_todolist.showtasks()
