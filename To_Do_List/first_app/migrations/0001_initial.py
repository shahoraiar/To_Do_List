# Generated by Django 4.2.3 on 2023-08-20 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TaskModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskTitle', models.CharField(max_length=50)),
                ('taskDescription', models.CharField(max_length=200)),
                ('is_completed', models.BooleanField()),
            ],
        ),
    ]
