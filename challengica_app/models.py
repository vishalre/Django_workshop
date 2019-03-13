from django.db import models
from datetime import datetime
from django.utils import timezone
from random import randint
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class SetNo(models.Model):
    setno = models.IntegerField(primary_key=True)

    def __str__(self):
        return str(self.setno)

class Question(models.Model):
    setno = models.ForeignKey(SetNo, on_delete=models.CASCADE)
    ques_img = models.TextField(max_length=100)
    ques_text = models.TextField(max_length=3000)
    ans_text = models.TextField(max_length=1000)

    def __str__(self):
        return "Set no: %s\nQuestion: %s\nAnswer: %s" % (self.setno, self.ques_text, self.ans_text)

def setendtime():
    return timezone.now() + timezone.timedelta(minutes=35)
    
class Contestant(models.Model):
    username = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    contact = models.CharField(max_length=10)
    points = models.IntegerField(default=0)
    year = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(5), MinValueValidator(1)]
    )
    starttime = models.DateTimeField('start time', default = timezone.now)
    endtime = models.DateTimeField('end time', default = setendtime)
    setno = models.ForeignKey(SetNo, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return "Username: %s\n" % (self.username)

    