from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User


USER = get_user_model()


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
    location = models.ForeignKey('Location', null=True, on_delete=models.PROTECT, verbose_name='Location')
    agency = models.ForeignKey('Agency', null=True, on_delete=models.PROTECT, verbose_name='Agency')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = "Rocket"
        verbose_name_plural = "Rocket"
        ordering = ['time_launch']


class Type(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('type', kwargs={'type_slug': self.slug})


class Location(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(blank=True)
    country_code = models.CharField(max_length=5)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('location', kwargs={'slug': self.slug})


class Agency(models.Model):
    OPTIONS = (
        ('commercial', 'Commercial'),
        ('government', 'Government'),
    )
    name = models.CharField(max_length=99, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    content = models.TextField(blank=True)
    type = models.CharField(max_length=12, choices=OPTIONS)



    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('agency', kwargs={'agency_slug': self.slug})
    
    class Meta:
        verbose_name = "Agency"
        verbose_name_plural = "Agency"
        ordering = ['name']   


class Launcher(models.Model):
    title = models.CharField(max_length=255)
    # description = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    family = models.CharField(max_length=255)
    full_name = models.CharField(max_length=1255)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_title': self.title})

    class Meta:
        verbose_name = "Launcher"
        verbose_name_plural = "Launcher"
        ordering = ['title']   
    

