# Generated by Django 4.2.13 on 2024-06-30 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('code', models.PositiveSmallIntegerField()),
                ('date_of_birth', models.DateField()),
                ('country', models.CharField(max_length=20)),
                ('bio', models.TextField()),
                ('age', models.SmallIntegerField()),
                ('nationality', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('course', models.CharField(max_length=40)),
                ('immediate_contact', models.CharField(max_length=20)),
            ],
        ),
    ]