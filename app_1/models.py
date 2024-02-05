from django.db import models

# Create your models here.
class Registration_form(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.TextField()
    phone_no = models.CharField(max_length=50)