from django.urls import path
from .views import *

urlpatterns = [
    path('projects/', project_list),
    path('projects/<int:pk>/', project_detail),
    path('tasks/', task_list),
    path('tasks/<int:pk>/', task_detail),
    path('users/', user_list),
    path('users/<int:pk>/', user_detail)
]