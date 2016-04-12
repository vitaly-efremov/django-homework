from django.conf.urls import patterns, url

from django.contrib import admin

from .views import IndexView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', IndexView.as_view()),
)
