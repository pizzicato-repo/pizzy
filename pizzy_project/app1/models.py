from django.db import models

from users.models import User

# Create your models here.

class Teatcher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    isIndependant = models.BooleanField(default=False, verbose_name="independant")
    def __str__(self):
        return self.user.username

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(null=True, verbose_name="date de naissance")
    def __str__(self):
        return self.user.username

#..........

class Discipline(models.Model):
    libelle = models.CharField(max_length=100)

class LearnBox(models.Model):
    libelle = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    owner = models.ForeignKey(Teatcher, on_delete=models.CASCADE)
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE)