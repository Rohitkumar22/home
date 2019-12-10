from django.shortcuts import render
from .models import Question,Choice

def hello(req):
    return render(req,'res/index.html')

def quiz(req):
    Task= Question.objects.all()
    return render(req,'res/quiz.html',{'ques':Task})

