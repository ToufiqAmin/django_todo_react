from django.contrib import admin
#import models of the project
from .models import Todo

#define class and refister model to see our CRUD operations
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed')

# Register your models here.

admin.site.register(Todo, TodoAdmin)
