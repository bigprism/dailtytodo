from django.urls import path
from .views import todo_list_api, todo_create_api, todo_update_api, todo_delete_api

urlpatterns = [
    path('api/todo/', todo_list_api, name='todo_list_api'),
    path('api/todo/create/', todo_create_api, name='todo_create_api'),
    path('api/todo/<int:pk>/update/', todo_update_api, name='todo_update_api'),
    path('api/todo/<int:pk>/delete/', todo_delete_api, name='todo_delete_api'),
]