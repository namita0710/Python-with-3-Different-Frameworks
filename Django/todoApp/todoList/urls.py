from . import views
from django.urls import path

urlpatterns = [
    path("",views.home,name="home"),
    path("home",views.home,name="home"),
    path("index",views.index,name="index"),
    path('add', views.add, name='add'),  # Route for adding a to-do item
    path('update/<int:todo_id>', views.update, name='update'),  # Route for updating a to-do item
    path('delete/<int:todo_id>', views.delete, name='delete'),  # Route for deleting a to-do item
]
