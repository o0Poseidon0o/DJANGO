from django.contrib import admin
from .models import Category, Website,Test

# Register your models here.
admin.site.register(Category)
admin.site.register(Website)
admin.site.register(Test)