from django.conf.urls import patterns, url

from django.contrib import admin

from views import IndexView, Clients_Add, Dogov_Add, Card_Add, Oper_Add, DeleteClient

#from django.conf.urls import patterns, url


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Lab2_723_prp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^client_add', Clients_Add.as_view()),
    url(r'^dogov_add', Dogov_Add.as_view()),
    url(r'^card_add', Card_Add.as_view()),
    url(r'^oper_add', Oper_Add.as_view()),
    url(r'^delete_info', DeleteClient.as_view()),
    url(r'^$', IndexView.as_view()),
)
