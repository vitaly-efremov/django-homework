#-*- coding: utf-8 -*-
from django.views.generic.base import TemplateView


class Student(object):
    def __init__(self, s_num, s_name):
        self.s_num=s_num
        self.s_name=s_name

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

    def student(self, s_num, s_name):
        self.student = Student(s_num, s_name)

    def score(self, s1, s2, s3, s4, s5):
        self.s1 = Score(self.student, sub1, s1)                 
        self.s2 = Score(self.student, sub2, s2)
        self.s3 = Score(self.student, sub3, s3)
        self.s4 = Score(self.student, sub4, s4)
        self.s5 = Score(self.student, sub5, s5)

    def average(self):
        self.average = float(self.s1.value + self.s2.value + self.s3.value + self.s4.value + self.s5.value)/5
        
        
class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update(
            {
                'students_statistics': [
                    {
                        'id': s.student.s_num,
                        'name': s.student.s_name,
                        's1': s.s1.value,
                        's2': s.s2.value,
                        's3':s.s3.value,
                        's4':s.s4.value,
                        's5':s.s5.value,
                        'average': s.average,
                    }
                    for s in main
                ],
                'excellent_students': excellent_students,
                'bad_students': bad_students

            }
        )
        return context
sub1 = Subject(1, 's1')
sub2 = Subject(2, 's2')
sub3 = Subject(3, 's3')
sub4 = Subject(4, 's4')
sub5 = Subject(5, 's5')


main = [stud1, stud2, stud3, stud4, stud5, stud6, stud7, stud8, stud9, stud10, stud11]
for s in main:
    s.average()
excellent = [s.student.s_name for s in main if s.average == 5]
bad = [s.student.s_name for s in main if s.average <= 2.5]
excellent_students = ', '.join(excellent)
bad_students = ', '.join(bad)
