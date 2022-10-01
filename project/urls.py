from django.contrib import admin
from django.urls import path
import posts.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', posts.views.main, name='main'),
    path('create/', posts.views.create, name='create'),
    path('read/', posts.views.read, name='read'),
    path('detail/<str:id>', posts.views.detail, name='detail'),
    path('edit/<str:id>/', posts.views.edit, name='edit'),
    path('delete/<str:id>/', posts.views.delete, name='delete'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)