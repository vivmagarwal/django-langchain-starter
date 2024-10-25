from django.urls import path
from .views import index, add_task, get_prediction

urlpatterns = [
    path('', index, name='index'),
    path('add-task', add_task, name='add_task'),
    path('predict', get_prediction, name='get_prediction'),
]
