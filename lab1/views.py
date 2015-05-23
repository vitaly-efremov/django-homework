# -*- coding: utf-8 -*-
from django.views.generic.base import TemplateView


class Person(object):
    def __init__(self, fio):
        self.fio = fio

    def get_fio(self):
        return str(self.fio)


class Student(Person):
    def __init__(self, id, fio, group, age):
        super(Student, self).__init__(fio)
        self.id = id
        self.group = group
        self.age = age

    def get_id(self):
        return int(id)


class Subject(object):
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return str(self.name)


class Score(object):
    def __init__(self, student_id, value):
        self.student_id = student_id
        self.value = value

    def get_m(self, q):
        return (self.value[q])

    def get_arith(self):
        return float(self.value[0] +
                     self.value[1] +
                     self.value[2] +
                     self.value[3] +
                     self.value[4]) / 5


students = []
students.append(Student(0, 'Алексин Павел Сергеевич', '743', 20))
students.append(Student(1, 'Вершинин Артем Сергеевич', '743', 20))
students.append(Student(2, 'Зарипов Данил Вадимович', '743', 19))
students.append(Student(3, 'Звягинцев Евгений Андреевич', '743', 19))
students.append(Student(4, 'Кайзер Екатерина Александровна', '743', 20))
students.append(Student(5, 'Ковалев Вечяслав Юрьевич', '743', 20))
students.append(Student(6, 'Шишкарев Демьян Григорьевич', '743', 20))


subjects = []
subjects.append(Subject('БДЭС'))
subjects.append(Subject('БОС'))
subjects.append(Subject('ДМ'))
subjects.append(Subject('ИЯ'))
subjects.append(Subject('ТВиМС'))


marks = []
marks.append(Score(0, [4, 5, 5, 3, 4]))
marks.append(Score(1, [4, 5, 5, 2, 3]))
marks.append(Score(2, [4, 4, 5, 3, 4]))
marks.append(Score(3, [4, 5, 5, 4, 5]))
marks.append(Score(4, [4, 5, 5, 5, 5]))
marks.append(Score(5, [4, 5, 5, 3, 3]))
marks.append(Score(6, [3, 3, 2, 3, 2]))


mark0 = []
mark1 = []
mark2 = []
mark3 = []
mark4 = []
fio = []
average = []
bad_gays = []
good_gays = []
for i in range(0, 7):
    mark0.append(marks[i].get_m(0))
    mark1.append(marks[i].get_m(1))
    mark2.append(marks[i].get_m(2))
    mark3.append(marks[i].get_m(3))
    mark4.append(marks[i].get_m(4))
    fio.append(students[i].get_fio())
    average.append(marks[i].get_arith())
    if (average[i] > 4.5):
        good_gays.append(students[i].get_fio())
    if (average[i] < 3):
        bad_gays.append(students[i].get_fio())


av_m0 = round((float(mark0[0]) + float(mark0[1]) + float(mark0[2]) + float(mark0[3]) +
         float(mark0[4]) + float(mark0[5]) + float(mark0[6]))/7,2)
av_m1 = round((float(mark1[0]) + float(mark1[1]) + float(mark1[2]) + float(mark1[3]) +
         float(mark1[4]) + float(mark1[5]) + float(mark1[6]))/7,2)
av_m2 = round((float(mark2[0]) + float(mark2[1]) + float(mark2[2]) + float(mark2[3]) +
         float(mark2[4]) + float(mark2[5]) + float(mark2[6]))/7,2)
av_m3 = round((float(mark3[0]) + float(mark3[1]) + float(mark3[2]) + float(mark3[3]) +
         float(mark3[4]) + float(mark3[5]) + float(mark3[6]))/7,2)
av_m4 = round((float(mark4[0]) + float(mark4[1]) + float(mark4[2]) + float(mark4[3]) +
         float(mark4[4]) + float(mark4[5]) + float(mark4[6]))/7,2)
av_m = (av_m0 + av_m1 + av_m2 + av_m3 + av_m4)/5


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update(
            {
                'students_statistics': [
                    {
                        'id': 1,
                        'fio': fio[0],
                        'bdes': mark0[0],
                        'bos': mark1[0],
                        'dm': mark2[0],
                        'english': mark3[0],
                        'tvims': mark4[0],
                        'average': average[0],
                    },
                    {
                        'id': 2,
                        'fio': fio[1],
                        'bdes': mark0[1],
                        'bos': mark1[1],
                        'dm': mark2[1],
                        'english': mark3[1],
                        'tvims': mark4[1],
                        'average': average[1],
                    },
                    {
                        'id': 3,
                        'fio': fio[2],
                        'bdes': mark0[2],
                        'bos': mark1[2],
                        'dm': mark2[2],
                        'english': mark3[2],
                        'tvims': mark4[2],
                        'average': average[2],
                    },
                    {
                        'id': 4,
                        'fio': fio[3],
                        'bdes': mark0[3],
                        'bos': mark1[3],
                        'dm': mark2[3],
                        'english': mark3[3],
                        'tvims': mark4[3],
                        'average': average[3],
                    },
                    {
                        'id': 5,
                        'fio': fio[4],
                        'bdes': mark0[4],
                        'bos': mark1[4],
                        'dm': mark2[4],
                        'english': mark3[4],
                        'tvims': mark4[4],
                        'average': average[4],
                    },
                    {
                        'id': 6,
                        'fio': fio[5],
                        'bdes': mark0[5],
                        'bos': mark1[5],
                        'dm': mark2[5],
                        'english': mark3[5],
                        'tvims': mark4[5],
                        'average': average[5],
                    },
                    {
                        'id': 7,
                        'fio': fio[6],
                        'bdes': mark0[6],
                        'bos': mark1[6],
                        'dm': mark2[6],
                        'english': mark3[6],
                        'tvims': mark4[6],
                        'average': average[6],
                    },
                    {
                        'fio': 'Ср. знач.',
                        'bdes': av_m0,
                        'bos': av_m1,
                        'dm': av_m2,
                        'english': av_m3,
                        'tvims': av_m4,
                        'average': av_m,
                    },

                ],
                'excellent_students': ', '.join(good_gays),
                'bad_students': ', '.join(bad_gays),
            }
        )
        return context
