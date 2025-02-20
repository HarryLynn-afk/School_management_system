class Student:
    def __init__(self, name, age, grade, student_id):
        self.name = name
        self.age = age
        self.grade = grade
        self.student_id = student_id

    def __repr__(self):
        return f"Student(name='{self.name}', age= {self.age}, grade ='{self.grade}', student_id={self.student_id})"