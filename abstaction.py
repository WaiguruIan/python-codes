#Adm NO: BSCIT-05-0096\2024
#Name: Ian Waiguru
from abc import ABC, abstractmethod # This must be at the top to import the module of abstract
#class Vehicle(ABC):
#   @abstractmethod 
#   def_start_engine(self):
#       pass

#class Car(Vehicle):
 #   def start_engine(self):

from abc import ABC, abstractmethod  # Import the ABC module for abstract classes

class Employee(ABC):
    def __init__(self, name, salary):
        self.__name = name  # Private attribute
        self.__salary = salary  # Private attribute

    def display_info(self):
        print("Name:", self.__name)  # Access the private name attribute

    def get_salary(self):
        return self.__salary  # Access the private salary attribute

    @abstractmethod
    def calculate_salary(self):
        pass


class FullTimeEmployee(Employee):
    def calculate_salary(self):
        return self.get_salary()  # Access the salary using the parent class method


class PartTimeEmployee(Employee):
    def calculate_salary(self):
        half_salary = self.get_salary() * 0.5  # Calculate half salary
        return half_salary


# Create instances of the subclasses
emp1 = PartTimeEmployee("Ian", 20000)
print(emp1.calculate_salary())  # Output: 10000.0
emp1.display_info()  # Output: Name: Ian

emp2 = FullTimeEmployee("Martin", 20000)
print(emp2.calculate_salary())  # Output: 20000
emp2.display_info()  # Output: Name: Martin

employees = [emp1, emp2]

# Loop to call methods
for emp in employees:
    emp.display_info()
    print(f"Calculated Salary: {emp.calculate_salary()}")

