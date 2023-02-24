from django.db import models

# Create your models here.
class Employee(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    address=models.TextField(max_length=40)


    def __str__(self):
        return self.name