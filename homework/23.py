class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_pass(self):
        return self.marks >= 40
count = 0

try:
    with open("students.txt", "r") as file:
        for line in file:
            try:
                name, marks = line.strip().split(",")
                marks = int(marks)

                s = Student(name, marks)

                if s.is_pass():
                    count += 1

            except ValueError:
                # Ignore invalid marks (e.g., abc)
                continue

    print(count)
except FileNotFoundError:
    print("File Not Found")

