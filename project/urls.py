from django.contrib import admin
from django.urls import path
import posts.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', posts.views.main, name='main'),
    path('create/', posts.views.create, name='create'),
    path('read/', posts.views.read, name='read'),
    path('detail/<str:id>', posts.views.detail, name='detail'),
]
