import random
# -*- coding: utf-8 -*-
# views.py
from django.views.generic.base import TemplateView
# Раздел описания классов


class Student:
    # id, person, group, age
    def __init__(self, student_id, person, group, age):
        # Конструктор класса Student
        self.student_id = student_id
        self.person = person
        self.group = group
        self.age = age
    pass


class Subject:
    # subject_id, name
    def __init__(self, subject_id, name):
        # Конструктор класса Subject
        self.subject_id = subject_id
        self.name = name
    pass


class Score:
    # student_id, subject_id, value
    def __init__(self, student_id, subject_id, value):
        # Конструктор класса Score
        self.student_id = student_id
        self.subject_id = subject_id
        self.value = value
    pass


class Person:
    def __init__(self, name, surname, patronymic):
        # Конструктор класса Person
        self.name = name
        self.surname = surname
        self.patronymic = patronymic

    def get_fio(self):
        return self.surname + self.name + self.patronymic
    pass
# Задание списка из ФИО студентов
names = ['Danil ', 'Timur ', 'Kunnei ', "Al'bina ", 'Ilona ']
surnames = ['Zaripov ', 'Koyshinov ', 'Tomskaya ', 'Oun ', 'Sagalakova ']
patronymics = ["Valer'evich", 'Samatuli', 'Martovna', 'Andreevna', "Vasil'evna"]
students_fio = []
for i in range(len(names)):
    students_fio.append(Person(names[i], surnames[i], patronymics[i]))
# Задание списка из преподаваемых предметов
subjects_example = ['timp', 'EiS', 'philosophy', 'english', 'sport']
subjects = []
for i in range(len(subjects_example)):
    subjects.append(Subject(i, subjects_example[i]))
# Задание списка с полной информацией о студентах
students_other_information = []
for i in range(len(names)):
    students_other_information.append(Student(i, students_fio[i], 743, 19))
# Задание списка успеваемости студентов
scores = []
for student_id in range(len(names)):
    for subject_id in range(len(subjects)):
        scores.append(Score(student_id, subject_id, random.randint(1, 5)))
# Задание списка средних баллов студентов
average_scores = []
average_score = 0.0
# Так как успеваемость студентов можно представить как двумерный массив, то
# для вычисления среднего балла по дисциплинам, мы должны пройтись по каждому студенту(по каждой строке)
# и после перейти на следующую строку
# average_score += scores[<номер студента(от 0 до 4)>*<количество предметов>+<номер текущего предмета>]
for student_id in range(len(names)):
    for subject_id in range(len(subjects_example)):
        average_score += scores[student_id*len(subjects_example)+subject_id].value
    average_scores.append(average_score/len(subjects_example))
    average_score = 0.0
# Зададим список из словарей
students_statistics = []
for student_id in range(len(names)):
    student_info = {
        'id': student_id+1,
        'fio': students_fio[student_id].get_fio(),
        'timp': scores[student_id*len(subjects_example)].value,
        'eis': scores[student_id*len(subjects_example) + 1].value,
        'philosophy': scores[student_id*len(subjects_example)+2].value,
        'english': scores[student_id*len(subjects_example)+3].value,
        'sport': scores[student_id*len(subjects_example)+4].value,
        'average': average_scores[student_id]
    }
    students_statistics.append(student_info)
# Зададим строки из отличников и отчисляемых
bad_students = ''
excellent_students = ''
for student_id in range(len(names)):
    if average_scores[student_id] > 4.5:
        # Если строка не пустая, то добавляем запятую впереди ФИО
        # Иначе запятую в начало строки не ставим, а добавляем только ФИО
        if len(excellent_students) > 0:
            excellent_students += ' ,' + students_fio[student_id].get_fio()
        else:
            excellent_students += students_fio[student_id].get_fio()
    elif average_scores[student_id] < 3:
        if len(bad_students) > 0:
            bad_students += ', ' + students_fio[student_id].get_fio()
        else:
            bad_students = students_fio[student_id].get_fio()


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update(
            {
                'students_statistics': students_statistics,
                'excellent_students': excellent_students,
                'bad_students': bad_students
            }
        )
        return context