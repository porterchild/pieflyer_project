from django.conf.urls import url
from django.views.generic.base import TemplateView
from . import views

app_name = 'pieflyer'
urlpatterns = [
    url(r'^', views.index, name='index'),
    url(r'^record_score/$', views.record_score, name='record_score'),
    ##url(r'^$', TemplateView.as_view(template_name='pieflyer/gamedoc.html')),
]