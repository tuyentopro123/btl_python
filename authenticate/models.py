from django.db import models
from django.utils import timezone

# Create your models here.
class Feedback(models.Model):
    user_send = models.CharField(max_length=200,blank = False, null=False)
    messages = models.TextField(max_length=1000,blank = False, null=False)
    time_create = models.DateTimeField(default=timezone.datetime.now())

class Quiz(models.Model):
    question = models.CharField(max_length=800,blank = False, null=False)
    op1 = models.CharField(max_length=500,blank = False,null=True)
    op2 = models.CharField(max_length=500,blank = False,null=True)
    op3 = models.CharField(max_length=500,blank = False,null=True)
    op4 = models.CharField(max_length=500,blank = False,null=True)
    ans = models.CharField(max_length=500,blank = False,null=True)
    
    def __str__(self):
        return self.question