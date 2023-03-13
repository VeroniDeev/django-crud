from django.db import models

class User(models.Model):
    surname = models.CharField(max_length=25, null=False, blank=False, default='')
    name = models.CharField(max_length=25, null=False, blank=False, default='')
    age = models.IntegerField(null=False, blank=False, default=0)

    def __str__(self) -> str:
        return self.surname
