from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Profile(models.Model):
    idno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=40)
    username=models.CharField(max_length=30)
    choices = (
        ('C', 'C'),
        ('C++', 'C++'),
        ('Java', 'Java'),
        ('Python', 'Python'),
    )
    intrest = models.CharField(max_length=6,choices=choices,blank=True)
    marks=models.IntegerField(default=0)
    choice = (
        ('Legendary', 'Legendary'),
        ('Titan', 'Titan'),
        ('Champion', 'Champion'),
        ('Gold', 'Gold'),
        ('Silver', 'Silver'),
        ('Bronze', 'Bronze'),
    )
    category=models.CharField(max_length=15,choices=choice,blank=True)

    def __str__(self):
        return self.username

class ConnectRequest(models.Model):
    idno = models.AutoField(primary_key=True)
    sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="sender")
    receiver = models.ForeignKey(Profile,on_delete=models.CASCADE, related_name="receiver")
    
    choice=(
        ("Accepted","Accepted"),
        ("Declined","Declined"),
        ("Pending","Pending")
    )

    status=models.CharField(max_length=10,choices=choice,blank=True)
    
    def __str__(self):
        return f"{self.sender} to {self.receiver} status {self.status}"



class C(models.Model):
    qno=models.AutoField(primary_key=True)
    question=models.TextField()
    
    option1=models.CharField(max_length=100,null='true')
    option2=models.CharField(max_length=100,null='true')
    option3=models.CharField(max_length=100,null='true')
    option4=models.CharField(max_length=100,null='true')
    ans=models.CharField(max_length=1,null='true')
    choices = (
        ('1', option1),
        ('2', option2),
        ('3', option3),
        ('4', option4),
    )
    answer=models.CharField(max_length=1, choices=choices)
    def __str__(self):
        return self.question


class Cpp(models.Model):
    qno=models.AutoField(primary_key=True)
    question=models.TextField()
    option1=models.CharField(max_length=100,null='true')
    option2=models.CharField(max_length=100,null='true')
    option3=models.CharField(max_length=100,null='true')
    option4=models.CharField(max_length=100,null='true')
    ans=models.CharField(max_length=1,null='true')
    choices = (
        ('1', option1),
        ('2', option2),
        ('3', option3),
        ('4', option4),
    )
    answer=models.CharField(max_length=1, choices=choices)
    def __str__(self):
        return self.question

class Java(models.Model):
    qno=models.AutoField(primary_key=True)
    question=models.TextField()
    option1=models.CharField(max_length=100,null='true')
    option2=models.CharField(max_length=100,null='true')
    option3=models.CharField(max_length=100,null='true')
    option4=models.CharField(max_length=100,null='true')
    ans=models.CharField(max_length=1,null='true')
    choices = (
        ('1', option1),
        ('2', option2),
        ('3', option3),
        ('4', option4),
    )
    answer=models.CharField(max_length=1, choices=choices)
    def __str__(self):
        return self.question


class Python(models.Model):
    qno=models.AutoField(primary_key=True)
    question=models.TextField()
    option1=models.CharField(max_length=100,null='true')
    option2=models.CharField(max_length=100,null='true')
    option3=models.CharField(max_length=100,null='true')
    option4=models.CharField(max_length=100,null='true')
    ans=models.CharField(max_length=1,null='true')
    choices = (
        ('1', option1),
        ('2', option2),
        ('3', option3),
        ('4', option4),
    )
    answer=models.CharField(max_length=1, choices=choices)
    def __str__(self):
        return self.question
