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
class content(models.Model):
    website=models.ForeignKey(Website, on_delete=models.PROTECT)
    name=name=models.CharField(max_length=250, unique=True)
    content=models.TextField()
    image=models.ImageField(upload_to='fristapp/image')

    def __str__(self):
        return self.name


