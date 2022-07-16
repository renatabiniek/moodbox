from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Tool


@admin.register(Tool)
class ToolAdmin(SummernoteModelAdmin):

    summernote_fields = ('method_details')
