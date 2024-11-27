from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def best_team(request):
    return HttpResponse('<h1>INDIA</h1>')