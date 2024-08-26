from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=120)


    def __str__(self):
        return self.name
    

#

class Books(models.Model):
    name = models.CharField(max_length=120)
    categories = models.ManyToManyField(Category, verbose_name='categories')
    price = models.IntegerField()
    description = models.TextField()
    author = models.CharField(max_length=120,null=True,default=None)
    image = models.URLField(verbose_name='Photo Url',null=True,default=None)

    def __str__(self):
        return self.name

