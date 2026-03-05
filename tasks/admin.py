from django.contrib import admin
from .models import Task, Category, Tag


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'owner', 'priority', 'status', 'due_date', 'category']
    list_filter = ['priority', 'status', 'category']
    search_fields = ['title', 'description']
    filter_horizontal = ['tags']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'color', 'created_by']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_by']
