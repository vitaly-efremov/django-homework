#-*- coding: utf-8 -*-
from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        statistict_stud = []
        students = Student{1:'Аримпилов', 2:'Борисов', 3:'Селиванова', 4:'Демченко', 5:'Иванов', 6:'Фёдоров', 7:'Хорошев', 8:'Кельский'}
        subject = Subject(['s1', 's2', 's3', 's4', 's5'])
        score = Score([[3,4,5,4,5], [5,4,5,4,3], [5,5,5,4,4], [4,4,3,4,5], [2,3,4,4,4],
                   [4,4,3,5,5], [5,5,5,5,5], [5, 5, 5, 5, 5]],
                   [1, 2, 3, 4, 5, 6, 7, 8])
        for i in range(1,9):
            statistics = Statistics(score.get_rez(i))
            statistict_stud.append(statistics.formatter(i, students.get_fio(i), subject.get_subject()))
        bad_stud = ', '.join(students.get_fio(i) for i in score.bad_student())
        excellent_stud = ', '.join(students.get_fio(i) for i in score.excellent_student(5))
        
        context.update(
            {
                'students_statistics': statistict_stud,
                'excellent_students': excellent_stud,
                'bad_students': bad_stud
            }
        )
        return context


class Student(object):
    def __init__(self, id, fio):
        self.student = dict(zip(id, fio))
    def get_fio(self, id):
        return self.student.setdefault(id)

class Subject(object):
    def __init__(self, subject):
        self.subject = subject
    def get_subject(self):
        return self.subject
    
class Score(object):
    def __init__(self, rez, id):
        self.student_marks = dict(zip(id, rez))
    def get_rez(self, id):
        return self.student_marks.setdefault(id)
    def bad_student(self):
        return [i[0] for i in self.student_marks.items() if i[1].count(2) != 0]
    def excellent_student(self, number_of_subjects):
        return [i[0] for i in self.student_marks.items() if i[1].count(5) == number_of_subjects]  

class Statistics(object):
    def __init__(self, rez):
        self.rez = rez
    def _average_grade(self):
        return float(sum(self.rez))/len(self.rez)
    def formatter(self, id, fio, subject):
        data = {'id':id, 'fio':fio}
        foo = dict(zip(subject, self.rez))
        data.update(foo)
        data.update({'average':self._average_grade()})
        return data

  
