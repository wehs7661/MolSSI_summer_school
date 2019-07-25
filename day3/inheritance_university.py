class Person:
    def __init__(self, name, surname, age, gender):
        self.name = name
        self.surname = surname
        self.age = age
        self.gender = gender
        self.id = self.generate_id() # call a method defined below in __init__
        self.courses = []

    def generate_id(self):
        id_hash = 0
        for s in self.name:
            id_hash += ord(s)
        for s in self.surname:
            id_hash += ord(s)
        id_hash = id_hash % 100000000

        return id_hash

    
    def __str__(self):
        return 'name: ' + self.surname + ', ' + self.name + '\ncourses: ' + str(self.courses)

class Student(Person):  # so the class Person is the "parent class" of the class Student
    def __init__(self, name, surname, age, gender):
        super().__init__(name, surname, age, gender)    
        # super() is used to look up the methods in the parent class

# Practice: edit the faculty class to use person as a parent class
class Faculty(Person):
    def __init__(self, name, surname, age, gender, position):
        super().__init__(name, surname, age, gender)  # inherit from the parent course, which have these 4 arguments
        self.position = position
        
        self.courses = []
    
    def assign_course(self, coursename):
        self.courses.append(coursename)

student1 = Student("William", "Hsu", 25, "Male")
print(student1)
print(student1.generate_id())
print(student1.__dict__)

faculty1 = Faculty("Michael", "Shirts", 40, "Male", "Assocaite Professer")
print(faculty1)
faculty1.assign_course('Math')
print(faculty1.__dict__)
