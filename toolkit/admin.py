from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Tool, Comment, Category


@admin.register(Tool)
class ToolAdmin(SummernoteModelAdmin):

    list_display = ('tool_name', 'author_name', 'category', 'published_status', 'date_added')
    search_fields = ['tool_name', 'method_details', 'keywords']
    prepopulated_fields = {'slug': ('tool_name',)}
    list_filter = ('date_added', 'published_status', 'author_name')
    summernote_fields = ('method_details')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    
    list_display = ('tool', 'name', 'content', 'date_added', 'approved')
    list_filter = ('name', 'date_added', 'approved')
    search_fields = ['name', 'content']
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


# admin.site.register(Category)
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)}
