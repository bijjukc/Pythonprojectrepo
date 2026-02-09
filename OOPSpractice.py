# 1. Create a Studnet class with name, roll number and marks 

# class Student:
#     def __init__(self, name, roll_no,marks):
#         self.name = name 
#         self.roll_no = roll_no
#         self.marks = marks
        
#     def print_Studnet_info (self ):
#         print(f"Student name is {self.name}, her roll number is {self.roll_no}, and she scored {self.marks} grade in 1st Sem")
        
#     def topper(self):
#         max_marks = 100
#         min_marks = 85
#         if self.marks >= min_marks and self.marks <=max_marks:
#             print("She topped the university")
        
        
# student1 = Student("Bijaya", 1 , 96 )
# # student2 = Student("Manish", 2 , "A" )

# student1.print_Studnet_info()
# student1.topper()
# student2.print_Studnet_info()


# 2. Create a BankAccount class with deposit and withdraw functionality

# class BankAccount:
#     def __init__(self,name , balance):
#         self.name = name
#         self.balance = balance
        
#     def deposit(self,amount):
#         self.balance += amount
#         print(f"After deposit total balnce is {self.balance}")
    
#     def withdraw(self, amount):
#         if self.balance >= amount:
#             self.balance -= amount
#             print(f"Your total balance is now {self.balance}, atfer you withdraw ")
#         else:
#             print("your balance is not enough to withdraw")
        
        
        
        
# my_bank_balance = BankAccount("Bijaya", 10000)
# my_bank_balance.deposit(10000)
# my_bank_balance.withdraw(25000)


#  Create a Car class with attributes like brand, model and fuel level

# class Car:
#     def __init__(self, brand , model, fuel):
#         self.brand = brand
#         self.model = model 
#         self.fuel = fuel
        
#     def show_car_details(self):
#         print(f"My friend bought a car and car brand name is {self.brand}, and the model is {self.model}")
        
        
#     def fuel_level(self, distance):
#         drive = distance * 0.2
#         if self.fuel <= drive:
           
#             print (f"fuel level is less now , you have to refill it otherwise you would be in trouble")
            
#         else:
#             print("Fuel is enough to drive")
            
            
# car1 = Car("Tyota", "Fortuner", 100)
# car1.show_car_details()
# car1.fuel_level(500)


# OOPS Intermediate questions

# Create a StudnetReport class to calcu;ate grade and percentage 

# class StudentReport:
#     def __init__(self, name, roll_no,marks):
#         self.name = name 
#         self.roll_no = roll_no
#         self.marks = marks
     
    
    
#     def calculate_grade(self,subjects):
#         subjects += self.marks
        
#         return subjects
#     #    sub_marks = subjects.append(self.marks)
    
    
        

#         # if self.marks <= 100 or self.marks >=85:
#         #     print("Grade : A")
#         # elif self.marks < 85 or self.marks >= 75:
#         #     print()
        
#     # def percentage (self):
#     #     total_percentage = 
        
        
# student = StudentReport("Bijaya", 2, [90,80,85,75,86])
# print(student.calculate_grade( ["physics ", "biology", "chemistry", "Math", "English" ]))



class StudentReport:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks  # list of marks

    def calculate_percentage(self):
        total_marks = sum(self.marks)
        number_of_subjects = len(self.marks)
        percentage = total_marks / number_of_subjects
        return percentage

    def calculate_grade(self):
        percentage = self.calculate_percentage()

        if percentage >= 85:
            return "A"
        elif percentage >= 75:
            return "B"
        elif percentage >= 60:
            return "C"
        else:
            return "Fail"

    def print_report(self):
        percentage = self.calculate_percentage()
        grade = self.calculate_grade()

        print(f"Student Name: {self.name}")
        print(f"Roll Number: {self.roll_no}")
        print(f"Percentage: {percentage:.2f}%")
        print(f"Grade: {grade}")


student = StudentReport("Bijaya", 2, [90, 80, 85, 75, 86])
student.print_report()
