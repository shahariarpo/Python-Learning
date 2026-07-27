class Student:
    # class variables are outside the constructor
    class_year = 2026
    num_students = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.num_students += 1

student1 = Student("Peter Parker", 3.96)
student2 = Student("Stephen Strange", 4.0)
student3 = Student("Natasha Romanoff", 2.72)

print(f"Number of students: {Student.num_students}")

print(student1.name)
print(student2.name)
print(student3.name)

