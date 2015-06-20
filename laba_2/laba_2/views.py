# -*- coding: utf-8 -*-

from django.views.generic.base import TemplateView
from models import Client, Master, Repairing

class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        allclient = Client.objects.all()
        allmaster = Master.objects.all()
        allrep = Repairing.objects.all()
        context.update(
            {
                'clients': allclient,
                'masters': allmaster,
                'rep': allrep,
            }
        )
        return context