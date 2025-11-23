from django.contrib import admin
from django.urls import path, include
from .views import homepage, about

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='homepage'),       # http://127.0.0.1:8000/
    path('about/', about, name='about'), 
    path('products/', include('products.urls')),  # http://127.0.0.1:8000/products/
]
