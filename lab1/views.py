# -*- coding: utf-8 -*-
from django.views.generic.base import TemplateView
import random


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        Stats = []
        Sub = []
        Scr = []
        Avr = 0
        ex_studs = []
        bad_studs = []

        for i in range(0,9,1):
            Sub = Subject.subjects(self)
            Scr = Score.get_score(Sub)
            Avr = Statistics.aver(Scr)
            if Avr < 3 : bad_studs.append(Student.name(i))
            elif Avr > 4 : ex_studs.append(Student.name(i))
            Stats.append({'id':(i + 1), 'fio':Student.name(i), Sub[0]: Scr[0],
                                Sub[1]: Scr[1], Sub[2]: Scr[2], 
                                Sub[3]: Scr[3], Sub[4]: Scr[4],
                                'average': Avr})
        context.update(
            {
                'students_statistics': Stats,
                'excellent_students': ex_studs,
                'bad_students': bad_studs
            }
        )
        return context


class Student:
    def name(id):
        name = ['Боровков Сергей', 'Бусыгин Иван', 'Ворожцов Сергей', 'Герасимов Вячеслав','Ерохин Евгений', 'Иванов Александр', 'Косаченко Татьяна', 'Кравченко Александр','Кузнецова Мария', 'Лозинг Варвара']
        return name[id]


class Statistics:
    def aver(score):
        sum = 0
        n = 0
        b = 0
        for i in score:
            sum += i
            n += 1
        b = sum/n
        return b


class Subject:
    def subjects(self):
        sub = ['timp','eis','philosophy','english','sport']
        return sub


class Score:
	def get_score(subject):
		score = []
		for i in range(len(subject)):
			score.append(random.randint(2,5))
		return score