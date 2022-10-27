from django.contrib import admin
from django.urls import path,include
from .views import *


urlpatterns = [
    # home
    path('',home),
    path('update-todo/',update_todo,name="update_todo"),
    path('delete-todo/<id>',delete_todo,name="delete_todo"),

]