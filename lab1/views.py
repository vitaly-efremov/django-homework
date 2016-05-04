# -*- coding: utf-8 -*-
from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        _all = []
        students = Student([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], ['Трушин Никита', 
                                                             'Якут', 
                                                             'Толмачев Владимир', 
                                                             'Култаев Павел', 
                                                             'Прокушев Павел', 
                                                             'Световец Дмитрий', 
                                                             'Ажель Никита', 
                                                             'Киселек', 
                                                             'Адрей Сергеевич', 
                                                             'Маняшка'])
        subject = Subject(['timp', 'eis', 'philosophy', 'english', 'sport'])
        score = Score([ [5, 5, 5, 5, 5], 
                        [2, 2, 2, 2, 2], 
                        [5, 5, 5, 5, 5], 
                        [4, 2, 5, 3, 5], 
                        [3, 5, 2, 4, 5],
                        [2, 5, 2, 2, 5], 
                        [3, 5, 4, 4, 5], 
                        [3, 5, 2, 2, 2], 
                        [5, 5, 5, 5, 5], 
                        [2, 2, 2, 2, 2]],
                   [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
                   
        for i in range(1,11):
            statistics = Statistics(score.getGrades(i))
            _all.append(statistics.FormatRecord(i, students.getID(i), subject.get()))
        _bad = ', '.join(students.getID(i) for i in score.BlackList())
        _good = ', '.join(students.getID(i) for i in score.WhiteList())
        
        context.update(
            {
                'students_statistics': _all,
                'excellent_students': _good,
                'bad_students': _bad
            })
        return context


class Student(object):
    def __init__(self, student_id, fio):
        self.student = dict(zip(student_id, fio))
        
    def getID(self, student_id):
        return self.student.setdefault(student_id)

class Statistics(object):
    def __init__(self, grades):
        self.grades = grades
        
    def AverageGrade(self):
        return float(sum(self.grades))/len(self.grades)
        
    def FormatRecord(self, student_id, fio, subgect):
        inform = {'id':student_id, 'fio':fio}
        tmp = dict(zip(subgect, self.grades))
        inform.update(tmp)
        inform.update({'average':self.AverageGrade()})
        return inform

class Subject(object):
    def __init__(self, subject):
        self.subject = subject
        
    def get(self):
        return self.subject


class Score(object):
    def __init__(self, grades, student_id):
        self.student_assessment = dict(zip(student_id, grades))
        
    def getGrades(self, student_id):
        return self.student_assessment.setdefault(student_id)
        
    def BlackList(self):
        tmp = self.student_assessment.items()
        return [i[0] for i in tmp if i[1].count(2) == len(i[1])]
        
    def WhiteList(self):
        tmp = self.student_assessment.items()
        return [i[0] for i in tmp if i[1].count(5) == len(i[1])]  
