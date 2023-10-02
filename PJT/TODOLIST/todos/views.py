from django.shortcuts import render, redirect
from .models import Todolist
from django.utils import timezone
from datetime import datetime

# Create your views here.
def index(request):
    todos = Todolist.objects.filter(completed=False)
    d_days = []
    for todo in todos:
        remaining_days = (todo.target_day - timezone.now().date()).days
        d_days.append(remaining_days)
    combined_data = list(zip(todos, d_days))
    
    context = {
        'combined_data': combined_data,
    }
    return render(request, 'todos/index.html', context)

def new(request):
    return render(request, 'todos/new.html')

def create(request):
    title = request.POST.get('title')
    description = request.POST.get('description')
    # created_at = request.POST.get('created_at')
    completed = request.POST.get('completed', False)
    important = request.POST.get('important', False)
    target_day = request.POST.get('target_day')

    todo = Todolist(title=title, description=description, completed=completed, important=important, target_day=target_day)
    todo.save()
    return redirect('todos:index')

def detail(request, pk):
    todo = Todolist.objects.get(pk=pk)
    context = {
        'todo' : todo,
    }
    return render(request, 'todos/detail.html', context)

def delete(request, pk):
    todo = Todolist.objects.get(pk=pk)
    todo.delete()
    return redirect("todos:index")

def edit(requets, pk):
    todo = Todolist.objects.get(pk=pk)
    context = {
        'todo' : todo,
    }
    return render(requets, 'todos/edit.html', context)

def update(request, pk):
    todo = Todolist.objects.get(pk=pk)
    todo.title = request.POST.get('title')
    todo.description = request.POST.get('description')
    todo.important = request.POST.get('important', False)
    todo.target_day = request.POST.get('target_day')
    todo.save()
    return redirect('todos:detail', todo.pk)

def compindex(request):
    todos = Todolist.objects.filter(completed=True)
    context = {
        'todos' : todos,
    }
    return render(request, 'todos/completed.html', context)

def completed(request, pk):
    todo = Todolist.objects.get(pk=pk)
    todo.completed = True
    todo.save()
    return redirect('todos:index')

def compdetail(request, pk):
    todo = Todolist.objects.get(pk=pk)
    context = {
        'todo' : todo,
    }
    return render(request, 'todos/compdetail.html', context)

def cal_d_day(request, todo_id):
    todo = Todolist.objects.get(id=todo_id)
    cur_date = datetime.now()
    d_day = (todo.target_day - cur_date).days()
    context = {
        'd_day' : d_day,
    }
    return render(request, 'todos/index.html', context)

def reset(request):
    Todolist.objects.all().delete()
    return redirect('todos:index')