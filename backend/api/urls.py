from django.urls import path

from api import views

urlpatterns = [
    path('matches', views.matches, name="matches")
]