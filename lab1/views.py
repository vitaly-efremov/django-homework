# -*- coding: utf-8 -*-
from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        spisokFIO = ['Petr Petrov', 'Ivan Ivanov', 'Nikolay Sidorov', 'Aleksey Molotov', 'Viktor Dragunov', 'Konstantin Kovrov', 'Sergey Korolev', 'Yuriy Gagarin', 'Aleksandr Suvorov','Aleksandr Pushkin']
        import random
        spisokTIMP = []
        spisokEIS = []
        spisokPHIL = []
        spisokENG = []
        spisokSPORT = []

        inf=[]
        otl=[]
        otch=[]

        for i in range(len(spisokFIO)):
            spisokTIMP.append(random.randint(2, 5))
            spisokEIS.append(random.randint(2, 5))
            spisokPHIL.append(random.randint(2, 5))
            spisokENG.append(random.randint(2, 5))
            spisokSPORT.append(random.randint(2, 5))
            k=(spisokPHIL[i] + spisokTIMP[i] + spisokEIS[i] + spisokENG[i] + spisokSPORT[
                    i]) / 5
            spis = {
                'id': i+1,
                'fio': spisokFIO[i],
                'timp': spisokTIMP[i],
                'eis': spisokEIS[i],
                'philosophy': spisokPHIL[i],
                'english': spisokENG[i],
                'sport': spisokSPORT[i],
                'average': k
            }
            inf.append(spis)
            if k==5:
                otl.append(spisokFIO[i])

            if k < 3:
                otch.append(spisokFIO[i])



        context = super(IndexView, self).get_context_data(**kwargs)
        context.update(
            {
                'students_statistics': inf,

                'excellent_students': otl,
                'bad_students': otch
            }
        )
        return context



