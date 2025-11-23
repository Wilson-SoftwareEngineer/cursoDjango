from django.contrib import admin
from django.urls import path
from .views import homepage, about

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='homepage'),       # http://127.0.0.1:8000/
    path('about/', about, name='about'),       # http://127.0.0.1:8000/about/
]
