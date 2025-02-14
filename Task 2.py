class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def introduce(self):
        print(f"Hello, my name is {self.name}, I am {self.age} years old, and I am studying {self.course}.")


student1 = Student("Angel", 21, "Computer Science")
student2 = Student("John Marciso", 22, "Criminology")
student3 = Student("Jefferson", 19, "Engineering")


student1.introduce()
student2.introduce()
student3.introduce()

