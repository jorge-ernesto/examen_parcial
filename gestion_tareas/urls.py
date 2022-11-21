from django.urls import path
from . import views

urlpatterns = [
    path('tareas/', views.list, name="list_tareas"),
]
