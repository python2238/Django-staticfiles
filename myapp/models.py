from django.db import models

class user(models.Model):
    name = models.CharField(max_length=50 )
    Contact = models.IntegerField(unique=True)

    def __str__(self):
        return self.name
