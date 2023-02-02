#Basics of artithmetics
a1 = 345
a2 = 456
a3 = a1 / a2
#print(a3)

#Basics of function definition and function calls
def showDivision(num1, num2):
    result = num1 / num2
    print("The result of the division is: " + str(result))
    print(result)

#showDivision(23,44)
#showDivision(5666,443)
#showDivision(433, 555)

#Basics of string manipulation
longText = """This is my first
very long
poem
on the power
of Python"""
#print(longText)
print(longText[-1])


#Lists 
anotherList = [23, 33, 55, 443, 554]
a4 = [23, 555, 2, 3, 55, 3, 555, 55, 3, 5, 3, 555, 3, "What", "is", longText, anotherList] 
print("The element's value is: " + str(a4[-1][3]) + " and the length of the list is: " + str(len(a4)))

for temp in a4:
    if temp == 555:
        print("Hurra, I found a triple 5!")
    else:
        print(temp)


#Dictionary
dict1 = {"name": "Przemysław", "surname": "Polański", "email": "polanski@kozminski.edu.pl"}
print(dict1)
print(dict1["email"])

#classes
class Employee():
    #constructor - based on "dunder"
    def __init__(self, name, surname, email):
        self.name = name
        self.surname = surname
        self.email = email

    def print_name(self):
        return ("My name is PPP or: " + self.name + " " + self.surname)

class Teachers(Employee):

    def print_name(self):
        return super().print_name()

emp1 = Employee("Przemysław", "Polański", "polanski@kozminski.edu.pl")
emp2 = Employee("Anna", "Rudzka", "anna@kozminski.edu.pl")
emp3 = Employee("Janusz", "Walczak", "janusz.walczak@ddd.com")
print(emp1.email)
print(emp2.surname)
print(emp3.email)
print(emp2.print_name())
