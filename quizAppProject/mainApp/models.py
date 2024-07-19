from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Qcategory(models.Model):
    title=models.CharField(max_length=100)
    detail=models.TextField()
    image=models.ImageField(upload_to='Category_Images/')

    def __str__(self):
        return self.title
    
    class Meta:
         verbose_name_plural='Catergories'
    
class Question(models.Model):
    category=models.ForeignKey(Qcategory, on_delete=models.CASCADE)
    question=models.TextField()
    option1=models.CharField(max_length=200)
    option2=models.CharField(max_length=200)
    option3=models.CharField(max_length=200)
    option4=models.CharField(max_length=200)
    time_limit=models.IntegerField()
    level=models.CharField(max_length=100)
    right_option=models.CharField(max_length=100)

def __str__(self):
        return self.question

# submitted answer -> recording
class SubAnswer(models.Model):
    question=models.ForeignKey(Question, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    right_choice=models.TextField(max_length=200)
    
    class Meta:
         verbose_name_plural='Recorded Answer'
