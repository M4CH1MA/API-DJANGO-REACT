from django.db import models
# Create your models here.

class Enterprise(models.Model):
    name = models.CharField(max_length=185)
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
