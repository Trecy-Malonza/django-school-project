# Generated by Django 4.2.14 on 2024-07-14 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_alter_student_id'),
        ('class', '0004_alter_class_id'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Class',
            new_name='SchoolClass',
        ),
    ]