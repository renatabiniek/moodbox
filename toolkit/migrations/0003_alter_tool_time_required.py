# Generated by Django 3.2.14 on 2022-08-01 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toolkit', '0002_auto_20220801_1817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tool',
            name='time_required',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
    ]
