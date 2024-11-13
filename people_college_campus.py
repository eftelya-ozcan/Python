class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Address: {self.address}")


class Faculty(Person):
    def __init__(self, name, age, address, department, title):
        super().__init__(name, age, address)
        self.department = department
        self.title = title

    def display_info(self):
        super().display_info()
        print(f"Department: {self.department}, Title: {self.title}")

    def teach_class(self):
        print(f"{self.name} is teaching a class in the {self.department} department")


class Staff(Person):
    def __init__(self, name, age, address, position, office_location):
        super().__init__(name, age, address)
        self.position = position
        self.office_location = office_location

    def display_info(self):
        super().display_info()
        print(f"Position: {self.position}, Office Location: {self.office_location}")

    def work(self):
        print(f"{self.name} is working as a {self.position} at {self.office_location}")

    
class Student(Person):
    def __init__(self, name, age, address, major, year):
        super().__init__(name, age, address)
        self.major = major
        self.year = year

    def display_info(self):
        super().display_info()
        print(f"Major: {self.major}, Year: {self.year}")

    def attend_class(self):
        print(f"{self.name} is attending a class as a {self.year} year student majoring in {self.major}")


faculty_member = Faculty("Dr. Smith", 45, "123 University Ave", "Computer Science", "Professor")
staff_member = Staff("Alice Johnson", 37, "456 Campus Rd", "Librarian", "Library")
student_member = Student("John Doe", 20, "789 Dorm St", "Biology", "Sophomore")

# Displaying information for each person and calling their specific methods
print("Faculty Information:")
faculty_member.display_info()
faculty_member.teach_class()

print("\nStaff Information:")
staff_member.display_info()
staff_member.work()

print("\nStudent Information:")
student_member.display_info()
student_member.attend_class()
