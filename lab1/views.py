# -*- coding: utf-8 -*-
from django.views.generic.base import TemplateView
import random


class Person(object):
    def __init__(self, fio):
        self.fio = fio


class Student(Person):
    def __init__(self, id, group, age, fio):
       super(Student, self).__init__(fio)
       self.id = id
       self.group = group
       self.age = age


class Subject(object):
    def __init__(self, id, name):
        self.id = id
        self.name = name


class Score(object):
    def __init__(self, student_id, subject_id, value):
        self.student_id = student_id
        self.subject_id = subject_id
        self.value = value


St_1 = Student(1, 723, 19, 'Иванов Иван Иванович')
St_2 = Student(2, 723, 20, 'Иванов Иван Степанович')
St_3 = Student(3, 723, 19, 'Иванов Иван Ильич')
St_4 = Student(4, 723, 21, 'Иванов Иван Кузьмич')
St_5 = Student(5, 723, 19, 'Петров Василий Владимирович')
St_6 = Student(6, 723, 20, 'Сидоров Илья Алексеевич')
St_7 = Student(7, 723, 20, 'Петров Виталий Олегович')
St_8 = Student(8, 723, 21, 'Сидоров Евгений Михайлович')
St_9 = Student(9, 723, 19, 'Борисов Петр Игнатьевич')
St_10 = Student(10, 723, 20, 'Борисов Максим Степанович')


Sub_1 = Subject(1, 'timp')
Sub_2 = Subject(2, 'eis')
Sub_3 = Subject(3, 'philosophy')
Sub_4 = Subject(4, 'english')
Sub_5 = Subject(5, 'sport')

list_students = [St_1, St_2, St_3, St_4, St_5, St_6, St_7, St_8, St_9, St_10]
list_subjects = [Sub_1, Sub_2, Sub_3, Sub_4, Sub_5]


list_score = []
for i in range(len(list_students)):
    for j in range(len(list_subjects)):
        list_score.append(Score(i, j, random.randint(2, 5)))


info = []
good_students = ' '
bad_students = ' '
timp_avg = 0
eis_avg = 0
philosophy_avg = 0
english_avg = 0
sport_avg = 0


for i in range(len(list_students)):
    information = {
        'id': list_students[i].id,
        'fio': list_students[i].fio,
        'timp': list_score[i].value,
        'eis': list_score[i+1].value,
        'philosophy': list_score[i+2].value,
        'english': list_score[i+3].value,
        'sport': list_score[i+4].value,
        'average': (list_score[i].value + list_score[i+1].value + list_score[i+2].value +
                     list_score[i+3].value + list_score[i+4].value)/5.0
    }

    timp_avg += list_score[i].value
    eis_avg += list_score[i+1].value
    philosophy_avg += list_score[i+2].value
    english_avg += list_score[i+3].value
    sport_avg += list_score[i+4].value

    if information['average'] > 3.5:
        good_students += list_students[i].fio + ', '
    if information['average'] <= 3:
        bad_students += list_students[i].fio + ', '
    info.append(information)

timp_avg /= float(len(list_students))
eis_avg /= float(len(list_students))
philosophy_avg /= float(len(list_students))
english_avg /= float(len(list_students))
sport_avg /= float(len(list_students))

information = {
    'timp':timp_avg,
    'eis':eis_avg,
    'philosophy':philosophy_avg,
    'english':english_avg,
    'sport':sport_avg
}
info.append(information)


bad_students = bad_students[: len(bad_students)-2]
if bad_students != '':
    bad_students += '.'
good_students = good_students[: len(good_students)-2]
if good_students != '':
    good_students += '.'


class IndexView(TemplateView):
    template_name = "index.html"
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        context.update(
            {
                'students_statistics': info,
                'excellent_students': good_students,
                'bad_students': bad_students
            }
        )
        return context