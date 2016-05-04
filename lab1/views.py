# -*- coding: utf-8 -*-
from django.views.generic.base import TemplateView

class Person:
    def __init__(self, fio):
        self.fio = fio


class Student(Person):
    def __init__(self, id, group):
        self.id = id
        self.group = group


class Subject:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class Score:
    def __init__(self, student, subject, value):
        self.student = student
        self.subject = subject
        self.value = value


class Statistics:
    def __init__(self):
        self.stat = ()

    def student(self, id, group):
        self.student = Student(id, group)

    def score(self, timp, eis, fil, inz, fiz, ti, twims, BDiES, BOS):
        self.timp = Score(self.student, sub1, timp)                 
        self.eis = Score(self.student, sub2, eis)
        self.fil = Score(self.student, sub3, fil)
        self.inz = Score(self.student, sub4, inz)
        self.fiz = Score(self.student, sub5, fiz)
        self.ti = Score(self.student, sub6, ti)
        self.twims = Score(self.student, sub7, twims)
        self.BDiES = Score(self.student, sub8, BDiES)
        self.BOS = Score(self.student, sub9, BOS)

    def average(self):
        self.average = float(self.fiz.value + self.eis.value + self.fil.value + self.inz.value + self.ti.value + self.twims.value
                             + self.BDiES.value + self.BOS.value)/8


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update(
            {
                'students_statistics': [
                    {
                        'id': s.student.id,
                        'fio': s.student.fio,
                        'timp': s.timp.value,
                        'eis': s.eis.value,
                        'ti':s.ti.value,
                        'twims':s.twims.value,
                        'BDiES':s.BDiES.value,
                        'BOS':s.BOS.value,
                        'philosophy': s.fil.value,
                        'english': s.eis.value,
                        'sport': s.fiz.value,
                        'average': s.average,
                    }
                    for s in main
                ],
                'excellent_students': excellent_students,
                'bad_students': bad_students

            }
        )
        return context
sub1 = Subject(1, 'timp')
sub2 = Subject(2, 'eis')
sub3 = Subject(3, 'fil')
sub4 = Subject(4, 'inz')
sub5 = Subject(5, 'fiz')
sub6 = Subject(6, 'ti')
sub7 = Subject(7, 'twims')
sub8 = Subject(8, 'BDiES')
sub9 = Subject(9, 'BOS')
    


stud1 = Statistics()
stud1.student = Student(1, 744)
stud1.student.fio = 'Пекарских Светлана'
stud1.score(5, 5, 5, 5, 5, 5,5,5,5)

stud2 = Statistics()
stud2.student = Student(2, 744)
stud2.student.fio = 'Андреева Юлия'
stud2.score(5, 4, 2, 3, 5, 4,5,4,5)

stud3 = Statistics()
stud3.student = Student(3, 744)
stud3.student.fio = 'Власенко Анастасия'
stud3.score(4, 4, 2, 5, 4, 2,5,5,4)

stud4 = Statistics()
stud4.student = Student(4, 744)
stud4.student.fio = 'Култаев Павел'
stud4.score(4, 4, 2, 5, 5, 5,5,5,5)

stud5 = Statistics()
stud5.student = Student(5, 744)
stud5.student.fio = 'Пятков Александр'
stud5.score(3, 2, 2, 2, 3, 3,2,3,2)

stud6 = Statistics()
stud6.student = Student(6, 744)
stud6.student.fio = 'Облаков Дмитрий'
stud6.score(4, 4, 2, 5, 5, 4,5,3,5)

stud7 = Statistics()
stud7.student = Student(7, 744)
stud7.student.fio = 'Филимоненко Игорь'
stud7.score(5, 5, 5, 5, 5, 5,5,5,5)

stud8 = Statistics()
stud8.student = Student(8, 744)
stud8.student.fio = 'Газизов Рустам'
stud8.score(4, 4, 2, 5, 5, 5,5,5,5)

stud9 = Statistics()
stud9.student = Student(9, 744)
stud9.student.fio = 'Селиванов Владимир'
stud9.score(4, 4, 2, 5, 5, 3,2,5,3)

stud10 = Statistics()
stud10.student = Student(10, 744)
stud10.student.fio = 'Кузнецова Анна'
stud10.score(4, 4, 2, 5, 5,3 ,5,5,3)

stud11 = Statistics()
stud11.student = Student(11, 744)
stud11.student.fio = 'Трушин Никита'
stud11.score(4, 4, 2, 5, 5, 3,5,4,5)

main = [stud1, stud2, stud3, stud4, stud5, stud6, stud7, stud8, stud9, stud10, stud11]
for s in main:
    s.average()
excellent = [s.student.fio for s in main if s.average == 5]
bad = [s.student.fio for s in main if s.average <= 2.5]
excellent_students = ', '.join(excellent)
bad_students = ', '.join(bad)
