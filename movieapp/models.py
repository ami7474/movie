from django.db import models



# Create your models here.
class mlist(models.Model):
    name=models.CharField(max_length=100)
    desc=models.TextField()
    year=models.IntegerField()
    img=models.ImageField(upload_to='pics')

    def __str__(self):
        return self.name
