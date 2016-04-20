# -*- coding: utf-8 -*-
from django.views.generic.base import TemplateView
import random

class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        listOfStudents = ['Боровков Сергей', 'Бусыгин Иван', 'Ворожцов Сергей', 'Герасимов Вячеслав',
                          'Ерохин Евгений', 'Иванов Александр', 'Косаченко Татьяна', 'Кравченко Александр',
                          'Кузнецова Мария', 'Лозинг Варвара', 'Мартынов Роман', 'Машуков Никита',
                          'Мухин Алексей', 'Мякишева Эвелина', 'Пехова Анна', 'Сапунов Антон',
                          'Черемных Алексей', 'Шивцов Данил', 'Федурин Артем']
        listOfStats = []
        Statistics.ExcStudents = []
        Statistics.BadStudents = []
        for i in range(len(listOfStudents)):
            Student.id = i
            Student.name = listOfStudents[i]
            Score.timp = random.randint(2, 5)
            Score.eis = random.randint(2, 5)
            Score.eng = random.randint(2, 5)
            Score.phil = random.randint(2, 5)
            Score.sport = random.randint(2, 5)
            Score.average = (Score.timp + Score.eis + Score.eng + Score.phil + Score.sport) / 5
            if Score.average >= 4.5:
                Statistics.ExcStudents.append(listOfStudents[i])
            elif Score.average <= 2.5:
                Statistics.BadStudents.append(listOfStudents[i])
            listOfStats.append({'id': Student.id, 'fio': Student.name, 'timp': Score.timp,
                                'eis': Score.eis, 'philosophy': Score.phil, 'english': Score.eng,
                                'sport': Score.sport, 'average': Score.average})

        context.update(
            {
                'students_statistics': listOfStats,
                #[{'id': n,
                #                          'fio': Student.name,
                #                          'timp': random.randint(2,5),
                #                          'eis': random.randint(2,5),
                #                          'philosophy': random.randint(2,5),
                #                          'english': random.randint(2,5),
                #                          'sport': random.randint(2,5)
                #                          } for n in range(len(listOfStudents))],
                # 'students_statistics': [
                #     {
                #         #'id': stud1.id,
                #         'fio' : stud1.name,
                #         # 'timp': 322,
                #         # 'eis': 3,
                #          'philosophy': 4,
                #         # 'english': 5,
                #         # 'sport': 2.3,
                #         # 'average': 2.3,
                #     },
                # ],
                    'excellent_students': Statistics.ExcStudents,
                    'bad_students': Statistics.BadStudents
            }
        )
        return context


class Student: #id,fio
    pass


class Statistics: #badStudents, excStudents
    # student_id, [Subjects]
    pass

class Subject:
    pass

class Score: #eis, fil, timp, eng, sport
    # Subject,
    pass