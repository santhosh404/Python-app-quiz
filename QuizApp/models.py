from django.db import models

# Create your models here.

class Basic(models.Model):
    question=models.TextField()
    option1=models.CharField(max_length=100)
    option2=models.CharField(max_length=100)
    option3=models.CharField(max_length=100)
    option4=models.CharField(max_length=100)
    correct_ans=models.CharField(max_length=100)


class DataTypes(models.Model):
    question=models.TextField()
    option1=models.CharField(max_length=100)
    option2=models.CharField(max_length=100)
    option3=models.CharField(max_length=100)
    option4=models.CharField(max_length=100)
    correct_ans=models.CharField(max_length=100)

class Operators(models.Model):
    question=models.TextField()
    option1=models.CharField(max_length=100)
    option2=models.CharField(max_length=100)
    option3=models.CharField(max_length=100)
    option4=models.CharField(max_length=100)
    correct_ans=models.CharField(max_length=100)



class Con_statements(models.Model):
    question=models.TextField()
    option1=models.CharField(max_length=100)
    option2=models.CharField(max_length=100)
    option3=models.CharField(max_length=100)
    option4=models.CharField(max_length=100)
    correct_ans=models.CharField(max_length=100)

class looping(models.Model):
    question=models.TextField()
    option1=models.TextField()
    option2=models.TextField()
    option3=models.TextField()
    option4=models.TextField()
    correct_ans=models.TextField()

class functions(models.Model):
    question=models.TextField()
    option1=models.CharField(max_length=100)
    option2=models.CharField(max_length=100)
    option3=models.CharField(max_length=100)
    option4=models.CharField(max_length=100)
    correct_ans=models.CharField(max_length=100)

class ExceptionHandling(models.Model):
    question=models.TextField()
    option1=models.CharField(max_length=100)
    option2=models.CharField(max_length=100)
    option3=models.CharField(max_length=100)
    option4=models.CharField(max_length=100)
    correct_ans=models.CharField(max_length=100)