# -*- coding: utf-8 -*-
from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update(
            {
                'students_statistics': [
                    {
                        'id': 1,
                        'fio': 'Кайзер Екатерина Александровна',
                        'timp': 5,
                        'bsbd': 5,
                        'philosophy': 5,
                        'english': 5,
                        'sport': 5,
                        'average': 5,},

                    {'id': 2,
                        'fio': 'Свешникова Юлия Руслановна',
                        'timp': 5,
                        'bsbd': 5,
                        'philosophy': 5,
                        'english': 5,
                        'sport': 5,
                        'average': 5,},
                    {'id': 3,
                        'fio': 'Ковалев Вячеслав Юрьевич',
                        'timp': 5,
                        'bsbd': 4,
                        'philosophy': 4,
                        'english': 4,
                        'sport': 3,
                        'average': 5,},
                    {'id': 4,
                        'fio': 'Шорохова Елизавета Витальевна',
                        'timp': 5,
                        'bsbd': 5,
                        'philosophy': 5,
                        'english': 4,
                        'sport': 3,
                        'average': 5,},
                    {'id': 5,
                        'fio': 'Иванов Алексей Владимирович',
                        'timp': 3,
                        'bsbd': 3,
                        'philosophy': 4,
                        'english': 3,
                        'sport': 2,
                        'average': 5,},
                    {'id': 6,
                        'fio': 'Козлова Людмила Сергеевна',
                        'timp': 2,
                        'bsbd': 3,
                        'philosophy': 2,
                        'english': 3,
                        'sport': 5,
                        'average': 5,},
                    {'id': 7,
                        'fio': 'Аршавин Андрей Андреевич',
                        'timp': 2,
                        'bsbd': 3,
                        'philosophy': 2,
                        'english': 3,
                        'sport': 5,
                        'average': 5,},
                     {'id': 8,
                        'fio': 'Коротков Иван Андреевич',
                        'timp': 2,
                        'bsbd': 3,
                        'philosophy': 3,
                        'english': 3,
                        'sport': 5,
                        'average': 5,},
                     {'id': 9,
                        'fio': 'Никитюк Никита Игоревич',
                        'timp': 5,
                        'bsbd': 4,
                        'philosophy': 5,
                        'english': 4,
                        'sport': 5,
                        'average': 5,},
                    {'id': 10,
                        'fio': 'Галузо Олеся Олеговна',
                        'timp': 5,
                        'bsbd': 5,
                        'philosophy': 4,
                        'english': 4,
                        'sport': 4,
                        'average': 5,}
                ],
                'excellent_students': 'Кайзер, Student B',
                'bad_students': 'Козлова, Student D'
            }
        )
        return context


class Student:
    pass


class Statistics:
    # student_id, [Subjects]
    pass

class Subject:
    pass

class Score:
    # Subject,
    pass