from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("Главная страничка")


def group_posts(request, slug):
    return HttpResponse(f"Груповая страничка с параметром {slug}")
