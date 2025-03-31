from django.contrib import admin
from .models import Task_register, Task_complete


admin.site.register(Task_register)
admin.site.register(Task_complete)
