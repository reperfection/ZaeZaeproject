from django.urls import path
from posts import views

urlpatterns = [
    path('', views.main, name='main'),
    path('create/', views.create, name='create'),
    path('read/', views.read, name='read'),
    path('detail/<str:id>', views.detail, name='detail'),
    path('edit/<str:id>/', views.edit, name='edit'),
    path('delete/<str:id>/', views.delete, name='delete'),
    path('mypage/', views.mypage, name='mypage'),
    path('edituser/', views.edituser, name='edituser'),
]