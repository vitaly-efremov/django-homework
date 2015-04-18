# -*- coding: utf-8 -*-
from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        studentList = StudentList()
        

        studentList.add(Student('Mukovkin Dmitry', 723, 19))
        studentList.add(Student('Ivan Gurakov', 723, 19))
        studentList.add(Student('Petya Petrov', 723, 24))
        
        subjectList = []

        subjectList.append(Subject('English'))
        subjectList.append(Subject('TiMP'))
        subjectList.append(Subject('Mathematic'))

        scoreList = ScoreList()

        scoreList.add(Score(studentList.list[0].ids, 1, 5))
        scoreList.add(Score(studentList.list[0].ids, 2, 5))
        scoreList.add(Score(studentList.list[0].ids, 3, 5))
        
        scoreList.add(Score(studentList.list[1].ids, 2, 5))
        scoreList.add(Score(studentList.list[1].ids, 1, 4))
        scoreList.add(Score(studentList.list[1].ids, 3, 5))

        scoreList.add(Score(studentList.list[2].ids, 2, 3))
        scoreList.add(Score(studentList.list[2].ids, 1, 3))
        scoreList.add(Score(studentList.list[2].ids, 3, 2))

        statistic = Statistics(studentList.all(), subjectList, scoreList.all())


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
    def __init__(self):
        self.list = []

    def add(self, student):
        self.list.append(student)
        
        return self.list

    def all(self):
        return self.list

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

class ScoreList(object):
    def __init__(self):
        self.list = []

    def add(self, score):
        self.list.append(score)
        
    def all(self):
        return self.list