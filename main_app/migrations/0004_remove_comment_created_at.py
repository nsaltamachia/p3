# Generated by Django 4.2.7 on 2023-11-27 19:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_remove_comment_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='created_at',
        ),
    ]
