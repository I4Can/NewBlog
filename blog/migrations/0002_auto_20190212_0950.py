# Generated by Django 2.1 on 2019-02-12 09:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tag',
            old_name='content',
            new_name='title',
        ),
    ]
