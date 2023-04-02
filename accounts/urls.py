from django.urls import path
from . import views

app_name = 'user'
urlpatterns = [
    path('login', views.login_page, name='login'),
    path('logout/', views.login_page, name='logout'),
    path('register/', views.register_page, name='register'),
    path('password-reset/', views.forgot_password, name='password-reset'),
    # path('', views.index, name='index'),
    # path('home/', views.home, name='home'),


    path('profile/<str:pk>/', views.user_profile, name='profile'),
]
