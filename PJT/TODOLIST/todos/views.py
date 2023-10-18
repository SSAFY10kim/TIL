from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Todolist, Comment
from django.utils import timezone
from datetime import datetime
from .forms import TodolistForm, CommentForm
from django.http import HttpResponseForbidden

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

@login_required
def create(request):
    if request.method == 'POST':
        form = TodolistForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            form.save()
            return redirect('todos:index')
    else:
        form = TodolistForm()
    context = {
        'form' : form,
    }
    return render(request, 'todos/new.html', context)

@login_required
def detail(request, pk):
    todo = get_object_or_404(Todolist, pk=pk)
    if request.user != todo.user:
        return HttpResponseForbidden(
            '<a href="http://127.0.0.1:8000/">[BACK]</a>'
            )
    context = {
        'todo' : todo,
    }
    return render(request, 'todos/detail.html', context)

@login_required
def delete(request, pk):
    todo = Todolist.objects.get(pk=pk)
    todo.delete()
    return redirect("todos:index")

@login_required
def edit(request, pk):
    todo = Todolist.objects.get(pk=pk)
    if request.method == "POST":
        form = TodolistForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todos:detail', todo.pk)
    else:
        form = TodolistForm(instance=todo)
    context = {
        'todo' : todo,
        'form' : form,
    }
    return render(request, 'todos/edit.html', context)

@login_required
def compindex(request):
    todos = Todolist.objects.filter(completed=True)
    context = {
        'todos' : todos,
    }
    return render(request, 'todos/completed.html', context)

@login_required
def completed(request, pk):
    todo = Todolist.objects.get(pk=pk)
    todo.completed = True
    todo.save()
    return redirect('todos:index')

@login_required
def uncompleted(request, pk):
    todo = Todolist.objects.get(pk=pk)
    todo.completed = False
    todo.save()
    return redirect('todos:index')

@login_required
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

@login_required
def reset(request):
    Todolist.objects.all().delete()
    return redirect('todos:index')

def board(request):
    todos = Todolist.objects.filter(completed=False, check_share=True)
    d_days = []
    for todo in todos:
        remaining_days = (todo.target_day - timezone.now().date()).days
        d_days.append(remaining_days)
    combined_data = list(zip(todos, d_days))
    
    context = {
        'combined_data': combined_data,
    }
    return render(request, 'todos/board.html', context)

def board_detail(request, pk):
    todo = Todolist.objects.get(pk=pk)
    comment_form = CommentForm()
    comments = todo.comment_set.all()
    context = {
        'todo' : todo,
        'comment_form' : comment_form,
        'comments' : comments,
    }
    return render(request, 'todos/boarddetail.html', context)

@login_required
def comments_create(request, pk):
    todo = Todolist.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.todo = todo
        comment.user = request.user
        comment_form.save()
        return redirect('todos:board_detail', todo.pk)
    context = {
        'todo' : todo,
        'comment_form' : comment_form,
    }
    return render(request, 'todos/boarddetail.html', context)

@login_required
def comments_delete(request, todo_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.user == comment.user:
        comment.delete()
    return redirect('todos:board_detail', todo_pk)

@login_required
def likes(request, pk):
    todo = Todolist.objects.get(pk=pk)
    if request.user in todo.like_users.all():
        todo.like_users.remove(request.user)
    else:
        todo.like_users.add(request.user)
    return redirect('todos:board_detail', pk)