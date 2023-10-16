from django.urls import path
from . import views

app_name = 'trends'
urlpatterns = [
    path('', views.index, name='index'),
    path('keyword/', views.keyword, name='keyword'),
    path('keyword/<int:pk>/', views.delete_keyword, name='delete_keyword'),
    path('crawling/', views.crawling, name='crawling'),
    path('crawling/histogram', views.histogram, name='histogram'),
    path('crawling/advanced/', views.advanced, name='advanced'),
]
