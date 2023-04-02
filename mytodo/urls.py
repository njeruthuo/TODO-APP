from . import views
from django.urls import path


app_name = 'mytodo'
urlpatterns = [
    path('', views.index, name='index'),
    path('todo-list/<str:pk>/', views.todo_view, name='todo-view'),
    path('change-todo/<str:pk>/', views.change_todo, name='modify'),
    path('delete/<str:pk>/', views.delete_todo, name='delete'),
    path('create/', views.create_todo, name='create'),
]
