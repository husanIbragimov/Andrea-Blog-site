# Generated by Django 3.2.13 on 2022-06-09 16:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_comment_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
