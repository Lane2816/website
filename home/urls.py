from django.urls import path

from . import views

urlpatterns = [
    path('', views.viewIt, name='index'),
]