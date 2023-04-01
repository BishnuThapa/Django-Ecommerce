from django.db import models

# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField()
    desctiption = models.TextField(max_length=255)
    cat_image = models.ImageField(upload_to='photos/categories', blank=True)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'