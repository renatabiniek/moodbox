# Generated by Django 3.2.14 on 2022-08-06 15:32

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toolkit', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tool',
            name='approved',
        ),
        migrations.AlterField(
            model_name='tool',
            name='method_details',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tool',
            name='tool_name',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
