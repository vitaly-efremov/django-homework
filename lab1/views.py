import random
# -*- coding: utf-8 -*-
from django.views.generic.base import TemplateView

class Student:
    def __init__(self, student_id, person, group, age):
        self.student_id = student_id
        self.person = person
        self.group = group
        self.age = age
    pass

class Subject:
    def __init__(self, subject_id, name):
        self.subject_id = subject_id
        self.name = name
    pass

class Score:
    # Subject,
    def __init__(self, student_id, subject_id, value):
        self.student_id = student_id
        self.subject_id = subject_id
        self.value = value
    pass

students = []
students.append(Student(0, 'Бугоркова Алиса', 724, 19))
students.append(Student(1, 'Воронин Александр', 773, 20))
students.append(Student(2, 'Генке Елизавета', 723, 19))
students.append(Student(3, 'Дё Вера', 764, 18))
students.append(Student(4, 'Ерофеева Жанна', 763, 19))
students.append(Student(5, 'Жибинов Андрей', 773, 20))
students.append(Student(6, 'Захаров Вадим', 773, 20))
students.append(Student(7, 'Иконникова Мария', 723, 20))
students.append(Student(8, 'Кострамикин Роман', 764, 19))
students.append(Student(9, 'Лимбах Влад', 763, 20))

subjects = []
subjects.append(Subject(0, 'ТиМП'))
subjects.append(Subject(1, 'ЭиС'))
subjects.append(Subject(2, 'Философия'))
subjects.append(Subject(3, 'Иностранный язык'))
subjects.append(Subject(4, 'Физическая культура'))

scores = []
for i in range(len(students)):
    for j in range(len(subjects)):
        scores.append(Score(i, j, random.randint(2, 5)))

score_summa = .0
average = []
for i in range(len(students)):
    for j in range(len(subjects)):
        score_summa += scores[i*len(subjects)+j].value
    average.append(score_summa/len(subjects))
    score_summa = .0

summa = .0
sred_ar = []
for i in range(len(subjects)):
    for j in range(len(students)):
        summa += scores[j*len(subjects)+i].value
    sred_ar.append(summa/len(students))
    summa = .0

excellent_students = ''
bad_students = ''
for i in range(len(students)):
    if average[i] > 4.5:
        if len(excellent_students) > 0:
            excellent_students += ', ' + students[i].person
        else:
            excellent_students = ' ' + students[i].person
    elif average[i] < 3:
        if len(bad_students) > 0:
            bad_students += ', ' + students[i].person
        else:
            bad_students = ' ' + students[i].person

students_statistics = []
for i in range(len(students)):
    student_info = {
        'id': i+1,
        'fio': students[i].person,
        'timp': scores[i*len(subjects)].value,
        'eis': scores[i*len(subjects) + 1].value,
        'philosophy': scores[i*len(subjects)+2].value,
        'english': scores[i*len(subjects)+3].value,
        'sport': scores[i*len(subjects)+4].value,
        'average': average[i]
    }
    students_statistics.append(student_info)

student_info = {
    'id': '',
    'fio': 'Итоговый балл',
    'timp': sred_ar[0],
    'eis': sred_ar[1],
    'philosophy': sred_ar[2],
    'english': sred_ar[3],
    'sport': sred_ar[4],
    'average': ''
}
students_statistics.append(student_info)

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
