from django.shortcuts import render, redirect
from .models import Todolist
# Create your views here.
def index(request):
    todos = Todolist.objects.all()
    context = {
        'todos' : todos,
    }
    return render(request, 'todos/index.html', context)

def new(request):
    return render(request, 'todos/new.html')

def create(request):
    title = request.POST.get('title')
    description = request.POST.get('description')
    # created_at = request.POST.get('created_at')
    # completed = request.POST.get('completed')
    important = request.POST.get('important')

    todo = Todolist(title=title, description=description, important=important)
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
    todo.important = request.POST.get('important')
    todo.save()
    return redirect('todos:detail', todo.pk)