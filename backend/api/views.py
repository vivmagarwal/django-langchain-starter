from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Task

# Create your views here.
def index(request):
  return JsonResponse({'message': 'Hello, world!'})

@csrf_exempt
def add_task(request):
  print(request.body)
  if request.method == 'POST':
    try:
      data = json.loads(request.body)
      title = data['title']
      completed = data['completed']
      task = Task.objects.create(title=title, completed=completed)
      return JsonResponse({
        'id': task.id,
        'title': task.title,
        'completed': task.completed,
        'created_at': task.created_at
      }, status=201) 
    except:
      return JsonResponse({'message': 'Invalid data!'})

  return JsonResponse({'message': 'Invalid method!'}, status=405)  




