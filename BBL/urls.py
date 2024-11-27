from django.urls import path
from BBL.views import *
urlpatterns=[
    path('best_team/',best_team,name='best_team')
]