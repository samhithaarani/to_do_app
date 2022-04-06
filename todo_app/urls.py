from django.urls import path
from.views import viewtodo,addtodo,deltodo
urlpatterns = [
    path('viewtodo',viewtodo),
    path('addtodo',addtodo),
    path('deltodo<int:todo_id>',deltodo)
]
