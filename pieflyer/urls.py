from django.conf.urls import url

from . import views

app_name = 'pieflyer'
urlpatterns = [
    url(r'^$', views.game, name='index'),
]