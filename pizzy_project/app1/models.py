from django.db import models

from users.models import User

# Create your models here.

class Teatcher(User):
    isBefore = models.BooleanField(default=False)

class Student(User):
    date_of_birth = models.DateField(null=True, verbose_name="date de naissance")

#..........

class Discipline(models.Model):
    libelle = models.CharField(max_length=100)

class LearnBox(models.Model):
    libelle = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    owner = models.ForeignKey(Teatcher, on_delete=models.CASCADE)
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE)