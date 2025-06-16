class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    def is_passing(self):
        return self.grade >= 50

    def __str__(self):
        return f"Student: {self.name}, Age: {self.age}, Grade: {self.grade}"
        
        

s1 = Student("Jack", 14, 98)
print(s1)
print(s1.is_passing())