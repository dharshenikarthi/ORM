from django .db import models
from django.contrib import admin
class Bank(models.Model):
  name=models.CharField(max_length=50)
  accountno=models.IntegerField(primary_key="accountno")
  dob=models.DateField()
  aadharno=models.IntegerField()
  email=models.EmailField() 
  branch=models.CharField(max_length=21)
  photo=models.ImageField()

class BankAdmin(admin.ModelAdmin):
 list_display=('name','accountno','aadharno','dob','email','branch','photo')
