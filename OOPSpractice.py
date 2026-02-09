# 1. Create a Studnet class with name, roll number and marks 

class Student:
    def __init__(self, name, roll_no,marks):
        self.name = name 
        self.roll_no = roll_no
        self.marks = marks
        
    def print_Studnet_info (self ):
        print(f"Student name is {self.name}, her roll number is {self.roll_no}, and she scored {self.marks} grade in 1st Sem")
        
    def topper(self):
        max_marks = 100
        min_marks = 85
        if self.marks >= min_marks and self.marks <=max_marks:
            print("She topped the university")
        
        
student1 = Student("Bijaya", 1 , 96 )
student2 = Student("Manish", 2 , "A" )

student1.print_Studnet_info()
student1.topper()
student2.print_Studnet_info()


# 2. Create a BankAccount class with deposit and withdraw functionality

class BankAccount:
    def __init__(self,name , balance):
        self.name = name
        self.balance = balance
        
    def deposit(self,amount):
        self.balance += amount
        print(f"After deposit total balnce is {self.balance}")
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Your total balance is now {self.balance}, atfer you withdraw ")
        else:
            print("your balance is not enough to withdraw")
        
        
        
        
my_bank_balance = BankAccount("Bijaya", 10000)
my_bank_balance.deposit(10000)
my_bank_balance.withdraw(25000)


#  Create a Car class with attributes like brand, model and fuel level

class Car:
    def __init__(self, brand , model, fuel):
        self.brand = brand
        self.model = model 
        self.fuel = fuel
        
    def show_car_details(self):
        print(f"My friend bought a car and car brand name is {self.brand}, and the model is {self.model}")
        
        
    def fuel_level(self, distance):
        drive = distance * 0.2
        if self.fuel <= drive:
           
            print (f"fuel level is less now , you have to refill it otherwise you would be in trouble")
            
        else:
            print("Fuel is enough to drive")
            
            
car1 = Car("Tyota", "Fortuner", 100)
car1.show_car_details()
car1.fuel_level(500)


# OOPS Intermediate questions

# Create a StudnetReport class to calcu;ate grade and percentage 

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


# Create a ShoppingCart class to add, remove and calculate total price
class ShoppingCart:
    def __init__ (self):
        self.items = {} # item_name : price
        
    def addItems(self, name , price):
        self.items[name] = price
        print(f" {name} added to cart")
        
         
        
    def removeItems(self, name):
        if name in self.items:
            del self.items[name]
            print(f" {name} removed from cart")
        else:
            print("Sorry ,item not found in cart")
            
    def total_price(self):
        total = 0
        for price in self.items.values():
            total += price
        return total
                


cart = ShoppingCart()
cart.addItems("Noodles", 70)
cart.addItems("Apple", 20)
cart.addItems("Rice", 100)
cart.removeItems("Noodles")
print(cart.total_price())


# Create a MovieTicket class to book and cancel tickets

class MovieTicket:
    def __init__(self,show,price,time):
        self.show = show
        self.price = price
        self.time = time
        self.tickets = 0
        self.is_booked = False
    
    def book_show(self, number):
        if self.show == "3 idiots" and self.time == "3 PM":
            self.tickets += number
            self.is_booked = True
            print(f"{number} tickets booked successfully")
        else:
            print("Show is not availaible today")
    
    def total_price(self):
        if self.is_booked:
            return self.tickets * self.price
        else:
         return 0
     
    def cancel_ticket(self):
        if self.is_booked:
            self.tickets = 0
            self.is_booked = False
        
            print("Tickets cancelled successfully")
        else:
            print("No tickets booked to cnacel")
        


movie = MovieTicket("3 idiots" ,100,  "3 PM")
movie.book_show(3)
print(movie.total_price())
movie.cancel_ticket()



#  Create a Wallet class to add money and spend money 

class Wallet:
    def __init__(self):
        self.money = 0
    def add_money(self, amount):
        self.money += amount
        print(f"You have {self.money} money in your wallet")
    
    def spend_money(self, amount):
        if self.money >= amount:
          self.money -=amount
          print(f"After you spend {amount}, you have {self.money} left in your wallet now")
        else:
            print("Insufficient money in your wallet to spend")
        


my_wallet = Wallet()
my_wallet.add_money(1000)
my_wallet.spend_money(1500)