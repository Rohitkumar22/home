from django.db import models

class Question(models.Model):
    question=models.CharField(max_length=100)

class Choice(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    choice=models.CharField(max_length=20)
    stats=models.IntegerField(default=0)

    