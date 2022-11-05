from django.urls import path
from posts import views

urlpatterns = [
    path('', views.main, name='main'),
    path('create/', views.create, name='create'),
    path('read/', views.read, name='read'),
    path('detail/<str:id>', views.detail, name='detail'),
    path('edit/<str:id>/', views.edit, name='edit'),
    path('delete/<str:id>/', views.delete, name='delete'),
    path('comment/update/<int:postid>/<int:commentid>/', views.update_comment, name="update_comment"),
    path('comment/delete/<int:postid>/<int:commentid>', views.delete_comment, name="delete_comment"),
    path('search/hashtag/', views.hashtag_search, name='hashtag_search'),
    path('like/<str:id>/', views.likes, name='likes'),
]