from django.urls import path
from .views import index, add_task

urlpatterns = [
    path('', index, name='index'),
    path('add-task', add_task, name='add_task'),
]