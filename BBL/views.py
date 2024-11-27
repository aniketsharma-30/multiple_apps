from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def best_team(request):
    return HttpResponse('<h1>PERTH SCOCHERS</h1>')
