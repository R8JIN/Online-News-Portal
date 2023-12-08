from django.contrib import admin
from News import models
# Register your models here.
admin.site.register(models.Category)
# admin.site.register(models.SubCategory)
admin.site.register(models.NewsPost)
admin.site.register(models.Comment)
admin.site.register(models.Bookmark)