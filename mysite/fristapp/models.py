from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=150, unique=True)
    def __str__(self):
        return self.name

class Website(models.Model):
    category=models.ForeignKey(Category, on_delete=models.PROTECT)
    name=models.CharField(max_length=250, unique=True)
    url=models.URLField(unique=True)

    def __str__(self):
        return self.name
class Test(models.Model):
    ma_so=models.AutoField(primary_key=True)
    ten=models.CharField(max_length=150, unique=True)
    def __str__(self):
        return self.name