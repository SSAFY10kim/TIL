from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('pjt04/admin/', admin.site.urls),
    path('pjt04/weathers/', include('weathers.urls'))
]
