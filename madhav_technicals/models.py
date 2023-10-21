from django.db import models

# Create your models here.


class Contact(models.Model):
  firstname = models.CharField(max_length=255,default='')
  lastname = models.CharField(max_length=255,default='')
  Email_Id = models.EmailField(max_length=100,default='')
  subject  = models.CharField(max_length=100,default='')
  Message = models.TextField(default='', blank=True)

  def __str__(self):
    return "%s %s" %(self.firstname , self.lastname )