# -*- coding: utf-8 -*-
from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):

        context = super(IndexView, self).get_context_data(**kwargs)
        bad_stud = ', '.join(student.get_name(i) for i in score.bad_student())
        excellent_stud = ', '.join(student.get_name(i) for i in score.excellent_student(5))
        context.update(
            {
                        'students_statistics': statis_stud,
                        'excellent_students': excellent_stud,
                        'bad_students': bad_stud

            }
        )
        return context


class Student:
    def __init__(self, studnumber, name):
        self.student = dict(zip(studnumber, name))

    def get_name(self, studnumber):
        return self.student.setdefault(studnumber)

class Statistics:
    def __init__(self, stat):
        self.stat = stat

    def _average_grade(self):
        return float(sum(self.stat))/len(self.stat)

    def formatter(self, studnumber, name, subject):
        file = {'num': studnumber, 'fio': name}
        timp = dict(zip(subject, self.stat))
        file.update(timp)
        file.update({'average':self._average_grade()})
        return file

class Subject:
    def __init__(self, subject):
        self.subject = subject

    def get_subject(self):
        return self.subject

class Score:
    def __init__(self, stat, studnumber):
        self.stud_mark = dict(zip(studnumber, stat))

    def get_stat(self, studnumber):
        return self.stud_mark.setdefault(studnumber)

    def bad_student(self):
        return [i[0] for i in self.stud_mark.items() if i[1].count(2) != 0]

    def excellent_student(self, num_subjects):
        return [i[0] for i in self.stud_mark.items() if i[1].count(5) == num_subjects]

statis_stud = []

student = Student([1, 2, 3, 4, 5], ['Nikita', 'Andrey', 'Vladimer', 'Max', 'Dmitriy'])
subject = Subject(['python', 'elektrotex', 'teorInf', 'terVer', 'bos'])
score = Score([[2, 4, 4, 5, 4], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [3, 4, 5, 4, 5], [3, 5, 3, 3, 5]],    [1, 2, 3, 4, 5])
for i in range(1,6):
    statis = Statistics(score.get_stat(i))
    statis_stud.append(statis.formatter(i, student.get_name(i), subject.get_subject()))