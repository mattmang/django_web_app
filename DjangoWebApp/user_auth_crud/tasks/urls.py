from django.urls import path
from django.conf import settings
from . import views

urlpatterns =[
    path('tasks/', views.task_list, name='task_list'),
    path('details/<int:pk>/', views.task_details, name='task_details'),
    path('create/', views.task_create, name='task_create'),
    path('update/<int:pk>/', views.task_update, name='task_update'),
    path('delete/<int:pk>/', views.task_delete, name='task_delete'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]