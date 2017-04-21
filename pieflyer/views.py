from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import Context, loader

# Create your views here.
def game(request):
    template = loader.get_template("pieflyer/gamedoc.html")
    return HttpResponse(template.render)

    


def index(request):
    template = loader.get_template("app/index.html")
    return HttpResponse(template.render)