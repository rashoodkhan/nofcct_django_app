from django.db import models
from django.contrib.auth.models import  User
import os

# Create your models here.

def get_upload_path(self,filename):
    return os.path.join("files_uploaded", filename)

class Blog(models.Model):
    title = models.CharField(max_length=50)
    date_posted = models.DateTimeField('Posted Date',auto_now_add=True)
    content = models.TextField()
    author = models.ForeignKey(User)

    def __unicode__(self):
        return self.title

class Event(models.Model):
    name = models.CharField(max_length=50)
    start_date = models.DateTimeField('Start Time',auto_now_add=True)
    end_date = models.DateTimeField('End Time')
    venue = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name

class FileManager(models.Model):
    title = models.CharField(max_length=50)
    CATEGORY = (
        ('Audio','Audio'),
        ('Video','Video'),
        ('Document','Document')
    )
    category = models.CharField('File Category', choices=CATEGORY, max_length=50)
    file_uploaded = models.FileField(upload_to='files_uploaded/')