# -*- coding: utf-8 -*-
from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update(
            {
                'students_statistics': statistics_data_list,
                'excellent_students': ', '.join(excellent_students),
                'bad_students':', '.join(bad_students)
            }
        )
        return context


class Student(object):
    def __init__(self,data):
        self.info = dict(zip(['id','last_name','first_name','middle_name'],data))
        self.info['full_name'] = self.info['last_name'] + ' ' + self.info['first_name'] + ' ' + self.info['middle_name']

    def get_first_name(self):
        return self.info.setdefault('first_name')

    def get_last_name(self):
        return self.info.setdefault('last_name')

    def get_middle_name(self):
        return self.info.setdefault('middle_name')

    def get_full_name(self):
        return self.info.setdefault('full_name')

class Statistics:
    def __init__(self):
        self.subject = Subject(['timp', 'eis', 'philosophy', 'english', 'sport'])

    def get_statistic(self,data):
        self.student = Student (data[0:4])
        self.score = Score(data[4])
        self.record = {}
        self.record['id'] = self.student.info['id']
        self.record['fio'] = self.student.get_full_name()
        self.record.update(dict(zip(self.subject.get_subject(), self.score.get_marks())))
        self.record['average'] = self.score.avg()
        return self.record

class Subject(object):
    def __init__(self, subject):
        self.subject = subject

    def get_subject(self):
        return self.subject

class Score(object):
    def __init__(self,value):
        self.marks = value

    def get_marks(self):
        return self.marks

    def avg(self):
        self.average_score = sum(self.marks)/len(self.marks)
        return self.average_score


students_data_list = [[1, 'Щедрин', 'Станислав', 'Павлович', [5, 5, 5, 5, 5]],
                      [2, 'Ковальчук', 'Анастасия', 'Олеговна', [3, 5, 5, 4, 2]],
                      [3, 'Скориков', 'Иван', 'Юрьевич', [2, 2, 2, 2, 2]],
                      [4, 'Чакелев', 'Данила', 'Александрович', [4, 5, 5, 5, 3]],
                      [5, 'Пономарева', 'Анна', 'Алексеевна', [5, 5, 5, 5, 5]],
                      [6, 'Филимоненко', 'Игорь', 'Витальевич', [4, 4, 5, 5, 5]],
                      [7, 'Власенко', 'Никита', 'Андреевич', [2, 2, 2, 2, 2]]
                      ]
statistics_data_list = []
group_724 = Statistics()

for data in students_data_list:
    group_724.get_statistic(data)
    statistics_data_list.append(group_724.record)

excellent_students = [student['fio'] for student in statistics_data_list if student['average'] == 5]
bad_students = [student['fio'] for student in statistics_data_list if student['average'] == 2]
