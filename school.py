class School:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def show_students(self):
        for student in self.students:
            print(student)

    def update_student(self, student_id, new_grade=None):
        for student in self.students:
            if student.student_id == student_id:
                if new_grade:
                    student.grade = new_grade
                return
        print(f"Student with ID {student_id} not found.")

    def remove_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                return
        print(f"Student with ID {student_id} not found.")