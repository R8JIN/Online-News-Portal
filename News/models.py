from django.db import models
from ckeditor.fields import RichTextField
from datetime import datetime
from accounts.models import User
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=255)
    caption = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.id} {self.title}'

    class Meta:
        verbose_name = '1. Category'


# class SubCategory(models.Model):
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     title = models.CharField(max_length=255)
#     caption = models.CharField(max_length=255)
#
#     def __str__(self):
#         return f'{self.category}-{self.title}'
#
#     class Meta:
#         verbose_name = '2.Subcategory'


class NewsPost(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE,default="")
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.now(), blank=True)
    image = models.ImageField(upload_to='News/categories', blank=False, null=False)
    caption = models.CharField(max_length=256, default="")
    details = RichTextUploadingField(default=None)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '2. NewsPost'


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(NewsPost, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.now(), blank=True)
    comment = RichTextUploadingField(default=None)


class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(NewsPost, on_delete=models.CASCADE)
