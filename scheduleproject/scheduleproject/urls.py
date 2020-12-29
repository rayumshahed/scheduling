from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('schedule/', include('scheduleapp.urls')),
    path('admin/', admin.site.urls),
]