from django.db import models
#from sign_up.models import Student

class stulogin(models.Model):
    roll_no = models.IntegerField()
    password  = models.CharField(max_length=16)


