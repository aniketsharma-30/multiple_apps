from django.urls import path
from IPL.views import *
urlpatterns=[
    path('best_team/',best_team,name='beat_team')
    
]