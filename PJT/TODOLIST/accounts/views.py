from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomAuthenticationForm, CustomUserChangeForm, CustomPasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import (
    require_http_methods,
    require_POST,
)
from django.http import JsonResponse

# Create your views here.
@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.method=='POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')

    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)

def logout(request):
    auth_logout(request)
    return redirect('todos:index')


@require_http_methods(['GET', 'POST'])
def login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('todos:index')
    else:
        form = CustomAuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)

def delete(request):
    request.user.delete()
    return redirect('todos:index')

@require_http_methods(['GET', 'POST'])
def change(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('todos:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/change.html', context)

@require_http_methods(['GET', 'POST'])
def change_password(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user=form.save()
            update_session_auth_hash(request, user)
            return redirect('todos:index')
    else:
        form = CustomPasswordChangeForm(request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/change_password.html', context)


def profile(request, username):
    User = get_user_model()
    person = User.objects.get(username=username)
    context = {
        'person' : person,
    }
    return render(request, 'accounts/profile.html', context)

@login_required
def follow(request, user_pk):
    User = get_user_model()
    you = User.objects.get(pk=user_pk)
    me = request.user
    if you != me:
        if me in you.followers.all():
            you.followers.remove(me)
            is_followed = False
        else:
            you.followers.add(me)
            is_followed = True
        context = {
            'is_followed' : is_followed,
            'followings_count' : you.followings.count(),
            'followers_count' : you.followers.count(),
        }
        return JsonResponse(context)
    return redirect('accounts:profile', you.username)