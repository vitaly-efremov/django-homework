from django.conf.urls import patterns, url

from django.contrib import admin

from .views import IndexView

import os

admin.autodiscover()

site_media = os.path.join(os.path.dirname(__file__), 'static')

urlpatterns = patterns('',
                       url(r'^static/(?P<path>.*)$',
                           'django.views.static.serve',
                           {'document_root': site_media}),
                       url(r'^$', IndexView.as_view()),
                       )
