from django.contrib import admin
from .models import Task
from .models import User

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')

class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'age')
admin.site.register(User, UserAdmin)