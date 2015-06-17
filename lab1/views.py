# -*- coding: utf-8 -*-
from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update(
            {
                'students_statistics': stat1.generate_dict_list(),
                'excellent_students': ', '.join(stat1.good()),
                'bad_students': ', '.join(stat1.bad()),
                'average_subj': [stat1.avr_sub(x) for x in stat1.all_subj_id()]
            }
        )
        return context

class Person(object):
    def __init__(self, fio, age):
        self.fio = fio
        self.age = age

class Student(Person):
    def __init__(self, id, group, age, fio):
        super(Student, self).__init__(fio, age)
        self.id = id
        self.group = group

class Statistics(object):
    def __init__(self, scores):
        self.scores = scores

    # средний балл студента
    def avr(self, stud):
        l = [s.value for s in self.scores if s.student == stud]
        return sum(l) / float(len(l))

    # средний балл предмета
    def avr_sub(self, subj):
        l = [s.value for s in self.scores if s.subject_id == subj]
        return sum(l) / float(len(l))

    # множество всех id предметов
    def all_subj_id(self):
        return {z.subject_id for z in self.scores}


    # множество всех студентов
    def all_stud(self):
        return {z.student for z in self.scores}

    # похвалить студентов
    def good(self):
        return [s.fio for s in self.all_stud() if self.avr(s) >= 4.5]

    # отчислить студентов
    def bad(self):
        return [s.fio for s in self.all_stud() if self.avr(s) < 3]

    # вывести
    def generate_dict_list(self):
        lst = [
            {
                'fio': x.fio,
                'marks': [s.value for s in self.scores if s.student == x],
                'average': round(self.avr(x), 2)
            }
            for x in self.all_stud()
        ]
        return lst

class Subject(object):
    def __init__(self, subject_id, name):
        self.subject_id = subject_id
        self.name = name

class Score(object):
    def __init__(self, student, subject_id, value):
        self.value = value
        self.student = student
        self.subject_id = subject_id
sub1=Subject(1, 'математика')
sub2=Subject(2, 'физика')
sub3=Subject(3, 'геометрия')
sub4=Subject(4, 'музыка')

a1=Student(1, 723, 20, 'Бикмухаметов Алексей Юрьевич')
a2=Student(2, 723, 19, 'Гураков Иван Ахмедович')
a3=Student(3, 723, 21, 'Бровкин Никита Ахмедович')
a4=Student(4, 723, 20, 'Сагалакова Илона Аделаидовна')
a5=Student(5, 723, 23, 'Ондар Регина Аделаидовна')
a6=Student(6, 723, 20, 'Сноу Джон Бастардович')
a7=Student(7, 723, 20, 'Ли Святослав Вячеславович')
a8=Student(8, 723, 19, 'Цой Виктор')
a9=Student(9, 723, 20, 'Они убили Джона')
a10=Student(10, 723, 20, 'Муковкин Дмитрий Ахмедович')

sc1=Score(a1, 1, 5)
sc2=Score(a1, 2, 5)
sc3=Score(a1, 3, 5)
sc4=Score(a1, 4, 5)
sc5=Score(a2, 1, 3)
sc6=Score(a2, 2, 4)
sc7=Score(a2, 3, 2)
sc8=Score(a2, 4, 2)
sc9=Score(a3, 1, 5)
sc10=Score(a3, 2, 3)
sc11=Score(a3, 3, 2)
sc12=Score(a3, 4, 4)
sc13=Score(a4, 1, 3)
sc14=Score(a4, 2, 2)
sc15=Score(a4, 3, 4)
sc16=Score(a4, 4, 3)
sc17=Score(a5, 1, 2)
sc18=Score(a5, 2, 5)
sc19=Score(a5, 3, 3)
sc20=Score(a5, 4, 2)
sc21=Score(a6, 1, 5)
sc22=Score(a6, 2, 5)
sc23=Score(a6, 3, 5)
sc24=Score(a6, 4, 5)
sc25=Score(a7, 1, 3)
sc26=Score(a7, 2, 2)
sc27=Score(a7, 3, 4)
sc28=Score(a7, 4, 4)
sc29=Score(a8, 1, 4)
sc30=Score(a8, 2, 4)
sc31=Score(a8, 3, 2)
sc32=Score(a8, 4, 5)
sc33=Score(a9, 1, 5)
sc34=Score(a9, 2, 3)
sc35=Score(a9, 3, 5)
sc36=Score(a9, 4, 2)
sc37=Score(a10, 1, 5)
sc38=Score(a10, 2, 4)
sc39=Score(a10, 3, 4)
sc40=Score(a10, 4, 5)

stat1=Statistics([sc1, sc2, sc3, sc4, sc5, sc6, sc7, sc8, sc9, sc10, sc11, sc12, sc13, sc14, sc15, sc16, sc17, sc18,
sc19, sc20, sc21, sc22, sc23, sc24, sc25, sc26, sc27, sc28, sc29, sc30, sc31, sc32, sc33, sc34, sc35, sc36, sc37, sc38,
sc39, sc40])


