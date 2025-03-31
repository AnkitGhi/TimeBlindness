
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('create', views.task_register, name="register task"),
    path('submission/<int:task_id>',views.task_completion, name="submit_task"),
    path('view', views.view_tasks, name ="view tasks")

]
