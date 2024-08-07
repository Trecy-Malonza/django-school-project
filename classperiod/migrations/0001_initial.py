# Generated by Django 4.2.14 on 2024-07-14 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClassPeriod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateField()),
                ('end_time', models.DateField()),
                ('course', models.CharField(max_length=50)),
                ('classroom', models.CharField(max_length=150)),
                ('day_of_the_week', models.CharField(max_length=7)),
            ],
        ),
    ]
