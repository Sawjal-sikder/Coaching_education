from django.db import models


class Gallery(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Photo(models.Model):
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='gallery/photos/')
    description = models.TextField()
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title
