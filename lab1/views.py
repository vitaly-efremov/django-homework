from django.views.generic.base import TemplateView


class Student(object):
    def __init__(self, numb, fio):
        self.student = dict(zip(numb, fio))

    def get_fio(self, numb):
        return self.student.setdefault(numb)


class Statistics(object):
    def __init__(self, mark):
        self.mark = mark

    def _average_mark(self):
        return float(sum(self.mark)) / len(self.mark)

    def format_record(self, numb, fio, predmet):
        inform = {'id':numb, 'fio':fio}
        tmp = dict(zip(predmet, self.mark))
        inform.update(tmp)
        inform.update({'average':self._average_mark()})
        return inform


class Subject(object):
    def __init__(self, subject):
        self.subject = subject

    def get_subject(self):
        return self.subject


class Score(object):
    def __init__(self, mark, numb):
        self.student_assessment = dict(zip(numb, mark))

    def get_mark(self, numb):
        return self.student_assessment.setdefault(numb)

    def otchislit(self):
        tmp = self.student_assessment.items()
        return [i[0] for i in tmp if i[1].count(2) != 0]

    def otlichnik(self, number_of_subjects):
        tmp = self.student_assessment.items()
        return [i[0] for i in tmp if i[1].count(5) == number_of_subjects]

#--------------------------------------------Организуем ввод данных------------------------------------------------------------------------
spisok_studentov = []
b = Student([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], ['Толмачев В.С.', 'Гоголь Н.В.', 'Чехов А.П.', 'Толстой Л.Н.', 'Пушкин А.С.', 'Тургенев И.С.', 'Некрасов Н.А.'])
c = Subject(['timp', 'finansy', 'philosophy', 'english', 'sport'])
d = Score([[5, 5, 5, 5, 5], [2, 2, 2, 3, 3], [3, 5, 4, 4, 5], [3, 5, 5, 4, 5], [3, 5, 3, 4, 5], [5, 5, 4, 4, 5], [3, 5, 4, 4, 5]], [1, 2, 3, 4, 5, 6, 7])
for i in range(1,8):
    a = Statistics(d.get_mark(i))
    spisok_studentov.append(a.format_record(i, b.get_fio(i), c.get_subject()))
#---------------------------------------------------Готово!-------------------------------------------------------------------------------


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        otchislit = ' , '.join(b.get_fio(i) for i in d.otchislit())
        otlichnik = ' , '.join(b.get_fio(i) for i in d.otlichnik(5))
        
        context.update(
            {
                'students_statistics': spisok_studentov,
                'excellent_students': otlichnik,
                'bad_students': otchislit
            }
        )
        return context


