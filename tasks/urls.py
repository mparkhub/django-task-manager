from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('create/', views.create_task, name='create_task'),
    path('task/<int:pk>/edit/', views.update_task, name='update_task'),
    path('task/<int:pk>/delete/', views.delete_task, name='delete_task'),
]
