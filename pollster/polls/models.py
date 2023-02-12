from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import UserManager
from django.contrib.auth.models import User
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

class VotesMember(models.Model):
    choice =  models.ForeignKey(Choice,on_delete = models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
class Comments(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    text= models.CharField(max_length = 300)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    date =  models.DateField(auto_now_add = True)
