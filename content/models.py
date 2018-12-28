from django.db import models


class Task:
    pass


class OS:
    pass


class Client(models.Model):
    mac_address = models.CharField(max_length=30, editable=False)
    name = models.CharField(max_length=30, default="")
    public_key = models.BigIntegerField(editable=False, unique=True)
    current_task = models.ForeignKey(Task, on_delete=models.DO_NOTHING)
    created = models.DateTimeField(auto_created=True, editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)


class Task(models.Model):
    script_id = models.IntegerField(unique=True, primary_key=True, editable=False)
    script = models.TextField(editable=False)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, editable=False)
    assigned = models.DateTimeField(auto_created=True, editable=False)
    completed = models.DateTimeField(null=True, editable=False)


class Version(models.Model):
    version_id = models.IntegerField(unique=True, primary_key=True)
    release_url = models.TextField()
    os_version = models.ForeignKey(OS, on_delete=models.DO_NOTHING)
    created = models.DateTimeField(editable=False, auto_created=True)


class OS(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created = models.DateTimeField(editable=False, auto_created=True)