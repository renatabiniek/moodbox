"""Register the models for the 'toolkit' app for admin panel"""
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Tool, Comment, Category


@admin.register(Tool)
class ToolAdmin(SummernoteModelAdmin):
    """Enable admin setup with list of fields and filters
    for the Tool model.
    """

    list_display = (
        'tool_name', 'author_name', 'category',
        'published_status', 'date_added'
        )
    search_fields = ['tool_name', 'method_details', 'keywords']
    list_filter = ('date_added', 'published_status', 'author_name')
    prepopulated_fields = {'slug': ('tool_name',)}
    summernote_fields = ('method_details',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Enable admin setup with list of fields and filters
    for the Comment model.
    """
    list_display = ('tool', 'name', 'content', 'date_added', 'approved')
    list_filter = ('name', 'date_added', 'approved')
    search_fields = ['name', 'content']
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        """Update comment status to approved"""
        queryset.update(approved=True)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Enable admin setup for the Category model."""
    prepopulated_fields = {'slug': ('category_name',)}
