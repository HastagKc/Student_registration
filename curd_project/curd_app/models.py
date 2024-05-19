from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    email = models.EmailField(max_length=50,unique=True)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    


