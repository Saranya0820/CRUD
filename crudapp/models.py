from django.db import models

class Employee(models.Model):
    name=models.CharField(max_length=25,blank=False,null=False)
    email=models.EmailField(max_length=50,blank=False)
    age=models.IntegerField(default=0)
    address=models.CharField(max_length=25,blank=False,null=False)
    gender=models.CharField(max_length=25,blank=False,null=False)

    def __str__(self):
        return self.name