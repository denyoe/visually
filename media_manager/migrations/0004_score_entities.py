# Generated by Django 2.1.5 on 2019-02-09 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media_manager', '0003_auto_20190209_2029'),
    ]

    operations = [
        migrations.AddField(
            model_name='score',
            name='entities',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]