# Generated by Django 2.2.12 on 2024-07-12 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20240712_0650'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='Student_id',
            field=models.IntegerField(default=1),
        ),
    ]
