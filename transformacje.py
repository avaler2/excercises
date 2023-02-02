class Person:

    name = "Paul"

    def __init__(self, name, surname, email):
        self.imie = name
        self.nazwisko = surname
        self.email = email

class Student(Person):
    def __init__(self, name, surname, email, subjects):
        super().__init__(name, surname, email)
        self.subjects = subjects

class Teacher(Person):
    def __init__(self, name, surname, email, specialisation):
        super().__init__(name, surname, email)
        self.spec = specialisation


student1 = Student("Przemysław", "Polański", "polanski@kozminski.edu", "Transformacje")
student2 = Student("Anna", "Mikołajek", "mmmm@mikok.pl", "Transformacje")
student3 = Student("Andrzej", "Wiśniewski", "aaa@lll.com", "Transformacje")
student4 = Student("Joanna", "Wielgus", "anaa@lll.com", "Transformacje")
print(student1.imie)
print(student2.imie)
print(student3.email)
print(student4.subjects)

teacher1 = Teacher("Anna", "Dombek", "adombek@gamil.com", "Teacher of coding")
print(teacher1.spec)
print(teacher1.name)

