

# Register your models here.
from django.contrib import admin
from .models import Todo

class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'complete', 'created_at', 'user')
    list_filter = ('complete', 'created_at')
    search_fields = ('title', 'description')

admin.site.register(Todo, TodoAdmin)