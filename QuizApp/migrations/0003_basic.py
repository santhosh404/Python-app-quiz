# Generated by Django 3.2 on 2021-07-27 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QuizApp', '0002_alter_quizapplication_question'),
    ]

    operations = [
        migrations.CreateModel(
            name='Basic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('option1', models.CharField(max_length=100)),
                ('option2', models.CharField(max_length=100)),
                ('option3', models.CharField(max_length=100)),
                ('option4', models.CharField(max_length=100)),
                ('correct_ans', models.CharField(max_length=100)),
            ],
        ),
    ]
