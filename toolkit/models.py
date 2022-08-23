"""Models"""
from decimal import Decimal
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from cloudinary.models import CloudinaryField

# The walktrough tutorial I Think Therefore I Blog
# from Code Institute has been used to help with the code in this project.

# Status of a post
STATUS = ((0, "Draft"), (1, "Published"))


class Category(models.Model):
    """Category model"""
    category_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=False)

    class Meta:
        """Order category names in ascending order"""
        ordering = ['category_name']

    def __str__(self):
        return self.category_name


class Tool(models.Model):
    """Tool model"""
    tool_name = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author_name = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='tool_items')
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE,
        related_name='categories', null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    keywords = models.CharField(max_length=100)
    method_details = models.TextField(null=True)
    time_required = models.DecimalField(
        max_digits=5, decimal_places=2,
        validators=[MinValueValidator(Decimal('0.01'))])
    related_website = models.URLField(max_length=200, blank=True)
    related_image = CloudinaryField('image', default='placeholder', blank=True)
    published_status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='tool_likes', blank=True)

    class Meta:
        """Order tools by date added in descending order"""
        ordering = ['-date_added']

    def __str__(self):
        return self.tool_name

    def number_of_likes(self):
        """Helper method to return number of likes on a tool item"""
        return self.likes.count()


class Comment(models.Model):
    """Comment model"""
    tool = models.ForeignKey(
        Tool, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=50)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        """Order comments by date added in ascending order"""
        ordering = ['date_added']

    def __str__(self):
        return f"Comment {self.content} by {self.name}"
