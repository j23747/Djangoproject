from django.urls import path
from . import views

urlpatterns = [
    path('', views.jokes, name = 'jokes')
]