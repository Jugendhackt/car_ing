from django.urls import path

from api import views

urlpatterns = [
    path('matches', views.matches, name="matches"),
    path('registercar', views.registercar, name="registercar"),
    path('registeruser', views.registeruser, name="registeruser")
]