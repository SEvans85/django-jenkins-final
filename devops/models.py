from django.db import models

# Create your models here.

from django.db import models

class PostIt(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    details = models.TextField()

    def __str__(self):
        return self.details[:20]

    class Meta:
        db_table = 'postit'