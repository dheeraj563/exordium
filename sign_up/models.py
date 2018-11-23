from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    roll_no = models.IntegerField()
    branch = models.CharField(max_length=30)
    image = models.ImageField(upload_to='media')