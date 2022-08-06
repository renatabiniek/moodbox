from django import forms
from django.core.exceptions import ValidationError
from .models import Comment, Tool


class CommentForm (forms.ModelForm):
    """Form to add new comment to a tool"""
    class Meta:
        model = Comment
        fields = ('content',)


class ToolForm (forms.ModelForm):
    """Form to add new tool"""
    class Meta:
        model = Tool
        fields = (
            'tool_name',
            'keywords',
            'category',
            'method_details',
            'time_required',
            'related_website',
            'related_image',
            )
        help_texts = {
            'tool_name': 'What is this technique called?',
            'keywords': 'When is it helpful? '
            'Add upto 3 keywords.',
            'method_details': 'What does it involve? '
            'Describe the idea behind it and any steps needed.',
            'time_required': 'How much time will it take '
            'to try this technique out? Add estimated time '
            'in fraction of an hour.',
            'related_website': 'Add URL address to additional related resources.',
            'related_image': 'Add any relevant image.',
        }


# def clean_file(self):
#     '''
#     Validates the file type on the related_image
#     field to match the only allowed file types
#     '''

#     data = self.cleaned_data['related_image']
#     if data:
#         try:
#             filename = data.name
#             if not filename.endswith(('.jpg', '.png')):
#                 print("error")
#                 raise forms.ValidationError("File type must be .jpg. Try uploading another file.")
#         except AttributeError:
#             pass
#     return data


