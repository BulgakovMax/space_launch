from django.db import models
from django.urls import reverse


class Rocket(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    time_launch = models.DateTimeField(auto_now_add=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    type = models.ForeignKey('Type', on_delete=models.PROTECT, verbose_name='Type')
    # location = models.ForeignKey('Location', on_delete=models.PROTECT, verbose_name='Location')


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = "Rocket"
        verbose_name_plural = "Rocket"
        ordering = ['time_create', 'title']


class Type(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('type', kwargs={'type_slug': self.slug})


# class Location(models.Model):
#     name = models.CharField(max_length=100, db_index=True)
#     slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
#
#     def __str__(self):
#         return self.name
#
#     def get_absolute_url(self):
#         return reverse('location', kwargs={'type_slug': self.slug})
