from django.db import models
from datetime import date


class reg(models.Model):
    name=models.CharField(max_length=10)
    subject=models.CharField(max_length=20)
    depart=models.CharField(max_length=20)
    qualification=models.CharField(max_length=20)
    exp=models.IntegerField()
    email=models.EmailField()
    id=models.IntegerField(primary_key=True)
class sreg1(models.Model):
    sname=models.CharField(max_length=10)
    sbranch=models.CharField(max_length=10)
    syear=models.IntegerField()
    semail=models.EmailField()
    id=models.IntegerField(primary_key=True)
class exam12(models.Model):
    busses_CHOICES = (
        ('eee','eee'),
        ('ece','ece'),
        ('cse','cse'),
        ('mech','mech'),
        ('civil','civil'),
    )
    departments = models.CharField(max_length=30, choices=busses_CHOICES)
    exam=models.CharField(max_length=20)
    year=models.IntegerField()
    date=models.DateField(null=True)
class events(models.Model):
    busses_CHOICES = (
        ('eee','eee'),
        ('ece','ece'),
        ('cse','cse'),
        ('mech','mech'),
        ('civil','civil'),
    )
    departments = models.CharField(max_length=30, choices=busses_CHOICES)
    sports_CHOICES = (
        ('cricket','cricket'),
        ('football','football'),
        ('vollyball','vollyball'),
        ('kabadi','kabadi'),
        ('tennis','tennis'),
    )
    sports = models.CharField(max_length=30, choices=sports_CHOICES)
    cultural_CHOICES = (
        ('dance','dance'),
        ('sqit','sqit'),
        ('singing','singing'),
        ('speach','speach'),
    )
    cultural = models.CharField(max_length=30, choices=cultural_CHOICES)
    year=models.IntegerField()
    date=models.DateField(null=True)
class faculty(models.Model):
    busses_CHOICES = (
        ('eee','eee'),
        ('ece','ece'),
        ('cse','cse'),
        ('mech','mech'),
        ('civil','civil'),
    )
    departments = models.CharField(max_length=30, choices=busses_CHOICES)
    name=models.CharField(max_length=20)
    subjects_CHOICES = (
        ('maths','maths'),
        ('physics','physics'),
        ('communication','communication'),
        ('edc','edc'),
        ('electricalmotors','electricalmotors'),
    )
    subjects = models.CharField(max_length=30, choices=subjects_CHOICES)
    year=models.IntegerField()
    date=models.DateField(null=True)
    time=models.TimeField(null=True)
class departments(models.Model):
    busses_CHOICES = (
        ('eee','eee'),
        ('ece','ece'),
        ('cse','cse'),
        ('mech','mech'),
        ('civil','civil'),
    )
    departments = models.CharField(max_length=30, choices=busses_CHOICES)
    flor=models.IntegerField()
    blockno=models.IntegerField()
    year=models.IntegerField()
class student(models.Model):
    name=models.CharField(max_length=20)
    busses_CHOICES = (
        ('eee','eee'),
        ('ece','ece'),
        ('cse','cse'),
        ('mech','mech'),
        ('civil','civil'),
    )
    departments = models.CharField(max_length=30, choices=busses_CHOICES)
    year=models.IntegerField()
    address=models.TextField(max_length=50)
class data(models.Model):
    data=models.CharField(max_length=100)






