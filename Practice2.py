
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

class Car:
    def __init__(self, make,model, fuel):
        self.make = make
        self.model = model
        self.fuel = fuel
        
    def drive(self, distance):
        
        fuel_needed = distance * 0.2
        if self.fuel >= fuel_needed:
            self.fuel -= fuel_needed
            print(f"you drive {distance} km. Fuel left {self.fuel}")
        else:
            print("Not enough fuel to drive")
      
        
        
    def refuel(self, amount):
        self.fuel += amount
        print(f"car refueled by {amount}. Total fuel: {self.fuel}")
        
my_car = Car("Ford", "Mustang", 10)
my_car.drive(8)
my_car.refuel(5)