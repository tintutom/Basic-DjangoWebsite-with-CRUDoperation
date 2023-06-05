from django.db import models

class AdminSignup(models.Model):
    username=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    pass1=models.CharField(max_length=100)
    pass2=models.CharField(max_length=100)
    is_admin=models.BooleanField(default=False)
