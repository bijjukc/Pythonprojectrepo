
# functions
# check the nums  is prime 


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




# Write a funciton to find a factorail of a num

# def fact_num(num):
#     result = 1
#     for i in range(num, 0, -1):
#         result *= i
#     return result
        
# print(fact_num(5))



# Classes and Objects

class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name 
        self.roll_no = roll_no
        self.marks = marks
        
    def display(self):
        print("My name is" , self.name , " and  the studnet roll no is " , self.roll_no , "and got makrs :" , self.marks)
    
info = Student("Biaya", 1, 98)
info.display()
   