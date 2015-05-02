# -*- coding: utf-8 -*-
from django.views.generic.base import TemplateView

class Statistics:
    def __init__(self, student_list, subject_list, score_list):
        self.st_list = student_list
        self.su_list = subject_list
        self.sc_list = score_list

    def listStudent(self):
        for e in self.st_list:
            e.subjects = self.subjectGetByStudent(e.ids)
            e.avg = 1.0* self.getAverage(e.subjects) / len(e.subjects)

        return self.st_list

    def subjectGetByStudent(self, student):
        return sorted(filter(lambda e: (e.student == student), self.sc_list), key = lambda score: score.subject)

    def getAverage(self, subjects):
        return sum(map(lambda x: x.score, subjects))
    
    def listSubject(self):
        return self.su_list

    def getExcellentStudent(self):
        return filter(lambda e: (1.0* self.getAverage(self.subjectGetByStudent(e.ids)) / len(e.subjects)) > 4.5, self.st_list)

    def getBadStudent(self):
        return filter(lambda e: (1.0 * self.getAverage(self.subjectGetByStudent(e.ids)) / len(e.subjects)) < 3.0, self.st_list)

    def getResultSummary(self):
        print map(lambda e: (1.0 * e._id) , self.su_list)
        return map(lambda e: (1.0 * sum(self.getBySubject(e._id)) / len(self.getBySubject(e._id))) , self.su_list)

    def getBySubject(self, _id):
        return map(lambda x: x.score, filter(lambda e: (e.subject == _id), self.sc_list))

class Person:
    pass

class Student(Person):
    inc = 1

    def __init__(self, person, group, age):
        self.ids = Student.inc
        self.fio = person
        self.group  = group
        self.age = age
        self.subjects = []

        Student.inc += 1

class StudentList:
    pass

# class Statistics:
#     def 
    # student_id, [Subjects]
    # pass

class Subject:
    inc = 1

    def __init__(self, name):
        self._id = Subject.inc
        self.name = name

        Subject.inc += 1

class Score(object):
    inc = 1
    def __init__(self, student, subject, score):
        self._id = Score.inc

        self.student = student
        self.subject = subject
        self.score = score
        
        Score.inc += 1

student_list = []
        

student_list.append(Student('Mukovkin Dmitry', 723, 19))
student_list.append(Student('Ivan Gurakov', 723, 19))
student_list.append(Student('Petya Petrov', 723, 24))

subject_list = []

subject_list.append(Subject('English'))
subject_list.append(Subject('TiMP'))
subject_list.append(Subject('Mathematic'))

score_list = []

score_list.append(Score(student_list[0].ids, 1, 5))
score_list.append(Score(student_list[0].ids, 2, 5))
score_list.append(Score(student_list[0].ids, 3, 5))

score_list.append(Score(student_list[1].ids, 2, 5))
score_list.append(Score(student_list[1].ids, 1, 4))
score_list.append(Score(student_list[1].ids, 3, 5))
    
score_list.append(Score(student_list[2].ids, 2, 3))
score_list.append(Score(student_list[2].ids, 1, 3))
score_list.append(Score(student_list[2].ids, 3, 2))

statistic = Statistics(student_list, subject_list, score_list)


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        

        context = super(IndexView, self).get_context_data(**kwargs)
        context.update(
            {
                'students_statistics': statistic.listStudent(),
                'list_subject': statistic.listSubject(),
                'excellent_students': statistic.getExcellentStudent(),
                'bad_students': statistic.getBadStudent(),
                'summarySubject': statistic.getResultSummary()
            }
        )
        return context
