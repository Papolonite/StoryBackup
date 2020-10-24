from django.db import models

# Create your models here.
class Activities(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return self.name

class People(models.Model):
    full_name = models.CharField(max_length=100)
    nickname = models.CharField(max_length=20)
    gender_choices = [
        ('Male','Male'),
        ('Female','Female')
    ]
    gender = models.CharField(max_length=9, choices=gender_choices)
    birthday = models.DateField()
    activities_registered = models.ForeignKey(Activities, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name