# Ex02 Django ORM Web Application
## Date: 

## AIM
To develop a Django application to store and retrieve data from a Movies Database using Object Relational Mapping(ORM).


## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
model.py
from django.db import models
from django.contrib import admin
class Student(models.Model):
    stu_id=models.IntegerField(primary_key=True)
    stu_name=models.CharField(max_length=30)

class StudentAdmin(admin.ModelAdmin):
    list_display=('stu_id','stu_name')# Create your models here.
admin.py

from django.contrib import admin
from.models import Student,StudentAdmin
admin.site.register(Student,StudentAdmin)
# Register your models here.
```

## OUTPUT

![alt text](image.png)


## RESULT
Thus the program for creating movies database using ORM hass been executed successfully
