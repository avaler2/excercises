a1 = 1200
a2 = 1500.04
A2 = 123.44
a3 = "Hello world"
studentName = "Przemysław Polański"
#this is a special formula for calculting something
result = a1+a2*a2

testResult = 5 < 2

import random

#print(random.randrange(1, 100))

longtext = """It will be 
a really 
long text
and I hope
it will span
a few lines """


myList = [12, 34, 55, 44, 33, 543, 33]
print(myList)

def printListOneByOne():
    for x in myList:
        print("Number is: " + str(x))


printListOneByOne()

class Employee():
    name = "Sebastian"
    surname = "Kowalski"
    def printName(self):
        print("My name is Sebastian.")

newEmp = Employee()
newEmp.printName()
print(newEmp.name)
