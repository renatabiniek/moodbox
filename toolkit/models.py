from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from ckeditor.fields import RichTextField

"""
The walktrough tutorial I Think Therefore I Blog
from Code Institute has been used
to help with the code in this project.
"""

# Status of a post

STATUS = ((0, "Draft"), (1, "Published"))

class Category(models.Model):
    '''Category model'''
    category_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.category_name


class Tool(models.Model):
    tool_name = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author_name = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tool_items')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categories', null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    keywords = models.CharField(max_length=100)
    method_details = RichTextField(blank=True, null=True)
    time_required = models.DecimalField(max_digits=5, decimal_places=2)
    related_website = models.URLField(max_length=200, blank=True)
    related_image = CloudinaryField('image', default='placeholder', blank=True)
    published_status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='tool_likes', blank=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.tool_name
    
    # Helper method to return number of likes on a tool item
    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    tool = models.ForeignKey(Tool, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=50)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['date_added']
    
    def __str__(self):
        return f"Comment {self.content} by {self.name}"

