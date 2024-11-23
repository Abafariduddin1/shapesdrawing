class Student:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
    def birthyr(self):
        print(2024-self.age)

    

student = Student("Alice", 13, 5.2, 34)
student2 = Student("Bob", 13, 5.5, 46)



print(student.name, student.age, student.height, student.weight)
print(student2.name, student2.age, student2.height, student2.weight)
student.birthyr()
