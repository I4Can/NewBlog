# Generated by Django 2.1 on 2019-02-06 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.CharField(choices=[('1', 'zml'), ('2', 'thd')], max_length=255),
        ),
    ]
