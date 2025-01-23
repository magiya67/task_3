from django.db import models

class MyModel(models.Model):
    content = models.CharField(max_length=100)

    def __str__(self):
        return self.content

# Create your models here.
