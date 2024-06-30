from django.db import models
from datetime import datetime

class Contact(models.Model):

     sno = models.AutoField(primary_key=True)
     name = models.CharField(max_length=255)
     email = models.EmailField(max_length=250, unique=True)
     mobile = models.IntegerField()
     message = models.TextField()
     date= models.DateTimeField(default=datetime.now, blank=True)

     def __str__(self):
          return self.name


class Post(models.Model):

     sno = models.AutoField(primary_key=True)
     title = models.CharField(max_length=255)
     content = models.TextField()
     image = models.ImageField(upload_to='image/')
     time = models.DateTimeField(auto_now=True, blank=True)

     def __str__(self):
          return self.title




CHOICE = (
     ('one year', 'one year'),
     ('Two year', 'Two year'),
     ('Three year', 'Three year'),
     ('Four year', 'Four year'),
     ('Five year', 'Five year'),

)
class Addjob(models.Model):

     jobtitle = models.CharField(max_length=255)
     salary = models.IntegerField()
     experience = models.CharField(choices=CHOICE, max_length=100)
     location = models.TextField()
     date = models.DateTimeField(default=datetime.now, blank=True)

     def __str__(self):
          return self.jobtitle

class Addnotification(models.Model):
     notification = models.TextField()
     date = models.DateTimeField(default=datetime.now, blank=True)



class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    address = models.TextField(max_length=100)
    phone = models.IntegerField()

    def __str__(self):
        return self.name


class Feedback(models.Model):
     name = models.CharField(max_length=100)
     email = models.EmailField(max_length=100)
     feedback = models.TextField()
     date = models.DateTimeField(default=datetime.now, blank=True)

     def __str__(self):
          return self.name

class Complain(models.Model):
     name = models.CharField(max_length=100)
     email = models.EmailField(max_length=100)
     complain = models.TextField()
     date = models.DateTimeField(default=datetime.now, blank=True)

     def __str__(self):
          return self.name








