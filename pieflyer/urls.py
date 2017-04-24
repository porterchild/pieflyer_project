from django.conf.urls import url
from django.views.generic.base import TemplateView
from . import views

app_name = 'pieflyer'
urlpatterns = [
    ##url(r'^$', views.game, name='game'),
    url(r'^$', TemplateView.as_view(template_name='pieflyer/gamedoc.html')),
]