from django.contrib import admin
from firstapp.models import Category, Website, Content


# Register your models here.
admin.site.register(Category)
admin.site.register(Website)
admin.site.register(Content)
