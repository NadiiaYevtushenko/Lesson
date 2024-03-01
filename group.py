class Group:
    def __init__(self, number):                                     # визначення функції (попередні дані )
        self.number = number
        self.group = []

    def add_student(self, student):                                # визначення функції (попередні дані )
        if len(self.group) >= 10:
            raise Just10Student("This group already has 10 students")
        self.group.append(student)

    def delete_student(self, last_name):                           # визначення функції (попередні дані )
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def find_student(self, last_name):                             # визначення функції (попередні дані )
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):                                             # вивід інфо по групі
        all_students = '\n'.join(str(student) for student in self.group)
        return f'Group: {self.number}\n{all_students}'