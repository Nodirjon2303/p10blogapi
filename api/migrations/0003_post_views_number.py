# Generated by Django 4.0.5 on 2022-06-13 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='views_number',
            field=models.BigIntegerField(default=0, null=True),
        ),
    ]