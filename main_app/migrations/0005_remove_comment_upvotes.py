# Generated by Django 4.2.7 on 2023-11-27 19:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_remove_comment_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='upvotes',
        ),
    ]
