from django.db import models
print()

# Create your models here.
class Client(models.Model):
    mac  = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    script_id = models.IntegerField()
    script = models.TextField()
