from django.urls import path
from accounts import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('mypage/', views.mypage, name='mypage'),
    path('edituser/', views.edituser, name='edituser'),
    path('passwordchange/', views.passwordchange, name='passwordchange'),
    path('register/', views.register, name='register'),
]