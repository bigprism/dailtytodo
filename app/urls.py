from django.urls import path
from .views import todo_list, todo_create, todo_update, todo_delete

urlpatterns = [
    path('todo/', todo_list, name='todo_list'),
    path('todo/create/', todo_create, name='todo_create'),
    path('todo/<int:pk>/update/', todo_update, name='todo_update'),
    path('todo/<int:pk>/delete/', todo_delete, name='todo_delete'),
]