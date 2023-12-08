from django.db import models
from django import forms
# Create your models here.

class Client_Info(models.Model):
    cName = models.CharField(max_length=20, null=False)
    cUid = models.CharField(max_length=50,null=False,default='')
    mdt = models.DateTimeField(auto_now=True) 
    favorite = models.TextField(default='')

    def __str__(self):
        return self.cName

class Client_History(models.Model):
    cUid = models.CharField(max_length=50,null=False,default='')
    mdt = models.DateTimeField(auto_now=True)
    cHistory = models.TextField(default='')

    def __str__(self):
        return self.cUid