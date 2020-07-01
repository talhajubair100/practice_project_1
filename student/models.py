from django.db import models

class Student(models.Model):
    full_name = models.CharField(max_length=50)
    std_class = models.CharField(max_length=10)
    mobile_number = models.CharField(max_length=11)
    address = models.CharField(max_length=50)
    gender = models.CharField(max_length=7)
    age = models.CharField(max_length=2)

    def __str__(self):
        return self.full_name

