from django.views.generic.base import TemplateView

class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        spisok = ['Ажель Никита', 'Дмитрий Световец', '', '', '', '', '', '', '', '']       
        student = []
        for i in range(len(spisok)):
                student.append(Student(i, spisok[i]))
        statistics = []
        whitelist = []
        blacklist = []
        for i in range(len(spisok)):
            if student[i].avg >= 4:
                whitelist.append(student[i].studentname)
            elif student[i].avg < 3:
                blacklist.append(student[i].studentname)
            statistics.append({'id': student[i].id, 'fio': student[i].studentname, 'average': student[i].avg, 'timp': student[i].score[0], 'eis': student[i].score[1],
                                'philosophy': student[i].score[2], 'english': student[i].score[3], 'sport': student[i].score[4]})

        context.update(
            {
                'students_statistics': statistics,
                'excellent_students': whitelist,
                'bad_students': blacklist
            }

        )
        return context

class Student:
        def __init__(self,num,name):
                self.studentname = name
                self.id = num
                self.s = Subject().subjList
                self.score = Score(self.s).scoreList
                self.avg = Statistics.getAvg(self.score)

class Statistics:
        def getAvg(sc):
                sum=0
                for i in sc:
                        sum+=i
                avg=sum/5
                return avg

class Subject:
        def __init__(self):
                self.subjList = ['timp','eis','philosophy','english','sport']

import random
class Score:
        def __init__(self,subj):
                self.scoreList = []
                for n in subj:
                        self.scoreList.append(random.randint(2, 5))
