from django import forms
from .models import Comment, Tool


class CommentForm (forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)


class ToolForm (forms.ModelForm):
    """Form to add new tool"""
    class Meta:
        model = Tool
        fields = ('tool_name', 'keywords', 'method_details', 'time_required', 'related_website', 'related_image',)
