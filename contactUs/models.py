from django.db import models


class companyProfile(models.Model):
    title = models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to='company/thumbnails/')
    map_link = models.URLField(max_length=255)
    address = models.CharField(max_length=255)
    email = models.EmailField()
    facebook = models.URLField(max_length=255, blank=True, null=True)
    twitter = models.URLField(max_length=255, blank=True, null=True)
    linkedin = models.URLField(max_length=255, blank=True, null=True)
    google = models.URLField(max_length=255, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class feetBack(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    comment = models.TextField()

    def __str__(self):
        return self.name
