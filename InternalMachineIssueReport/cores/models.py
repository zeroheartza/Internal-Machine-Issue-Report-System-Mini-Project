from django.db import models




class Machine(models.Model):
    name = models.CharField(max_length=150, unique=True, null=False, blank=False)

    def __str__(self):
        return self.name

