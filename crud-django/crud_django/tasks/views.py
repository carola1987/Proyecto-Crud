from django.shortcuts import render, redirect
from .models import Task

# Create your views here.


def index(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/index.html', {'tasks': tasks})


def add_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        if title and description:
            Task.objects.create(title=title, description=description)
            return redirect('index')
    return render(request, 'tasks/add_task.html')


def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('index')
