from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name = 'home'),
    path('create_todo/', views.create_todo, name = 'create_todo'),
    path('todo_list/', views.todo_list, name = 'todo_list'),
    path('view_todo/<int:todo_id>', views.view_todo, name = 'view_todo'),
    path('edit_todo/<int:todo_id>', views.edit_todo, name = 'edit_todo'),
    path('completed_list/', views.completed_list, name = 'completed_list'),
    path('register/', views.register, name = 'register'),
]
