class Student:

    def __init__(self, name, surname, course):
        self.name = name
        self.surname = surname
        self.course = course
        self.grades = {}

    def add_grade(self, discipline, grade):
        self.grades[discipline] = grade
        return f'{self.name} {self.surname} получил итоговую оценку: {grade}. Предмет: {discipline}'

    def display_all_grades(self):
        if not self.grades:
            print(f'У студента {self.name} {self.surname} оценок нет.')
        else:
            print(f'Оценки студента {self.name} {self.surname}')
            for discipline, grade in self.grades.items():
                print(f"Предмет: {discipline} >> {grade}")

    def __str__(self):
        return f'Cтудент {self.name} {self.surname}. Курс: {self.course}'


if __name__ == '__main__':
    # student_name = "Иван"
    # student_surname = "Иванов"
    # student_course = "QA"
    #
    # student = Student(student_name, student_surname, student_course)
    # print(student)
    # print(student.add_grade('Ручное тестирование', 10))
    # print(student.add_grade('Системное администрирование', 11))
    # print(student.add_grade('Основы программирования на Python', 12))
    #
    # student.display_all_grades()

    student_matrix = [
        ['name', 'surname', 'discipline'],
        ["Петр", "Петров", "JS"],
        ["Владимир", "Владимиров", "Databases"],
        ["Дмитрий", "Леонов", "Tests"],
    ]

    student_objects = []

    for name, surname, course in student_matrix[1:]:
        student_objects.append(Student(name, surname, course))

    print(student_objects)
    for student in student_objects:
        print(student)
