from django.contrib import admin
from django.contrib.admin import ModelAdmin
from todos.models import Todo

# Register your models here.
class TodoAdmin(ModelAdmin):
    # Add the 'profile_pic' field to the user display in the admin panel
    pass

# Register your custom user model with the custom admin class
admin.site.register(Todo, TodoAdmin)