from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Tool


@admin.register(Tool)
class ToolAdmin(SummernoteModelAdmin):

    list_display = ['tool_name', 'author_name', 'published_status', 'date_added']
    search_fields = ['tool_name', 'method_details', 'keywords']
    prepopulated_fields = {'slug': ('tool_name',)}
    list_filter = ('date_added', 'published_status', 'author_name')
    summernote_fields = ('method_details')
