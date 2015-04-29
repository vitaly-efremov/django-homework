# -*- coding: utf-8 -*-
from django.views.generic.base import TemplateView
from operator import itemgetter


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        e = Data()
        context.update(
            {
                'students_statistics': e.get_statistics(),
                'excellent_students': e.excellent_students(),
                'bad_students': e.worst_students()
            }
        )
        return context


class Data ():
    def __init__(self):
        self.students = {}
        self.subjects = {}
        self.tables = (None, None)
        self.data_set_create(self.raw_data_get())

    def raw_data_get(self):
        table_0 = {
            'id_0': (u"Светлаков Михаил Олегович", 743, 18),
            'id_1': (u'Рандомов Первый Рандомович', 743, 18),
            'id_2': (u'Рандомов Второй Рандомович', 743, 18),
            'id_3': (u'Рандомов Третий Рандомович', 743, 18),
            'id_4': (u'Рандомов Четвертый Рандомович', 743, 18),
            'id_5': (u'Рандомов Пятый Рандомович', 743, 18),
            'id_6': (u'Рандомов Шестой Рандомович', 743, 18),
            'id_7': (u'Рандомов Седьмой Рандомович', 743, 18),
            'id_8': (u'Рандомов Восьмой Рандомович', 743, 18),
            'id_9': (u'Рандомов Девятый Рандомович', 743, 18)
        }
        table_1 = {
            'id_0': ['Philosophy', ('id_0', 5), ('id_1', 4), ('id_2', 3), ('id_3', 3), ('id_4', 2), ('id_5', 5),
                     ('id_6', 4), ('id_7', 3), ('id_8', 5), ('id_9', 4)],
            'id_1': ['TIMP', ('id_0', 5), ('id_1', 4), ('id_2', 3), ('id_3', 3), ('id_4', 2), ('id_5', 5),
                     ('id_6', 4), ('id_7', 3), ('id_8', 5), ('id_9', 4)],
            'id_2': ['Sport', ('id_0', 5), ('id_1', 4), ('id_2', 3), ('id_3', 3), ('id_4', 2), ('id_5', 5),
                     ('id_6', 4), ('id_7', 3), ('id_8', 5), ('id_9', 4)],
            'id_3': ['Inostranny yazik', ('id_0', 5), ('id_1', 4), ('id_2', 3), ('id_3', 3), ('id_4', 2),
                     ('id_5', 5), ('id_6', 4), ('id_7', 3), ('id_8', 5), ('id_9', 4)],
            'id_4': ['EIS', ('id_0', 5), ('id_1', 4), ('id_2', 3), ('id_3', 3), ('id_4', 5), ('id_5', 5),
                     ('id_6', 4), ('id_7', 3), ('id_8', 5), ('id_9', 4)],
        }
        self.subjects = [Subject(key, table_1[key][0]) for key in table_1.keys()]
        return table_0, table_1

    def value_get(self, values_list, student_id):
        temp = None
        for x in values_list:
            if x[0] == student_id:
                temp = x
                break
        return temp[1]

    def data_set_create(self, tables):
        if tables[0] is not None and tables[1] is not None:
            self.students = {Student('id_'+str(x), Person(tables[0]['id_'+str(x)][0]), tables[0]['id_'+str(x)][1], tables[0]['id_'+str(x)][2]): [[subject_id, self.value_get(tables[1][subject_id], 'id_'+str(x))] for subject_id in tables[1].keys()] for x in range(len(tables[0].keys())-1)}
        else:
            print "Data error"

    def average_grade(self, student_id, subject_id='all'):
        grades = []
        if subject_id != 'all':
            for value in self.students.values():
                if value[0] == subject_id:
                    grades.append(value[1])
        else:
            for student in self.students.keys():
                if student.id == student_id:
                    grades = [values[1] for values in self.students[student]]
                    break
            if len(grades) == 0:
                print "Error"
            else:
                return float(sum(grades))/len(grades)

    def excellent_students(self, criteria=4.5):
        ex_list = ''
        for student in self.students.keys():
            if self.average_grade(student.id) > criteria:
                if ex_list != '':
                    ex_list += ', '
                ex_list += student.person.fio
        if ex_list == '':
            return u'Нет хороших студентов :('
        else:
            return ex_list

    def worst_students(self, criteria=3):
        ex_list = ''
        for student in self.students.keys():
            if self.average_grade(student.id) < criteria:
                if ex_list != '':
                    ex_list += ', '
                ex_list += student.person.fio
        if ex_list == '':
            return u'Нет плохих студентов :)'
        else:
            return ex_list

    def stats_create(self, student_id):
        g = None

        for student in self.students.keys():
            if student.id == student_id:
                g = student
        return {
            'id': str(int(student_id[3])+1),
            'fio': g.person.fio,
            'timp': str([grade[1] for grade in self.students[g] if grade[0] == 'id_1'][0]),
            'eis': str([grade[1] for grade in self.students[g] if grade[0] == 'id_4'][0]),
            'philosophy': str([grade[1] for grade in self.students[g] if grade[0] == 'id_0'][0]),
            'english': str([grade[1] for grade in self.students[g] if grade[0] == 'id_3'][0]),
            'sport': str([grade[1] for grade in self.students[g] if grade[0] == 'id_2'][0]),
            'average': self.average_grade(student_id),
        }

    def get_statistics(self):
        sorted_id = [(key, key.id) for key in self.students.keys()]
        sorted_id.sort(key=lambda student: student[1][3])
        return [self.stats_create(student[1]) for student in sorted_id]


class Student:
    def __init__(self, id, person, group, age):
        self.id = id
        self.person = person
        self.group = group
        self.age = age


class Statistics:
    def __init__(self, student_id, subjects):
        self.student_id = student_id
        self.Subjects = subjects


class Subject:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class Score:
    def __init__(self, student_id, subject_id):
        self.student_id = student_id
        self.subject_id = subject_id


class Person:
    def __init__(self, fio):
        self.fio = fio