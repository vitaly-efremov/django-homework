# -*- coding: utf-8 -*-
from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        e = DataSet()
        context.update(
            {
                'students_statistics': e.context_create(),
                'excellent_students': e.best_students(),
                'bad_students': e.worst_students()
            }
        )
        return context


class Person():
    def __init__(self, fio):
        self.fio = fio

    def get_name(self):
        return self.fio


class Score():
    def __init__(self, grades):
        self.grades = [grade for grade in grades if len(grade) == 2]

    def get_grade(self, student_id):
        grade = -1
        for value in self.grades:
            if value[0] == student_id:
                grade = value[1]
                break
        if grade == -1:
            print 'Data Error'
            return 0
        else:
            return grade

    def average_grade(self, student_id='default', subjects='default'):
        if student_id == 'default':
            return float(sum([grade[1] for grade in self.grades]))/len(self.grades)
        else:
            if subjects != 'default':
                summary = 0
                for subject in subjects.values():
                    for value in subject.get_grades():
                        if value[0] == student_id:
                            summary += value[1]
                            break
                return float(summary)/len(subjects.keys())
            else:
                print 'Data Error'
                return 0


class Subject(Score):
    def __init__(self, name, grades):
        Score.__init__(self, grades=grades)
        self.name = name

    def get_name(self):
        return self.name

    def get_grades(self):
        return self.grades


class Student(Person, Score):
    def __init__(self, fio, age, group):
        Person.__init__(self, fio=fio)
        self.age = age
        self.group = group


class DataSet ():
    def __init__(self):
        self.tables = {
            'students': {},
            'subjects': {}}

    def raw_data_get(self):
        table_0 = [
            ('id_0', u'Светлаков Михаил Олегович', 743, 18),
            ('id_1', u'Рандомов Первый Рандомович', 743, 18),
            ('id_2', u'Рандомов Второй Рандомович', 743, 18),
            ('id_3', u'Рандомов Третий Рандомович', 743, 18),
            ('id_4', u'Рандомов Четвертый Рандомович', 743, 18),
            ('id_5', u'Рандомов Пятый Рандомович', 743, 18),
            ('id_6', u'Рандомов Шестой Рандомович', 743, 18),
            ('id_7', u'Рандомов Седьмой Рандомович', 743, 18),
            ('id_8', u'Рандомов Восьмой Рандомович', 743, 18),
            ('id_9', u'Рандомов Девятый Рандомович', 743, 18)
        ]
        table_1 = [
            ('id_0', 'philosophy', ('id_0', 5), ('id_1', 4), ('id_2', 3), ('id_3', 3), ('id_4', 2), ('id_5', 5),
                ('id_6', 4), ('id_7', 3), ('id_8', 5), ('id_9', 4)),
            ('id_1', 'timp', ('id_0', 5), ('id_1', 4), ('id_2', 3), ('id_3', 3), ('id_4', 2), ('id_5', 5),
                ('id_6', 4), ('id_7', 3), ('id_8', 5), ('id_9', 4)),
            ('id_2', 'sport', ('id_0', 5), ('id_1', 4), ('id_2', 3), ('id_3', 3), ('id_4', 2), ('id_5', 5),
                ('id_6', 4), ('id_7', 3), ('id_8', 5), ('id_9', 4)),
            ('id_3', 'english', ('id_0', 5), ('id_1', 4), ('id_2', 3), ('id_3', 3), ('id_4', 2),
                ('id_5', 5), ('id_6', 4), ('id_7', 3), ('id_8', 5), ('id_9', 4)),
            ('id_4', 'eis', ('id_0', 5), ('id_1', 4), ('id_2', 5), ('id_3', 3), ('id_4', 5), ('id_5', 5),
                ('id_6', 4), ('id_7', 3), ('id_8', 5), ('id_9', 4)),
            ]
        self.tables['students'] = {student[0]: Student(fio=student[1], group=student[2], age=student[3])
                                   for student in table_0}
        self.tables['subjects'] = {subject[0]: Subject(name=subject[1],
                                   grades=[value for value in subject if len(value) == 2])
                                   for subject in table_1}

    def subject_get_id(self, subject_name):
        id_n = ''
        for subject_id in self.tables['subjects'].keys():
            if self.tables['subjects'][subject_id].get_name() == subject_name:
                id_n = subject_id
                break
        if id_n == '':
            print 'Data Error'
        return id_n

    def worst_students(self, criteria=3):
        str = ' '
        list = [self.tables['students'][student_id].get_name() for student_id in self.tables['students']
                if self.tables['students'][student_id].average_grade(student_id, self.tables['subjects']) < criteria]
        for name in list:
            str += name+", "
        str = str[0:len(str)-2]
        if str == ' ':
            return u'Нет плохих студентов :)'
        else:
            return str

    def best_students(self, criteria=4.5):
        str = ' '
        list = [self.tables['students'][student_id].get_name() for student_id in self.tables['students']
                if self.tables['students'][student_id].average_grade(student_id, self.tables['subjects']) > criteria]
        for name in list:
            str += name+", "
        str = str[0:len(str)-2]
        if str == ' ':
            return u'Нет хороших студентов :('
        else:
            return str

    def context_create(self):
        self.raw_data_get()
        context = []
        sorted_id = self.tables['students'].keys()
        sorted_id.sort(key=lambda x: x[3])
        for student_id in sorted_id:
            context.append({
                'id': int(student_id[3]),
                'fio': self.tables['students'][student_id].get_name(),
                'timp': int(self.tables['subjects'][self.subject_get_id('timp')].get_grade(student_id)),
                'eis': int(self.tables['subjects'][self.subject_get_id('eis')].get_grade(student_id)),
                'philosophy': int(self.tables['subjects'][self.subject_get_id('philosophy')].get_grade(student_id)),
                'english': int(self.tables['subjects'][self.subject_get_id('english')].get_grade(student_id)),
                'sport': int(self.tables['subjects'][self.subject_get_id('sport')].get_grade(student_id)),
                'average': float(self.tables['students'][student_id].average_grade(student_id, self.tables['subjects']))
            })
        context.append({
            'id': '-',
            'fio': 'Средний балл по дисциплинам',
            'timp': float(self.tables['subjects'][self.subject_get_id('timp')].average_grade()),
            'eis': float(self.tables['subjects'][self.subject_get_id('eis')].average_grade()),
            'philosophy': float(self.tables['subjects'][self.subject_get_id('philosophy')].average_grade()),
            'english': float(self.tables['subjects'][self.subject_get_id('english')].average_grade()),
            'sport': float(self.tables['subjects'][self.subject_get_id('sport')].average_grade()),
            'average': ''
            })
        return context