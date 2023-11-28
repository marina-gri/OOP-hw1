class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lect(self, lecturer, course, grade):
        if 0 < grade <= 10:
            if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached_lect and course in self.courses_in_progress:
                if course in lecturer.lecturer_grades:
                    lecturer.lecturer_grades[course] += [grade]
                else:
                    lecturer.lecturer_grades[course] = [grade]
            else:
                return 'Ошибка'
        else:
            return "Оценка вне допустимого диапозона"

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached_lect = []
        self.lecturer_grades = {}

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if 0 < grade <= 10:
            if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
                if course in student.grades:
                    student.grades[course] += [grade]
                else:
                    student.grades[course] = [grade]
            else:
                return 'Ошибка'
        else:
            return "Оценка вне допустимого диапозона"


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

# cool_mentor = Mentor('Some', 'Buddy')
# cool_mentor.courses_attached += ['Python']

# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)

reviewer1 = Reviewer('Igor', 'Petrov')
reviewer1.courses_attached += ['Python']

reviewer1.rate_hw(best_student, 'Python', 10)
reviewer1.rate_hw(best_student, 'Python', 10)
reviewer1.rate_hw(best_student, 'Python', 10)

lect1 = Lecturer('Sergey', 'Ivanov')
lect1.courses_attached_lect += ['Python']
best_student.rate_lect(lect1, 'Python', 8)
best_student.rate_lect(lect1, 'Python', 10)
best_student.rate_lect(lect1, 'Python', 7)
best_student.rate_lect(lect1, 'Python', 9)

print(best_student.name, best_student.surname)
print(best_student.grades)

print(f'Лектор: {lect1.name} {lect1.surname} читает курсы: {(", ").join(lect1.courses_attached_lect)}')
print(lect1.lecturer_grades)
