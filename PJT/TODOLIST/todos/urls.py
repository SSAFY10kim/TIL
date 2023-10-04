from django.urls import path, include
from . import views

app_name = 'todos'
urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/update/', views.update, name='update'),
    path('compindex/', views.compindex, name='compindex'),
    path('<int:pk>/completed/', views.completed, name='completed'),
    path('<int:pk>/compdetail/', views.compdetail, name='compdetail'),
    path('reset/', views.reset, name='reset'),
    ]