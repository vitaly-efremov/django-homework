#-*- coding: utf-8 -*-
from django.views.generic.base import TemplateView


class Student(object):
    def __init__(self, s_num, s_name):
        self.student = dict(zip(s_num, s_name))
    def get_s_name(self, s_num):
        return self.student.setdefault(s_num)

class Subject(object):
    def __init__(self, subject):
        self.subject = subject
    def get_subject(self):
        return self.subject
    
class Score(object):
    def __init__(self, rez, s_num):
        self.student_marks = dict(zip(s_num, rez))
    def get_rez(self, s_num):
        return self.student_marks.setdefault(s_num)
    def bad_student(self):
        return [i[0] for i in self.student_marks.items() if i[1].count(2) != 0]
    def excellent_student(self, number_of_subjects):
        return [i[0] for i in self.student_marks.items() if i[1].count(5) == number_of_subjects]  

class Statistics(object):
    def __init__(self, rez):
        self.rez = rez
    def _average_grade(self):
        return float(sum(self.rez))/len(self.rez)
    def formatter(self, s_num, s_name, subject):
        data = {'id':s_num, 'name':s_name}
        foo = dict(zip(subject, self.rez))
        data.update(foo)
        data.update({'average':self._average_grade()})
        return data
        
        
class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        statistict_stud = []
        students = Student([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], ['Jarle', 'Ikkeland', 'Kagerou', 'Zukin', 'Koumori', 'Henpuku', 'Noddie', 'Mottleweed', 'Iteza', 'Yatarou'])
        subject = Subject(['s1', 's2', 's3', 's4', 's5'])
        score = Score([[5, 4, 4, 5, 5], [2, 3, 4, 2, 4], [3, 3, 4, 3, 5], [3, 5, 5, 2, 5], [3, 5, 2, 4, 5],
                   [5, 5, 5, 4, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 3], [3, 5, 3, 3, 5], [3, 5, 4, 3, 5]],
                   [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        for i in range(1,11):
            statistics = Statistics(score.get_rez(i))
            statistict_stud.append(statistics.formatter(i, students.get_s_name(i), subject.get_subject()))
        bad_stud = ', '.join(students.get_s_name(i) for i in score.bad_student())
        excellent_stud = ', '.join(students.get_s_name(i) for i in score.excellent_student(5))
        
        context.update(
            {
                'students_statistics': statistict_stud,
                'excellent_students': excellent_stud,
                'bad_students': bad_stud
            }
        )
        return context
