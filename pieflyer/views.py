from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import Context, loader
from .models import Score

# Create your views here.
def game(request):
    template = loader.get_template("pieflyer/gamedoc.html")
    
    highest_score_list = Score.objects.order_by('-score')[:5]
    context = {'highest_score_list': highest_score_list}
    
    return HttpResponse(template.render)

    
    
def index(request):
    highest_score_list = Score.objects.order_by('-score')[:5]
    context = {'highest_score_list': highest_score_list}