from django.db import models

# Create your models here.
class Shortner(models.Model):
    url = models.URLField(max_length=2000)
    link = models.CharField(max_length=10, unique=True)

    class Meta:
        ordering = [ 'link']
    
    def __str__(self):
        return self.url