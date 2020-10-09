from xmlrpc.client import DateTime

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from datetime import *
from datetime import datetime

# Create your models here.

class LeafInventory(models.Model):

    in_Date = models.DateField()
    in_Time = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(23.59) ])
    tray_Id = models.IntegerField()
    temp = models.FloatField()
    weight = models.FloatField(validators=[MinValueValidator(0)])
    out_Date = models.DateField()
    out_Time = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(23.59) ])

    class Meta:
        db_table = 'inventory'


class TeaGrades(models.Model):
    teaGrade = models.CharField(max_length=10, unique=True)

    class Meta:
        db_table = 'tea_grade'

    def __str__(self):
        return self.teaGrade


class Final_product_sub(models.Model):

    subID = models.IntegerField(blank=True)
    teaGrade = models.ForeignKey(TeaGrades, on_delete=models.CASCADE)
    gradeWeight = models.FloatField(validators=[MinValueValidator(0)])

    class Meta:
        db_table="Final_product_sub"


class Final_product_Main(models.Model):

    subID = models.IntegerField(blank=True)
    totalWeight = models.FloatField(blank=True, validators=[MinValueValidator(0)])
    date = models.DateField(default= datetime.now)

    class Meta:
        db_table="Final_product_Main"

