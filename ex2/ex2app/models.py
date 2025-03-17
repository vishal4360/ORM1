from django.db import models
from django.contrib import admin
class Student(models.Model):
    stu_id=models.IntegerField(primary_key=True)
    stu_name=models.CharField(max_length=30)

class StudentAdmin(admin.ModelAdmin):
    list_display=('stu_id','stu_name')# Create your models here.
