# Generated by Django 2.1 on 2019-02-12 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20190212_1143'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='last_edit_time',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='修改时间'),
        ),
    ]
