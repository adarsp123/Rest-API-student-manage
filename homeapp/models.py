from django.db import models

# Create your models here.
class Student(models.Model):
    First_name=models.CharField(max_length=100)
    Last_name=models.CharField(max_length=100)
    address=models.CharField(max_length=250)
    roll_number=models.IntegerField()
    mobile_number=models.CharField(max_length=100)

    def __str__ (self):
        return self.First_name + " " + self.Last_name

