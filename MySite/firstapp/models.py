from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.name


class Website(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # on_delete=models.CASCADE
    name = models.CharField(max_length=250, unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name


class Content(models.Model):
    website = models.ForeignKey(Website, on_delete=models.CASCADE)  # on_delete=models.CASCADE
    name = models.CharField(max_length=250, unique=True)
    # content = models.TextField()
    # content = RichTextField()
    content = RichTextUploadingField()
    image = models.ImageField(upload_to='firstapp/images')

    def __str__(self):
        return self.name

    

# class Test(models.Model):
#     ma_so = models.AutoField(primary_key=True)
#     ten = models.CharField(max_length=150, unique=True)

#     def __str__(self):
#         return self.ten

class Member(models.Model):
    username=models.TextField(max_length=250, unique=True)
    password=models.TextField(max_length=100, null=True)
    fullname=models.TextField(max_length=250)
    email=models.EmailField(unique=True)
    address=models.TextField(max_length=250)
    
    def __str__(self):
        return self.name