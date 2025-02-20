from school import School
from student import Student

# Create a School object
my_school = School("Westwood Academy")

# Create Student objects
student1 = Student("Alice", 14, "8th", 101)
student2 = Student("Bob", 15, "9th", 102)
student3 = Student("Charlie", 13, "7th", 103)
student4 = Student("David", 16, "10th", 104)
student5 = Student("Eva", 15, "9th", 105)

# Add students to the school
my_school.add_student(student1)
my_school.add_student(student2)
my_school.add_student(student3)
my_school.add_student(student4)
my_school.add_student(student5)

# Display all students
print("\nAll students:")
my_school.show_students()

# Update a student's details
print("\nUpdating Bob's grade to 10th...")
my_school.update_student(102, new_grade="10th")

# Remove a student
print("\nRemoving Charlie...")
my_school.remove_student(103)

# Display
print("\nAll students after update and removal:")
my_school.show_students()