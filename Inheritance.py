#  INHERITANCE PRACTICE 
# Create a base class Person and chils Car and Bike

class Person:
    def __init__(self,name,age,height):
        self.name = name 
        self.age = age
        self.height = height
        
    def show_details(self):
        print(f"Name : {self.name}, age : {self.age}, height: {self.height}")
   
class Student(Person):
    def __init__(self,name, age ,height,student_id, grade):
       super().__init__(name,age,height)  #calls the base class constructor
       self.student_id = student_id
       self.grade = grade
   
    def display_student(self):
        self.show_details() #use method from base class
        print(f"Studnet ID : {self.student_id}, Grade : {self.grade}")
        
    
class Teacher(Person):
    def __init__(self, name , age , height,subject, salary ):
        super().__init__(name, age, height)
        self.subject = subject
        self.salary = salary
        
    def display_teacher(self):
        self.show_details()
        print(f"Subject : {self.subject}, Salary : {self.salary}")
        
        
        
s1 = Student("Bijaya", 30, 5.8, "S123", "A" )
s1.display_student()

t1 = Teacher("Manish", 34, 5.8,"Math", 51000)
t1.display_teacher()



# Create a base class Vehicle and child classes Car and Bike

class vehicle:
    def __init__(self, color, milage, brand):
        self.color = color
        self.brand = brand
        self.milage = milage
        
    def car_info(self):
        print(f"Color:  {self.color}, Brand : {self.brand} ,Milage : {self.milage}" )
            
            
            
class car(vehicle):
    def __init__(self,color, brand , milage , model):
        super().__init__(color,brand, milage)
        self.model = model 
        
    def show_car_details(self):
        self.car_info()
        print(f"Model : {self.model}")
    
    
class Bike(vehicle):
    def __init__(self, color,milage , brand, name, ):
        super().__init__(color, milage, brand)
        self.name = name
        
    def bike_details(self):
        self.car_info()
        print(f"Name of the bike : {self.name}")
        
        
car1 = car("Red", "Toyota" , 300 , "Fortuner")
car1.show_car_details()
print("")
bike1 = Bike("Black", 200, "Honda", "Dio")
bike1.bike_details()