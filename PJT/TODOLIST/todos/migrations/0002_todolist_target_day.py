# Generated by Django 4.2.2 on 2023-09-29 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='target_day',
            field=models.DateField(blank=True, null=True),
        ),
    ]
