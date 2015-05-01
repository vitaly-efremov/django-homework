# -*- coding: utf-8 -*-
from django.views.generic.base import TemplateView
from operator import itemgetter


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 8e136f9494b658c4f2a16185cce99bc3671aaaa0
        e = DataSet()
        context.update(
            {
                'students_statistics': e.context_create(),
                'excellent_students': e.best_students(),
<<<<<<< HEAD
=======
=======
        e = Data()
        context.update(
            {
                'students_statistics': e.get_statistics(),
                'excellent_students': e.excellent_students(),
>>>>>>> 1843df9f0be953cb07189206da1b00ab6c234094
>>>>>>> 8e136f9494b658c4f2a16185cce99bc3671aaaa0
                'bad_students': e.worst_students()
            }
        )
        return context


<<<<<<< HEAD
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
=======
<<<<<<< HEAD
class Person():
    def __init__(self, fio):
        self.fio = fio
=======
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
>>>>>>> 1843df9f0be953cb07189206da1b00ab6c234094

    def get_name(self):
        return self.fio

<<<<<<< HEAD

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
=======
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
>>>>>>> 1843df9f0be953cb07189206da1b00ab6c234094
>>>>>>> 8e136f9494b658c4f2a16185cce99bc3671aaaa0
