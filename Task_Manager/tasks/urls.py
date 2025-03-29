from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.task,name='task'),
    path('add/',views.create_tasks,name='add-task')

]