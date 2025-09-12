class Student:
    def __init__(self, name, grade, department):
        # Initialize attributes
        self.name = name
        self.grade = grade
        self.department = department

    def print_info(self):
        # Print student information
        print(f"Name: {self.name}, Grade: {self.grade}, Department: {self.department}")

    def update_grade(self, new_grade):
        # Update the student's grade
        self.grade = new_grade


if __name__ == "__main__":
    # Create student instances and demonstrate functionality
    student1 = Student("Alice", "A", "Computer Science")
    student2 = Student("Bob", "B", "Mathematics")
    student3 = Student("Charlie", "C", "Physics")

    totalStudents = [student1, student2, student3]

    print("=== Initial Student Records ===")
    for student in totalStudents:
        student.print_info()

    print("\n=== Updating Bob's Grade to D  ===")
    student2.update_grade("D")
    student2.print_info()

    print("\n=== Final Student Records ===")
    for student in totalStudents:
        student.print_info()


