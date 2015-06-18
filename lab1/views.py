from django.views.generic.base import TemplateView, View

from django.shortcuts import redirect

from models import Client, Dogov, Card, Oper

class Clients_Add(View):
      def post(self, *args, **kwargs):
        nomer_id_value = self.request.POST['nomer_id']
        familia_value = self.request.POST['familia']
        name_value = self.request.POST['name']
        otchestvo_value = self.request.POST['otchestvo']
        pol_value = self.request.POST['pol']
        data_value = self.request.POST['data']
        mobile = self.request.POST['mobile']
        nomer_dogovora_value = self.request.POST['nomer_dogovora']
        Client.objects.create(nomer_id=nomer_id_value,
                              familia=familia_value, name=name_value, otchestvo=otchestvo_value,
                              pol=pol_value, data=data_value, mobile=mobile, nomer_dogovora=nomer_dogovora_value)
        return redirect('/')

class Dogov_Add(View):
      def post(self, *args, **kwargs):

        iddog_value = self.request.POST['iddog']
        uslov_value = self.request.POST['uslov']
        data1_value = self.request.POST['data1']
        idcard_value = self.request.POST['idcard']
        Dogov.objects.create(uslov=uslov_value,
                              data1=data1_value, idcard=idcard_value, iddog=iddog_value)
        return redirect('/')

class Card_Add(View):
      def post(self, *args, **kwargs):
        idcard_value = self.request.POST['idcard']
        valid_value = self.request.POST['valid']
        data2_value = self.request.POST['data2']
        nomer_oper_value = self.request.POST['nomer_oper']
        Card.objects.create(valid=valid_value,
                              idcard=idcard_value, data2=data2_value, nomer_oper=nomer_oper_value)
        return redirect('/')

class Oper_Add(View):
      def post(self, *args, **kwargs):

        nomer_oper_value = self.request.POST['nomer_oper']
        opera_value = self.request.POST['opera']
        data3_value = self.request.POST['data3']
        Oper.objects.create(nomer_oper=nomer_oper_value,
                              opera=opera_value, data3=data3_value)
        return redirect('/')


class DeleteClient(View):
    def post(self, *args, **kwargs):
        info_delete = self.request.POST['delete_info']
        Client.objects.filter(id=int(info_delete)).delete()
        return redirect('/')


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):

        context = super(IndexView, self).get_context_data(**kwargs)
        dogovs_view = Dogov.objects.all()
        clients_view = Client.objects.all()
        card_view = Card.objects.all()
        oper_view = Oper.objects.all()
        context.update(
            {
            'clients_view': clients_view,
            'dogovs_view': dogovs_view,
            'card_view': card_view,
            'oper_view': oper_view,
            }
        )
        return context
# Create your views here.
