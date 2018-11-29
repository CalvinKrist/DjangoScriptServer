from django.db import models
print()

# Create your models here.
class Client(models.Model):
    mac  = models.CharField(max_length=30, default="")
    name = models.CharField(max_length=30, default="")
    script_id = models.IntegerField(default=0)
    script = models.TextField(default="")