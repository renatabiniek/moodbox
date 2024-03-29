# Generated by Django 3.2.14 on 2022-08-21 11:44

import cloudinary.models
from decimal import Decimal
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'ordering': ['category_name'],
            },
        ),
        migrations.CreateModel(
            name='Tool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tool_name', models.CharField(max_length=30, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('keywords', models.CharField(max_length=100)),
                ('method_details', models.CharField(blank=True, max_length=500, null=True)),
                ('time_required', models.DecimalField(decimal_places=2, max_digits=5, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))])),
                ('related_website', models.URLField(blank=True)),
                ('related_image', cloudinary.models.CloudinaryField(blank=True, default='placeholder', max_length=255, verbose_name='image')),
                ('published_status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0)),
                ('author_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tool_items', to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='toolkit.category')),
                ('likes', models.ManyToManyField(blank=True, related_name='tool_likes', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date_added'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('approved', models.BooleanField(default=False)),
                ('tool', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='toolkit.tool')),
            ],
            options={
                'ordering': ['date_added'],
            },
        ),
    ]
