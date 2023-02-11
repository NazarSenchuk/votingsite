from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import UserManager

class MyUser(AbstractBaseUser):
    username = models.CharField(max_length = 100,unique= True)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    objects = UserManager()
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
    user = models.ForeignKey(MyUser,on_delete=models.CASCADE)

