# Generated by Django 3.2 on 2021-07-28 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QuizApp', '0003_basic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basic',
            name='option3',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='basic',
            name='option4',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
