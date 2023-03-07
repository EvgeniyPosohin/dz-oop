class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def set_grades(self, lecture, course, grade):
        if isinstance(lecture, Lecturer) \
                and course in self.courses_in_progress \
                and course in lecture.courses_attached \
                and 0 <= grade <= 10:
            if course in lecture.grades:
                lecture.grades[course] += [grade]
            else:
                lecture.grades[course] = [grade]
        else:
            print('Не принадлежит классу или нет общих курсов')

    def __str__(self):
        txt = f'Имя: {self.name}\n'\
              f'Фамилия: {self.surname}\n'\
              f'Средняя оценка за Д/з: {grades(self):.1f}\n'\
              f'Курсы в процессе изучения: {self.courses_in_progress}\n'\
              f'Завершенные курсы: {self.finished_courses}'
        return txt


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        txt = f'Имя: {self.name}\n'\
              f'Фамилия: {self.surname}\n'\
              f'Средняя оценка за лекции: {grades(self):.1f}'
        return txt

    # можно объявить до класса from functools import total_ordering
    # @total_ordering
    def __ge__(self, other):
        return grades(self) >= grades(other)

    def __le__(self, other):
        return grades(self) <= grades(other)

    def __lt__(self, other):
        return grades(self) < grades(other)

    def __gt__(self, other):
        return grades(self) > grades(other)


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) \
                and course in self.courses_attached \
                and course in student.courses_in_progress\
                and 0 <= grade <= 10:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            print('Ошибка')

    def __str__(self):
        txt = f'Имя: {self.name}\n'\
              f'Фамилия: {self.surname}'
        return txt


# вынес за классы функцию по подсчёту средней оценки за д/з,
# теперь её могу вызывать в обоих классах.
def grades(self):
    grade_self = [sum(i) / len(i) for i in self.grades.values()]
    return sum(grade_self)/len(grade_self)


# функция работает со студентами и лекторами
def count_grades(students, cours):
    list_grades = []
    for student in students:
        if cours in student.grades.keys():
            grade_self = sum(student.grades[cours])/len(student.grades[cours])
            list_grades.append(grade_self)
        else:
            continue
    if list_grades:
        return round(sum(list_grades) / len(list_grades), 2)
    else:
        return 'ошибка в запросе: нет курса или оценок'


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student_2 = Student('Иван', 'Иванов', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student_2.courses_in_progress += ['Python']

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

cool_mentor.rate_hw(best_student_2, 'Python', 8)
cool_mentor.rate_hw(best_student_2, 'Python', 8)
cool_mentor.rate_hw(best_student_2, 'Python', 7)


reviewer = Reviewer('Василий', 'Пупкин')

cool_lectore = Lecturer('Петр', 'Петров')
cool_lectore.courses_attached += ['Python']
cool_lectore_2 = Lecturer('Семён', 'Семенов')
cool_lectore_2.courses_attached += ['Python']

best_student.set_grades(cool_lectore, 'Python', 8)
best_student.set_grades(cool_lectore, 'Python', 10)
best_student.set_grades(cool_lectore, 'Python', 10)

best_student.set_grades(cool_lectore_2, 'Python', 8)
best_student.set_grades(cool_lectore_2, 'Python', 9)
best_student.set_grades(cool_lectore_2, 'Python', 9)

List_lector = [cool_lectore, cool_lectore_2]
list_sudent = [best_student, best_student_2]
print(f'средняя оценка по студентам- {count_grades(list_sudent, "Python")}')
print(f'средняя оценка по лекторам- {count_grades(List_lector, "Python")}')
print(cool_lectore >= best_student)
print(best_student)
print(cool_lectore.grades)
