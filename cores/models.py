from django.db import models


class Machine(models.Model):
    name = models.CharField(max_length=150, unique=True, null=False, blank=False)

    def __str__(self):
        return self.name

class Issue(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE, null=False, blank=False)
    issue = models.CharField(max_length=150, null=False, blank=False)
    description = models.CharField(max_length=250, null=False, blank=False)
    timestamp = models.DateTimeField(null=True,blank=True,auto_now_add=True)
    status = models.CharField(max_length=20,default="Open", null=False, blank=False)

class History(models.Model):
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE, null=False, blank=False)
    status = models.CharField(max_length=20, null=False, blank=False)
    timestamp = models.DateTimeField(null=True,blank=True,auto_now_add=True)
    comment = models.CharField(max_length=250, null=True, blank=True)

