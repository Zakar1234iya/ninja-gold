from django.urls import *
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('process_money', views.process_money, name='process_money'),
    path('save_score', views.save_score, name='save_score'),
    path('highscore', views.highscore, name='highscore'),
    path('reset', views.reset, name='reset'),
]
