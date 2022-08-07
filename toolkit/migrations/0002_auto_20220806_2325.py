# Generated by Django 3.2.14 on 2022-08-06 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toolkit', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['category_name']},
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=200, null=True, unique=True),
        ),
    ]