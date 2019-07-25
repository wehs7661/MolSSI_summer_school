class Student:
    def __init__(self, name, surname, age, gender):
        self.name = name
        self.surname = surname
        self.age = age
        self.gender = gender
        self.courses = []

    # write an enrollment method that takes in a course and adds it to the student courses
    def add_courses(self, courses):
        if isinstance(courses, list):
            self.courses.extend(courses) 
        else:
            self.courses.append(courses) 
    
    def __str__(self):
        return 'name: ' + self.surname + ', ' + self.name + '\ncourses: ' + str(self.courses)


class Faculty:
    def __init__(self, name, surname, age, gender, position):
        self.name = name
        self.surname = surname
        self.age = age
        self.gender = gender
        self.courses = []
        self.position = position

    def assign_course(self, courses):
        self.courses.append(courses)

    def __str__(self):
        return 'name: ' + self.surename + ', ' +self.name + '\ncourses: ' + str(self.courses)


def main():
    student1 = Student('William', 'Hsu', 25, 'Male')
    print(student1.courses)
    student1.add_courses('Math')
    print(student1.courses)
    student1.add_courses(['Biology', 'Computer Science'])
    print(student1.courses)

    print(student1)

if __name__ == '__main__':
    main()
