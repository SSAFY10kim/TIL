from django.urls import path, include
from . import views

app_name = 'todos'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/update/', views.update, name='update'),
    path('compindex/', views.compindex, name='compindex'),
    path('<int:pk>/completed/', views.completed, name='completed'),
    path('<int:pk>/compdetail/', views.compdetail, name='compdetail'),
    path('reset/', views.reset, name='reset'),
    path('board/', views.board, name='board'),
    path('<int:pk>/board/', views.board_detail, name='board_detail'),
    ]


# 자유게시판 detail(삭제, 완료 안보이게), 댓글, 좋아요, 팔로우