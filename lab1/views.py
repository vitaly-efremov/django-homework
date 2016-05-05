# -*- coding: utf-8 -*-
from django.views.generic.base import TemplateView
class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update(
            {
                'students_statistics': statistics,
                'excellent_students': excellent_students,
                'bad_students': bad_students
                
            },

            
        )
        return context



import random

class Student(object):
    def __init__(self, id, fio):
        self.id = id
        self.fio = fio

student1 = Student(1, 'Andreev')
student2 = Student(2, 'Sergeev')
student3 = Student(3, 'Petrov')
student4 = Student(4, 'Sidorov')
student5 = Student(5, 'Antonov')
       
students = [student1, student2, student3, student4, student5]



class Subject(object):
    def __init__(self, name):
        self.name = name

subject1 = Subject('timp')
subject2 = Subject('eis')
subject3 = Subject('philosophy')
subject4 = Subject('english')
subject5 = Subject('sport')

subjects = [subject1, subject2, subject3, subject4, subject5]


class Score(object):
    def __init__(self, subject, value):
        self.subject = subject
        self.value = value

        
class Statistic(object):
    def __init__(self, student, scores):
        self.id = student.id
        self.fio = student.fio
        total = 0 
        for s in scores:
            total += s.value
            setattr(self, s.subject.name, s.value)

        self.average = float(total) / len(scores)


statistics = []
for student in students:
    
    score1 = Score(subject1, random.randint(1, 5))
    score2 = Score(subject2, random.randint(1, 5))
    score3 = Score(subject3, random.randint(1, 5))
    score4 = Score(subject4, random.randint(1, 5))
    score5 = Score(subject5, random.randint(1, 5))

    scores = [score1, score2, score3, score4, score5]
    statistic = Statistic(student, scores)
    statistics.append(statistic)


excellent_students =  ', '.join([st.fio for st in statistics if st.average >= 4.0])
bad_students =  ', '.join([st.fio for st in statistics if st.average <= 3.0])










